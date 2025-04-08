import logging
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel
from dotenv import load_dotenv
import json
import asyncio
import re
from utils.publish_to_topic import produce
from langchain_openai import ChatOpenAI
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

# Load environment variables from .env file
load_dotenv()

AGENT_OUTPUT_TOPIC = 'mortgage_validated_apps'

model = ChatOpenAI(model="gpt-4o", temperature=0)

SYSTEM_PROMPT = """You're a Credit and Fraud Risk Analyst at River Banking, a leading
    financial institution specializing in personalized mortgage solutions. River Banking
    is committed to responsible lending and fraud prevention through advanced risk
    analysis and data-driven decision-making.

    Your role is to analyze a mortgage applicant's financial profile and supporting
    documentation to produce a Credit and Fraud Risk Assessment Report. This report will
    evaluate the applicant's creditworthiness and flag potential fraud risks based on key
    indicators such as credit score, income stability, debt ratios, and account history.
    Your findings will help determine whether the applicant meets River Banking's lending
    criteria and ensure the integrity of the loan underwriting process.
    """

@tool
def get_fraud_risk_assesment(mortgage_application):
    """
    Gets the applicants fraud risk assessment.
    
     Arg:
        mortgage_application (dict): A dictionary with the following keys:
                customer_email (str): The customer's email.
                borrower_name (str): The customer's name.
                income (int): The customer's yearly income.
                property_address (str): The customer's email.
                property_state (str): The customer's email.
                property_value (int): The customer's email.
                employment_status (str): The customer's email.
                credit_score (float): The customer's email.
                credit_utilization (float): The customer's email.
                debt_to_income_ratio (float): The customer's email.
                open_credit_accounts (float): The customer's email.
                recent_defaults (float): The customer's email.
                payment_history (list): An array of the customer's payment history.
    """
    
    print("Using tool get_fraud_risk_assesment")
    print(f"Calculating the fraud risk for applicant {mortgage_application['borrower_name']}")
    
    example_output = {
    "applicant_id": "C12345678",
    "assessment_timestamp": "2025-03-27T14:35:00Z",
    "risk_score": 72,
    "risk_level": "medium",
    "signals": {
        "payment_anomalies": {
            "consecutive_failures": 2,
            "late_payments_in_last_12_months": 3,
            "method_switch_pattern": ["auto_debit", "manual", "manual"],
            "high_risk_behavior": "true"
        },
        "identity_risk": {
            "email_mismatch": "false",
            "phone_number_recent_change": "true",
            "multiple_policies_same_identity": "false"
        },
        "policy_behavior": {
            "frequent_policy_cancellations": 1,
            "address_change_frequency": 3,
            "policy_lapse_days": 45
        },
        "claim_anomalies": {
            "suspicious_claims_count": 2,
            "claims_within_90_days_of_policy_start": 1
        },
        "external_data_flags": {
            "known_fraud_watchlist_hit": "false",
            "device_fingerprint_mismatch": "true"
            }
        }
    }

    prompt = f"""
      Take the mortgage application and compute the fraud risk assessment.

      Mortgage Application:
      {mortgage_application}

      The output should look like this:
      {json.dumps(example_output)}

      Only include theå output. No additional description is needed.
      Failure to strictly follow the output format will result in incorrect output.
    """

    data = model.invoke([{ "role": "user", "content": prompt }])
    
    print(data.content)
    
    return data

# Output definition for agent
class MortgageValidatedApps(BaseModel):
    """Validated mortgage application"""

    application_id: str
    applicant_id: str
    customer_email: str
    borrower_name: str
    income: int
    payslips: str
    loan_amount: int
    property_address: str
    property_state: str
    property_value: int
    employment_status: str
    credit_score: int
    credit_utilization: float
    debt_to_income_ratio: float
    fraud_risk_score: int
    loan_stack_risk: str
    risk_category: str
    agent_reasoning: str

tools = [get_fraud_risk_assesment]
# model.with_structured_output(MortgageValidatedApps)
graph = create_react_agent(model, tools=tools, state_modifier=SYSTEM_PROMPT, response_format=MortgageValidatedApps)

async def start_agent_flow(mortgage_application):
    example_output = {
        "application_id": "12345",
        "applicant_id": "A001",
        "customer_email": "test@gmail.com",
        "borrower_name": "John Doe",
        "income": 75000,
        "payslips":"s3_arn",
        "loan_amount": 250000,
        "property_address": "123 Demo Road",
        "property_state": "California",
        "property_value": 300000,
        "employment_status": "Full-time",
        "credit_score": 710,
        "credit_utilization": 32.5,
        "debt_to_income_ratio": 36.5,
        "fraud_risk_score": 72,
        "loan_stack_risk": "High",
        "risk_category": "Moderate",
        "agent_reasoning": "Applicant has a good credit score but high credit utilization. Potential loan stacking risk detected."
    }

    inputs = {"messages": [("user", f"""
        Using the applicant's financial profile and payment history, generate a Credit and Fraud Risk Assessment Report
        that evaluates the applicant's creditworthiness and flags any potential fraud indicators. This report will help
        River Banking make informed, responsible mortgage approval decisions that balance risk with opportunity.

        Key Responsibilities:
        - Review the applicant's payment history, income level, credit score, and overall credit utilization to determine credit risk.
        - Use credit report indicators like open accounts, recent defaults, and debt-to-income ratio to assess stability and lending reliability.
        - Run a fraud risk analysis using the dedicated Fraud Risk Assessment tool to identify anomalies or potential red flags.
        - Combine insights from creditworthiness and fraud detection to form a holistic risk profile for underwriting.
        - Flag any inconsistencies or indicators of identity manipulation, falsified documentation, or suspicious financial behavior.

        Use dedicated tools to assess credit and fraud risk:
        - Fraud Risk Assessment Tool - Returns a JSON-formatted analysis that detects fraud risk based on provided applicant data and behavioral patterns.

        Ensure the output is concise, structured, and useful for downstream decision automation.

        Applicant's Mortgage Application and Payment History:
        {mortgage_application}

        Expected Output - Credit and Fraud Risk Assessment Report: The report should be formatted in JSON and include:
        The report should be formatted in JSON and must include the following fields populated based on the analysis:

        application_id, applicant_id, customer_email, borrower_name, income, payslips, loan_amount, property_address,
        property_state, property_value, employment_status, credit_score, credit_utilization,
        debt_to_income_ratio - These should be carried over unchanged from the input.
        fraud_risk_score - A numeric fraud risk score (e.g., 0-100) returned from the Fraud Risk Assessment tool.
        loan_stack_risk - A categorical risk level indicating the likelihood of concurrent or undisclosed loans (e.g., "Low", "Moderate", "High").
        risk_category - An overall credit and fraud risk classification (e.g., "Low", "Moderate", "High").
        agent_reasoning - A brief summary explaining the decision rationale, covering key credit or fraud-related findings.

        Output Format
            The output must be strictly formatted as JSON, with no additional text, commentary, or explanation.

            The JSON should exactly match the following structure:
            {json.dumps(example_output)}
            
            Failure to strictly follow this format will result in incorrect output.
      """)]}

    response = await graph.ainvoke(inputs)   
    last_message_content = response["messages"][-1]
    content = last_message_content.pretty_repr()
    
    json_match = re.search(r"\{.*\}", content, re.DOTALL)

    if json_match:
        fraud_risk_assessment = json_match.group()

        logger.info(f"Response from agent: {fraud_risk_assessment}")
        
        value_for_kakfa = json.loads(fraud_risk_assessment)

        # Write a message to the agent messages topic with the output from this agent
        produce(AGENT_OUTPUT_TOPIC, value_for_kakfa)
        
def lambda_handler(event, context):
    logger.info("Received event:")
    # logger.info(event)

    payload = event.get("payload", {})
    mortgage_application = payload.get("value")
    
    # get_fraud_risk_assesment(mortgage_application)

    if mortgage_application:
        try:
            asyncio.run(start_agent_flow(mortgage_application))
        except Exception as e:
            logger.error(f"Failed to decode value: {e}")

    return {
        'statusCode': 200,
        'body': 'Processed successfully'
    }
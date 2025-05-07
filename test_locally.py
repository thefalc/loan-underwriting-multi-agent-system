import base64
from credit_and_fraud_check import lambda_handler  # Update with the actual file path

def test_locally():
    payload_value = {
      "application_id": "APP-200182",
      "customer_email": "drew.koepp@yahoo.com",
      "borrower_name": "Drew Koepp",
      "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
      "income": 191563,
      "payslips": "s3://riverbank-payslip-bucket/01JR1174EQ8E5HMRY8NXP127MP",
      "loan_amount": 136787,
      "property_address": "419 Ratke Parkways",
      "property_state": "West Virginia",
      "property_value": 182383,
      "employment_status": "self-employed",
      "credit_score": 581,
      "credit_utilization": 88.5,
      "debt_to_income_ratio": 0,
      "open_credit_accounts": 2,
      "recent_defaults": 0,
      "payment_history": {
        "array": [
          {
            "transaction_id": "TX-3000667",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 238,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-07-04T14:44:21.445+00:00"
          },
          {
            "transaction_id": "TX-3000676",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 369,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-06-03T23:20:57.115+00:00"
          },
          {
            "transaction_id": "TX-3002193",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 320,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2025-03-23T15:23:34.361+00:00"
          },
          {
            "transaction_id": "TX-3002585",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 430,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-10-30T11:06:47.068+00:00"
          },
          {
            "transaction_id": "TX-3002673",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 265,
            "status": "failed",
            "failure_reason": "insufficient_funds",
            "payment_date": "2024-05-18T22:25:40.795+00:00"
          },
          {
            "transaction_id": "TX-3003405",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 394,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-06-13T06:45:11.816+00:00"
          },
          {
            "transaction_id": "TX-3005553",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 293,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-11-17T13:54:04.666+00:00"
          },
          {
            "transaction_id": "TX-3005922",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 179,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-12-02T08:43:33.455+00:00"
          },
          {
            "transaction_id": "TX-3007378",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 374,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-06-10T16:46:43.832+00:00"
          },
          {
            "transaction_id": "TX-3007567",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 179,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-08-11T22:36:50.318+00:00"
          },
          {
            "transaction_id": "TX-3007824",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 285,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-04-20T20:59:18.850+00:00"
          },
          {
            "transaction_id": "TX-3000495",
            "applicant_id": "01JR1174EQ8E5HMRY8NXP127MP",
            "method": "auto-debit",
            "amount": 160,
            "status": "failed",
            "failure_reason": "insufficient_funds",
            "payment_date": "2025-04-04T23:46:39.712+00:00"
          }
        ]
      }
    }

    fake_event = {
        "payload": {
            "key": base64.b64encode(b"123").decode('utf-8'),
            "value": payload_value,
            "timestamp": 1743638590453,
            "topic": "mortgage_applications",
            "partition": 5,
            "offset": 463
        }
    }
    
    print(fake_event)

    # result = lambda_handler(fake_event, None)
    # print(result)

if __name__ == "__main__":
    test_locally()

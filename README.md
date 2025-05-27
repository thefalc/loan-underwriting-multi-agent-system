# Credit and Fraud Risk Agent
This is a singular agent that does credit and fraud risk assesment based on a loan application, credit information, and past payment history.

# What you'll need
In order to set up and run the application, you need the following:

* [Python 3.10](https://www.python.org/downloads/) or above
* A [Confluent Cloud](https://www.confluent.io/) account
* A [OpenAI](https://openai.com/api/) API key
* A [LangChain](https://www.langchain.com/) API key
* [Docker](https://www.docker.com/) installed

## Getting set up

### Get the starter code
In a terminal, clone the sample code to your project's working directory with the following command:

```shell
git clone https://github.com/thefalc/loan-underwriting-multi-agent-system.git
```

### Configuration settings

Go into your root project direction and create a `.env` file with your OpenAI and LangChain API details.

```bash
LANGCHAIN_TRACING_V2='true'
LANGCHAIN_API_KEY='REPLACE_ME'
OPENAI_API_KEY='REPLACE_ME'
```

Next, following the [instructions](https://docs.confluent.io/cloud/current/client-apps/config-client.html) to create a new Python client. Once the client downloads, unzip it and find the `client.properties` file. Copy this file into the root directory.

## Deploying the Lambda

* Create an IAM Role for Lambda
  1. Go to the IAM Console: https://console.aws.amazon.com/iam/
  2. Create a Role:
    * Trusted entity type: AWS service
    * Use case: Lambda
    * Next

3. Attach policies:
* For basic Lambda execution:
* `AWSLambdaBasicExecutionRole` (writes logs to CloudWatch)

4. Name your role `credit-check-lambda-role` and create it.

* Using the AWS CLI, login to AWS

```bash
aws ecr get-login-password | docker login \
  --username AWS \
  --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com
```

* Create a repository

```bash
aws ecr create-repository --repository-name credit-check-lambda
```

* Build the Docker image

```bash
docker build --provenance=false --platform linux/amd64 --no-cache -t credit-check-lambda . 
```

* Tag and push the image

```bash
docker tag credit-check-lambda:latest <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/credit-check-lambda:latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.u<AWS_REGION>.amazonaws.com/credit-check-lambda:latest
```

* Create the Lambda function

```bash
aws lambda create-function \
  --function-name credit-check-lambda \
  --package-type Image \
  --code ImageUri=<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com credit-check-lambda:latest \
  --role arn:aws:iam::<AWS_ACCOUNT_ID>:role/credit-check-lambda-role
```

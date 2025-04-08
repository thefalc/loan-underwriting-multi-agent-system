import base64
from credit_and_fraud_check import lambda_handler  # Update with the actual file path

def test_locally():
    payload_value = {
      "application_id": "APP-200259",
      "customer_email": "forest.nikolaus@hotmail.com",
      "borrower_name": "Sam Hirthe",
      "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
      "income": 1015416,
      "payslips": "s3://riverbank-payslip-bucket/01JR1174FDRZPJ3F3699MCBKJG",
      "loan_amount": 368610,
      "property_address": "136 Wiegand Garden",
      "property_state": "North Dakota",
      "property_value": 491481,
      "employment_status": "Full-employed",
      "credit_score": 564,
      "credit_utilization": 60.9,
      "debt_to_income_ratio": 0,
      "open_credit_accounts": 4,
      "recent_defaults": 0,
      "payment_history": {
        "array": [
          {
            "transaction_id": "TX-3000351",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 249,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-08-09T05:00:56.601+00:00"
          },
          {
            "transaction_id": "TX-3001046",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 463,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-11-02T20:52:47.003+00:00"
          },
          {
            "transaction_id": "TX-3001112",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 245,
            "status": "failed",
            "failure_reason": "insufficient_funds",
            "payment_date": "2024-05-10T03:32:44.100+00:00"
          },
          {
            "transaction_id": "TX-3001604",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 119,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2025-01-21T05:07:26.908+00:00"
          },
          {
            "transaction_id": "TX-3002803",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 450,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-04-23T06:28:45.256+00:00"
          },
          {
            "transaction_id": "TX-3003010",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 364,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-06-04T09:36:24.741+00:00"
          },
          {
            "transaction_id": "TX-3003678",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 442,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2025-03-25T09:18:01.919+00:00"
          },
          {
            "transaction_id": "TX-3004436",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 140,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-08-31T08:13:35.909+00:00"
          },
          {
            "transaction_id": "TX-3005302",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 219,
            "status": "failed",
            "failure_reason": "insufficient_funds",
            "payment_date": "2024-07-19T21:23:03.465+00:00"
          },
          {
            "transaction_id": "TX-3005475",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 174,
            "status": "failed",
            "failure_reason": "insufficient_funds",
            "payment_date": "2024-12-14T16:43:12.480+00:00"
          },
          {
            "transaction_id": "TX-3005728",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 125,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-05-30T07:17:45.092+00:00"
          },
          {
            "transaction_id": "TX-3007139",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 106,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-07-18T18:36:03.522+00:00"
          },
          {
            "transaction_id": "TX-3007518",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 358,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2025-03-17T06:45:04.044+00:00"
          },
          {
            "transaction_id": "TX-3008127",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 469,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2025-03-07T20:21:24.979+00:00"
          },
          {
            "transaction_id": "TX-3008270",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 210,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2025-01-10T20:03:14.479+00:00"
          },
          {
            "transaction_id": "TX-3008933",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 217,
            "status": "failed",
            "failure_reason": "insufficient_funds",
            "payment_date": "2024-12-05T03:57:43.437+00:00"
          },
          {
            "transaction_id": "TX-3009028",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 113,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2025-02-07T20:34:48.684+00:00"
          },
          {
            "transaction_id": "TX-3009110",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 457,
            "status": "successful",
            "failure_reason": "N/A",
            "payment_date": "2024-08-17T21:51:06.321+00:00"
          },
          {
            "transaction_id": "TX-3009258",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 177,
            "status": "failed",
            "failure_reason": "insufficient_funds",
            "payment_date": "2024-07-24T02:46:55.742+00:00"
          },
          {
            "transaction_id": "TX-3009925",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 392,
            "status": "failed",
            "failure_reason": "insufficient_funds",
            "payment_date": "2024-08-22T18:08:05.268+00:00"
          },
          {
            "transaction_id": "TX-3000497",
            "applicant_id": "01JR1174FDRZPJ3F3699MCBKJG",
            "method": "auto-debit",
            "amount": 304,
            "status": "failed",
            "failure_reason": "insufficient_funds",
            "payment_date": "2025-04-04T23:47:04.816+00:00"
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

    result = lambda_handler(fake_event, None)
    print(result)

if __name__ == "__main__":
    test_locally()

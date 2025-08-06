import json
import pytest
import requests
from conftest import base_url

from logging import getLogger
logger = getLogger(__name__)

test_data = (
    "C12345",
)

@pytest.mark.api
@pytest.mark.parametrize("customer_id", test_data)
def test_get_customers_transactions(base_url, mock_transactions_response, customer_id):
    valid_transaction_types = {"deposit", "withdrawal", "transfer"}
    validation_matrix = []
    customer_endpoint = f"{base_url}/{customer_id}/transactions"
    logger.info(f"Testing endpoint: {customer_endpoint}")
    response = requests.get(customer_endpoint)
    try:
        logger.info(f"Response json: {response.json()}")
    except json.decoder.JSONDecodeError:
        logger.error("Response is not a valid JSON!")
        logger.error(f"Response text: {response.text}")

    logger.info(f"Response status code: {response.status_code}")
    validation_matrix.append(response.status_code == 200)
    customer_id_in_response = response.json().get('customer_id')
    logger.info(f"Customer ID in response is: {customer_id_in_response}")
    validation_matrix.append(customer_id_in_response == customer_id)
    transactions_list = response.json().get('transactions', [])
    logger.info("Transactions list retrieved:")
    logger.info(transactions_list)
    validation_matrix.append(len(transactions_list) > 0)
    transactions_validation_list = []
    for transaction in transactions_list:
        validation_matrix_for_transaction = []
        logger.info(f"Validating transaction: {transaction}")
        amount = transaction.get('amount', None)
        validation_matrix_for_transaction.append(isinstance(amount, float))
        currency = transaction.get('currency', None)
        validation_matrix_for_transaction.append(currency == "EUR")
        transaction_type = transaction.get('type', None)
        validation_matrix_for_transaction.append(transaction_type in valid_transaction_types)
        transactions_validation_list.append(validation_matrix_for_transaction)

    assert all(validation_matrix) and all(
        all(transactions_valid) for transactions_valid in transactions_validation_list
    ), "Validation failed"
    logger.info("All validations passed successfully.")
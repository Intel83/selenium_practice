import pytest
import requests_mock
from logging import config, getLogger
from transaction_tools import (
    transaction_id_generator,
    transaction_amount_generator,
    transaction_type_generator
)

# Configure logging
config.fileConfig('./logging.conf', disable_existing_loggers=False)
logger = getLogger(__name__)

# API-related fixtures
@pytest.fixture(scope="session")
def base_url():
    """
    Provides the base URL for the API tests.
    """
    base_url = "https://api.fakebank.com/customers"
    logger.info(f"Using base URL: {base_url}")
    yield base_url

@pytest.fixture()
def mock_transactions_response(base_url):
    """
    Mocks the response for transactions API endpoint.
    """
    tid_generator = transaction_id_generator()
    with requests_mock.Mocker() as m:
        customer_id = "C12345"
        endpoint = f"{base_url}/{customer_id}/transactions"
        transactions = [
            {
                "id": next(tid_generator),
                "amount": transaction_amount_generator(),
                "currency": "EUR",
                "type": transaction_type_generator()
            } for _ in range(5)
        ]
        m.get(endpoint, json={"customer_id": customer_id, "transactions": transactions}, status_code=200)
        logger.info(f"Mocked response for {endpoint}")
        yield m

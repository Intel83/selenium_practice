import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver_grid_herokuapp
from logging import getLogger
logger = getLogger(__name__)

test_data = (
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("invalid_user", "wrong_password", "Your username is invalid!"),
    ("invalid_user", "wrong_password", "Your username is invalid!"),
    ("invalid_user", "wrong_password", "Your username is invalid!"),
    ("invalid_user", "wrong_password", "Your username is invalid!"),
    ("invalid_user", "wrong_password", "Your username is invalid!")
)
@pytest.mark.login
@pytest.mark.parametrize("username, password, expected_message", test_data)
def test_credentials(driver_grid_herokuapp, username, password, expected_message):
    """
    Tests the login functionality with valid credentials.
    """
    # Enter valid credentials
    logger.info(f"Testing with username: {username} and password: {password}")
    driver_grid_herokuapp.find_element(By.ID, "username").send_keys(username)
    driver_grid_herokuapp.find_element(By.ID, "password").send_keys(password)

    # Submit the form
    logger.info("Submitting the login form.")
    driver_grid_herokuapp.find_element(By.XPATH, "//button[contains(@class, 'radius')]").click()

    # Wait for flash message
    logger.info("Waiting for the flash message to appear.")
    WebDriverWait(driver_grid_herokuapp, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash"))
    )

    # Assert success
    logger.info(f"Checking the flash message for expected content: {expected_message}.")
    message_shown = driver_grid_herokuapp.find_element(By.CLASS_NAME, "flash").text.strip()
    assert expected_message in message_shown, "Unexpected behavior or message not found."

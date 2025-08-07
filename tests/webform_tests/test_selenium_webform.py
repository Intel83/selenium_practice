import pytest
from selenium.webdriver.support.select import Select

from conftest import driver_selenium_webform

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logging import getLogger
logger = getLogger(__name__)

test_data = [
    ("Marcin", "This is a test message.", "2025-07-31", "One", "Form submitted"),
    ("Test User", "Other message.", "2025-07-31", "Two", "Form submitted")
]
@pytest.mark.parametrize(["name", "message", "date", "select_option", "expected_message"], test_data)
def test_webform_submission(driver_selenium_webform, name, message, date, select_option, expected_message):
    """
    Tests the web form submission functionality.
    """
    # Step 1 - Fill out the form
    logger.info(f"Filling out the web form with provided data: "
                f"Name={name}, Message={message}, Date={date}, Select Option={select_option}.")
    driver_selenium_webform.find_element(By.NAME, "my-text").send_keys(name)
    driver_selenium_webform.find_element(By.NAME, "my-textarea").send_keys(message)
    driver_selenium_webform.find_element(By.NAME, "my-date").send_keys(date)
    Select(driver_selenium_webform.find_element(By.NAME, "my-select")).select_by_visible_text(select_option)
    # Step 2 - submit form
    logger.info("Submitting the web form.")
    driver_selenium_webform.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
    WebDriverWait(driver_selenium_webform, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "display-6"))
    )
    # Step 3 - Assert success message
    logger.info(f"Checking for success message: {expected_message}.")
    # Find the success message element and verify its content
    success_message = driver_selenium_webform.find_element(By.CLASS_NAME, "display-6").text
    assert expected_message in success_message, "Form submission failed or message not found."
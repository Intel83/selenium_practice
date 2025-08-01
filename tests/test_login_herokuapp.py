from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver_herokuapp

def test_valid_login(driver_herokuapp):
    """
    Tests the login functionality with valid credentials.
    """
    # Enter valid credentials
    driver_herokuapp.find_element(By.ID, "username").send_keys("tomsmith")
    driver_herokuapp.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Submit the form
    driver_herokuapp.find_element(By.XPATH, "//button[contains(@class, 'radius')]").click()

    # Wait for flash message
    WebDriverWait(driver_herokuapp, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash"))
    )

    # Assert success
    success_message = driver_herokuapp.find_element(By.CLASS_NAME, "flash").text
    assert "You logged into a secure area!" in success_message, "Login failed or message not found."

def test_invalid_login(driver_herokuapp):
    """
    Tests the login functionality with invalid credentials.
    """
    # Enter invalid credentials
    driver_herokuapp.find_element(By.ID, "username").send_keys("invalid_user")
    driver_herokuapp.find_element(By.ID, "password").send_keys("wrong_password")

    # Submit the form
    driver_herokuapp.find_element(By.CLASS_NAME, "radius").click()

    # Wait for flash message
    WebDriverWait(driver_herokuapp, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash"))
    )

    # Assert failure
    failure_message = driver_herokuapp.find_element(By.CLASS_NAME, "flash").text
    assert "Your username is invalid!" in failure_message, "Login succeeded with invalid credentials."

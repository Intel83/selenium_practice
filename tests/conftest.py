import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# driver-related fixtures
@pytest.fixture(scope="function")
def driver():
    """
    Sets up the Chrome WebDriver with the necessary configurations.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()
    yield driver
    driver.quit()
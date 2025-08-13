import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from logging import config, getLogger

# Configure logging
config.fileConfig('./logging.conf', disable_existing_loggers=False)
logger = getLogger(__name__)

# driver for remote grid - herokuapp
@pytest.fixture(scope="session")
def driver_grid_herokuapp():
    """
    Sets up the Chrome WebDriver for remote grid testing on HerokuApp.
    """
    logger.info("Setting up Chrome WebDriver for remote grid HerokuApp login test.")
    # Initialize the Chrome WebDriver for remote grid
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for CI/CD environments
    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

# driver for remote grid - selenium webform
@pytest.fixture(scope="session")
def driver_grid_selenium_webform():
    """
    Sets up the Chrome WebDriver for remote grid testing on Selenium WebForm.
    """
    logger.info("Setting up Chrome WebDriver for remote grid Selenium WebForm test.")
    # Initialize the Chrome WebDriver for remote grid
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for CI/CD environments
    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    yield driver
    driver.quit()

# # driver-related fixtures
# @pytest.fixture(scope="function")
# def driver_herokuapp():
#     """
#     Sets up the Chrome WebDriver with the necessary configurations.
#     """
#     logger.info("Setting up Chrome WebDriver for HerokuApp login test.")
#     # Initialize the Chrome WebDriver
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://the-internet.herokuapp.com/login")
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# @pytest.fixture(scope="function")
# def driver_selenium_webform():
#     """
#     Sets up the Chrome WebDriver for the Selenium WebForm test.
#     """
#     logger.info("Setting up Chrome WebDriver for Selenium WebForm test.")
#     # Initialize the Chrome WebDriver
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#     driver.maximize_window()
#     yield driver
#     driver.quit()
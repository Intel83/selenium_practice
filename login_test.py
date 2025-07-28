from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_valid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    # Enter valid credentials
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Submit the form
    driver.find_element(By.CLASS_NAME, "radius").click()

    # Wait for flash message
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash"))
    )

    # Assert success
    success_message = driver.find_element(By.CLASS_NAME, "flash").text
    assert "You logged into a secure area!" in success_message, "Login failed or message not found."

    driver.quit()

if __name__ == "__main__":
    test_valid_login()

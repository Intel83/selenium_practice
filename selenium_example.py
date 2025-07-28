from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup Chrome
options = Options()
options.add_argument("--headless")  # remove if you want the browser visible
service = Service()
driver = webdriver.Chrome(service=service, options=options)

try:
    # 1. Go to the website
    driver.get("https://example.com")
    assert "Example" in driver.title

    # 2. Click on the link
    link = driver.find_element(By.XPATH, "//a[contains(text(),'More information')]")
    link.click()

    # 3. Verify redirection
    assert "iana.org" in driver.current_url
    print("✅ Test passed.")
except Exception as e:
    print(f"❌ Test failed: {e}")
finally:
    driver.quit()

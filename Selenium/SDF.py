from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver (You can change to your WebDriver path if needed)
driver = webdriver.Chrome(options=options)

try:
    print("Test Execution Started")

    # Open the MGIT website
    driver.get("https://www.mgit.ac.in")

    # Wait for the page to load (optional, just to ensure the page loads completely)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Wait for 10 seconds to simulate checking the website
    time.sleep(10)

    # Print success message
    print("Test Execution Completed Successfully!")

finally:
    # Close the browser session
    driver.quit()

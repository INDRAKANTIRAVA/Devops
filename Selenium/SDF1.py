from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

print("Test Execution Started")

# Configure Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")  # Disable GPU to avoid rendering issues
options.add_argument("--no-sandbox")  # Required for some environments
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")

try:
    # Initialize the WebDriver (Remote setup for Selenium Grid)
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    # Maximize the browser window
    driver.maximize_window()

    # Navigate to Google
    driver.get("https://www.google.com/")
    print("Navigated to Google.")

    # Wait for the search bar to become visible and perform a search
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()  # Submit the search query
    print("Search executed successfully!")

    # Wait for the search results to load and click on the first result
    first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
    )
    first_result.click()
    print("Clicked on the first search result!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the browser is closed properly
    driver.quit()
    print("Test Execution Completed Successfully!")

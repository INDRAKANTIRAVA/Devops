import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def setup_webdriver():
    """Set up and initialize the Edge WebDriver."""
    options = webdriver.EdgeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')
    # Uncomment below for headless mode
    # options.add_argument('--headless')

    driver_path = EdgeChromiumDriverManager().install()
    service = Service(driver_path)  # Use Service for specifying the driver path
    logger.info("Initializing WebDriver...")
    return webdriver.Edge(service=service, options=options)

def fill_registration_form(driver):
    """Fill the registration form and submit."""
    url = "file:///Users/indrakantirava/Devops/Selenium/Untitled.html"  # Use local file path instead of the server URL
    logger.info(f"Navigating to the form at {url}...")
    driver.get(url)

    try:
        # Wait for the form to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))
        logger.info("Form loaded successfully.")

        # Fill out the form fields
        logger.info("Filling out the form...")
        driver.find_element(By.ID, "firstName").send_keys("Indra Kanti Rava")
        time.sleep(2)
        driver.find_element(By.ID, "lastName").send_keys("Vadde")
        time.sleep(2)
        driver.find_element(By.ID, "email").send_keys("vaddeindrakantirava@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID, "phone").send_keys("8978296445")
        time.sleep(2)

        # Submit the form
        logger.info("Submitting the form...")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Wait for and verify the success message
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "successMessage")))
        confirmation_message = driver.find_element(By.ID, "successMessage").text
        assert "Thank you for registering!" in confirmation_message, "Unexpected confirmation message!"
        logger.info("Test Passed: Confirmation message verified.")
    except Exception as e:
        logger.error(f"Test Failed: {e}")
        raise
    finally:
        time.sleep(2)  # Optional pause before closing

def main():
    """Main function to execute the test."""
    logger.info("Test Execution Started")
    driver = None

    try:
        logger.info("Initializing WebDriver...")
        driver = setup_webdriver()
        logger.info("WebDriver initialized successfully.")

        # Execute the form fill and submission
        fill_registration_form(driver)
    except Exception as e:
        logger.error(f"An error occurred during test execution: {e}")
    finally:
        if driver:
            try:
                logger.info("Closing the browser...")
                driver.quit()
                logger.info("Browser closed successfully.")
            except Exception as e:
                logger.error(f"Error while closing the browser: {e}")

    logger.info("Test Execution Completed Successfully!")

if __name__ == "__main__":
    main()

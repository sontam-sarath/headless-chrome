import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--no-sandbox')  # Avoid sandboxing issues
chrome_options.add_argument('--disable-dev-shm-usage')  # Prevent shared memory errors
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
chrome_options.binary_location = "/usr/bin/google-chrome"  # Ensure this matches the output of 'which google-chrome'

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a webpage
driver.get("https://www.google.com")
print("Title is:", driver.title)

# Close WebDriver
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import base64

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
chrome_options.add_argument('--no-sandbox')  # Avoid sandboxing issues
# Avoid shared memory issues
# chrome_options.add_argument('--disable-dev-shm-usage')

# Start WebDriver using the Service class
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL to the page you want to save as PDF
url = 'https://sontam-sarath.github.io/portfolio/'

# Open the page in the headless browser
driver.get(url)

# Wait for the page to fully load (adjust if needed)
# time.sleep(5)

# Use Chrome DevTools Protocol to save the page as a PDF
file_path = "C:/Users/ssontam/Desktop/ssontam/headless-chrome/ss.pdf"
print_options = {
    "paperWidth": 8.5,
    "paperHeight": 11,
    "marginTop": 0.5,
    "marginBottom": 0.5,
    "marginLeft": 0.5,
    "marginRight": 0.5,
    "printBackground": True
}

# Trigger PDF saving
result = driver.execute_cdp_cmd("Page.printToPDF", print_options)

# Write the PDF data to a file
with open(file_path, "wb") as f:
    f.write(base64.b64decode(result['data']))

# Close the driver
driver.quit()

print("PDF saved successfully at:", file_path)

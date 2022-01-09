from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add option to prevent the window from automatically closing after code is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Site for testing clicks
driver.get("http://the-internet.herokuapp.com/")
# Wait until the element loads instead of just sleep(time) to save time
driver.implicitly_wait(10)

# Click on the option to try out Dynamic loading content
dynamicLoading_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Dynamic Loading')]")
dynamicLoading_element.click()

driver.implicitly_wait(10)

# Try out example 2
dynamicLoading_element_Example2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Example 2: Element rendered after the fact')]")
dynamicLoading_element_Example2.click()

driver.implicitly_wait(10)

# Find and click the Start button to initiate the loading bar
dynamicLoading_element_start_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Start')]")
dynamicLoading_element_start_btn.click()

# Setup explicit_wait to check when value has finished loading

WebDriverWait(driver, 30).until(
    # We check for the 'finish' element to show up which confirms the load has finished
    EC.presence_of_element_located((By.ID, 'finish'))
)

# If we got 'Process finished with exit code 0' that means the Wait worked properly
# and found the 'Hello World' element that shows up after the loading ends

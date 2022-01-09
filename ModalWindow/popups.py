import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Add option to prevent the window from automatically closing after code is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Site for testing clicks
driver.get("http://the-internet.herokuapp.com/")
# Wait until the element loads instead of just sleep(time) to save time
driver.implicitly_wait(10)

# Click on the option to try out how to handle entry ad's
dynamicLoading_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Entry Ad')]")
dynamicLoading_element.click()

# Wait for popup to start since it's always on a based timer
print('wait started')
time.sleep(2)
print('wait ended')

# We are using a try/catch block in case our pop up does not load
# If we call this block and the element is not found our script will crash
try:
    modal_window = driver.find_element(By.CLASS_NAME, 'modal-title')
    close_popup_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Close')]")
    print(close_popup_btn)
    close_popup_btn.click()
except:
    print('Popup not found , finishing script')

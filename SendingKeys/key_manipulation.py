from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Add option to prevent the window from automatically closing after code is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Site for testing key input sending
driver.get("http://the-internet.herokuapp.com")
# Wait until the element loads instead of just sleep(time) to save time
driver.implicitly_wait(10)

input_box_element_link = driver.find_element(By.XPATH, "//*[contains(text(), 'Form Authentication')]")
input_box_element_link.click()

driver.implicitly_wait(10)

input_box_element_username = driver.find_element(By.ID, 'username')
input_box_element_password = driver.find_element(By.ID, 'password')
input_box_element_login_btn = driver.find_element(By.XPATH, "//*[contains(text(), ' Login')]")

input_box_element_username.send_keys('tomsmith')
input_box_element_password.send_keys('SuperSecretPassword!')
driver.implicitly_wait(10)
input_box_element_login_btn.click()
# Wait 5 seconds to see that we successfully logged in
time.sleep(5)

# Click logout btn
input_box_element_logout_btn = driver.find_element(By.XPATH, "//*[contains(text(), ' Logout')]")
input_box_element_logout_btn.click()



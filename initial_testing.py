import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



# Add option to prevent the window from automatically closing after code is executed
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Site for testing clicks
driver.get("http://the-internet.herokuapp.com/")
# Wait until the element loads
driver.implicitly_wait(10)
element_new = driver.find_element(By.XPATH, "//*[contains(text(), 'File Download')]")

element_new.click()
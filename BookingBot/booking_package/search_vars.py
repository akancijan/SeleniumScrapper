from selenium.webdriver.chrome.options import Options

# Replace this path with your location where Chrome drivers are saved
driver_path = r'C:\Selenium_drivers\chromedriver.exe'

# Landing page for our bot
BASE_URL = 'https://www.booking.com'

# Add option to prevent the window from automatically closing after code is executed
chrome_options = Options()
# Swap value to get the following:
#   True = Browser stays open after code executes
#   False = Browser closes after code executes
auto_close_browser = True
chrome_options.add_experimental_option("detach", auto_close_browser)



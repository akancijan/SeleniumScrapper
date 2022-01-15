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

# Present values on booking site
# ( NOTE : I listed only the short versions of names for those currencies
# EUR,HRK,GBP,AUD,CAD,ARS,,AZN,BHD,BRL,BGN,XOF,CLP,CNY,COP,CZK,DKK,EGP
# FJD,GEL,HKD,HUF,INR,IDR,ILS,JPY,JOD,KZT,KRW,KWD,MYR,MXN,MDL,NAD,TWD,NZD,NOK
# OMR,PLN,QAR,RON,RUB,SAR,SGD,ZAR,SEK,CHF,THB,TRY,AED,UAH
wanted_currency = 'EUR'

# Travel destination
wanted_travel_destination = 'Pula'

# Check in date
# NOTE : format is yyyy-mm-dd
wanted_check_in_date = '2022-01-26'
wanted_check_out_date = '2022-02-07'

# Number of people
wanted_number_of_adults = 4

# If you select any children, you need to fill in their ages
# in the age_of_children list
# example : 2 children of ages 15 and 10
## wanted_number_of_children = 2
## age_of_children = [15,10]
wanted_number_of_children = 3
age_of_children = [15, 10, 18]

# Number of rooms
wanted_number_of_rooms = 3




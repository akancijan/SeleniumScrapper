import os
from BookingBot.booking_package import search_vars as consts
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=consts.driver_path):
        teardown = False
        super(Booking, self).__init__(executable_path=driver_path, options=consts.chrome_options)
        # All searches will wait aprox 15 seconds
        self.implicitly_wait(15)
        self.maximize_window()
    # Navigate to booking.com
    def land_first_page(self):
        self.get(consts.BASE_URL)

    # Swap displayed currencies
    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency = self.find_element(
            By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency.click()
    # Find location
    def select_travel_destination(self, travel_destination):
        search_field = self.find_element(
            By.ID,
            'ss'
        )
        search_field.clear()
        search_field.send_keys(travel_destination)
        # Click the first item in dropdown list for our search parameter
        first_result = self.find_element(
            By.CSS_SELECTOR,
            'li[data-i="0"]'
        )
        first_result.click()

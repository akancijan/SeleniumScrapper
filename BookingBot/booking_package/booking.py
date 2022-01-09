import os
from BookingBot.booking_package import search_vars as consts
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=consts.driver_path):
        teardown = False
        super(Booking, self).__init__(executable_path=driver_path, options=consts.chrome_options)

    def land_first_page(self):
        self.get(consts.BASE_URL)

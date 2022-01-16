import os
from BookingBot.booking_package import search_vars as consts
from BookingBot.booking_package.booking_filtration import BookingFiltration

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

    def select_travel_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{check_out_date}"]'
        )

        check_out_element.click()

    def set_age_of_children(self, children_guests):
        children_ages = []
        for i in range(children_guests):
            age_input = input(f'Enter age for child nr. {i+1} ')
            children_ages.append(age_input)
        print(children_ages)
        return children_ages

    def select_number_of_people(self, adult_guests, children_guests, number_of_rooms):
        toggle_adults_element = self.find_element(
            By.ID,
            'xp__guests__toggle'
        )
        toggle_adults_element.click()

        # ------------- VALUES for Adults/Guests/Rooms --------------
        # Get element that displays number of adults for search
        current_adults_value_element = self.find_element(
            By.ID,
            'group_adults'
        )
        # Get element that displays number of children for search
        current_children_value_element = self.find_element(
            By.ID,
            'group_children'
        )

        # Get element that displays number of rooms for search
        current_room_value_element = self.find_element(
            By.ID,
            'no_rooms'
        )
        #------------- INCREASE / DECREASE Buttons --------------
        # Grab the increase and decrease buttons for adults
        decrease_adults_value_element = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Decrease number of Adults"]'
        )
        increase_adults_value_element = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Increase number of Adults"]'
        )

        # Grab the increase and decrease buttons for children
        decrease_children_value_element = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Decrease number of Children"]'
        )
        increase_children_value_element = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Increase number of Children"]'
        )

        # Grab the increase and decrease buttons for rooms
        decrease_room_value_element = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Decrease number of Rooms"]'
        )
        increase_room_value_element = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Increase number of Rooms"]'
        )

        submit_button_element = self.find_element(
            By.CLASS_NAME,
            'sb-searchbox__button '
        )


        # Grab selector for dropdown list of children ages
        '''
            TO BE DONE
        '''

        # Setup our wanted numbers until we get the desired number of
        # Adults - > Children -> Rooms
        check_adults, check_children, check_ages, check_rooms = False, False, False, False

        #ages_of_children = self.set_age_of_children(children_guests)

        while True:
            # Return current number of adults
            adults_number = current_adults_value_element.get_attribute('value')
            children_number = current_children_value_element.get_attribute('value')
            rooms_number = current_room_value_element.get_attribute('value')
            # Check if value of adults has been set to the right amount
            if int(adults_number) == adult_guests:
                check_adults = True
            elif int(adults_number) > adult_guests:
                decrease_adults_value_element.click()
            else:
                increase_adults_value_element.click()

            # Set the values for children
            if int(children_number) == children_guests:
                check_children = True
            elif int(children_number) > children_guests:
                decrease_children_value_element.click()
            else:
                increase_children_value_element.click()
            # If a single or more children are select add their ages
            # else we just ignore this block
            if children_guests != 0 and check_children == True:
                for i in range(len(consts.age_of_children)):
                    print(f'Age of child nr. {i+1} is {consts.age_of_children[i]}')
                    ### Add click for their ages

            if int(rooms_number) == number_of_rooms:
                check_rooms = True
            elif int(rooms_number) > number_of_rooms:
                decrease_room_value_element.click()
            else:
                increase_room_value_element.click()

            if check_adults == True and check_children == True and check_rooms == True:
                break


        # After values have been set click search button
        submit_button_element.click()

    def apply_filter_options(self):
        filtration = BookingFiltration(driver=self)

        filtration.filter_by_star_value(consts.wanted_star_rating)
        filtration.filter_by_lowest_price_first()
        filtration.report_selected_results()

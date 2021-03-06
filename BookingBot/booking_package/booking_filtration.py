# Class with instance methods for filtartion options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from BookingBot.booking_package.booking_report import BookingReport
from time import sleep
from selenium.webdriver.common.keys import Keys


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def filter_by_star_value(self, star_values):
        # For click to work the box needs to be visible
        # We use this command to scroll down on the page
        # If you need to scroll more experiment with scrollTo values
        self.driver.execute_script("window.scrollTo(0, 1000);")

        for star_value in star_values:
            star_filtration_selection_element = self.driver.find_element(
                By.CSS_SELECTOR,
                f'div[data-filters-item="class:class={star_value}"]'
            )
            star_filtration_selection_element.click()

    def filter_by_lowest_price_first(self):
        sort_by_lowest_element = self.driver.find_element(
            By.CSS_SELECTOR,
            'li[data-id="price"]'
        )
        sleep(3)
        sort_by_lowest_element.click()

    def report_selected_results(self):
        sleep(3)
        result_boxes = self.driver.find_element(
            By.ID,
            'search_results_table'
        )
        report = BookingReport(result_boxes)
        report.pull_titles()
        report.pull_price()
        report.pull_rating()

        report.print_out_gathered_data()

        report.generate_report()

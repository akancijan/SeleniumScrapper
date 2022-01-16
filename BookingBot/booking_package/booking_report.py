# File contains methods to gather data from our searches
# And format them to an output
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.returned_search_boxes = self.unbox_deal_boxes()

    def unbox_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            By.CSS_SELECTOR,
            'div[data-testid="property-card"]'
        )

    def pull_titles(self):

        for search_result in self.returned_search_boxes:
            property_name = search_result.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="title"]'
            ).text
            print(property_name)

    def pull_price(self):
        for search_result in self.returned_search_boxes:
            total_price = search_result.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="price-and-discounted-price"]'
            ).text
            print(total_price)

    def pull_rating(self):
        for search_result in self.returned_search_boxes:
            try:
                rating = search_result.find_element(
                    By.CSS_SELECTOR,
                    'div[data-testid="review-score"]'
                ).text
                print(rating)
            except NoSuchElementException as e:
                print(f'error {e}')
                print('No reviews found')

# File contains methods to gather data from our searches
# And format them to an output
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from BookingBot.booking_package import search_vars as consts

import xlsxwriter
import re
from datetime import date


class BookingReport:
    # Arrays that will hold scrapped data before we write it to excel
    property_names = []
    prices = []
    ratings = []
    # Using datetime package to add day of execution to excel file name
    today = date.today()
    formatted_day = today.strftime("%d-%m-%y")



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
            self.property_names.append(property_name)

    def pull_price(self):
        for search_result in self.returned_search_boxes:
            total_price = search_result.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="price-and-discounted-price"]'
            ).text
            print(total_price)
            self.prices.append(total_price)

    def pull_rating(self):
        for search_result in self.returned_search_boxes:
            try:
                rating = search_result.find_element(
                    By.CSS_SELECTOR,
                    'div[data-testid="review-score"]'
                ).text
                print(rating)
                self.ratings.append(rating)
            except NoSuchElementException as e:
                print(f'error {e}')
                print('No reviews found')
                self.ratings.append('No ratings found')

    def generate_report(self):
        workbook = xlsxwriter.Workbook(f'{consts.report_path}/report_{self.formatted_day}.xlsx')
        worksheet = workbook.add_worksheet(f'Prices for {consts.wanted_travel_destination}')

        worksheet.write('A1', 'Property name')
        worksheet.write('B1', 'Rating value')
        worksheet.write('C1', 'Rating description')
        worksheet.write('D1', 'Nr. of reviews')
        worksheet.write('E1', f'Original price ({consts.wanted_currency})')
        worksheet.write('F1', 'Price if discounted')

        row_index = 2
        for i in range(len(self.property_names)):
            worksheet.write(f'A{row_index}', self.property_names[i])

            # Grab parts of the review and split them into seperate values
            review_info = self.ratings[i].split('\n')
            # If a review was present add the separate values to corresponding columns
            if len(review_info) > 1:
                worksheet.write(f'B{row_index}', review_info[0])
                worksheet.write(f'C{row_index}', review_info[1])
                worksheet.write(f'D{row_index}', review_info[2])
            # if no value was present add N/A
            else:
                worksheet.write(f'B{row_index}', 'N/A')
                worksheet.write(f'C{row_index}', 'N/A')
                worksheet.write(f'D{row_index}', 'N/A')

            price_editing = self.prices[i].replace(',', '')
            price_editing = re.sub('[^0-9]', ' ', price_editing)
            split_prices = price_editing.split(' ')
            prices_separated = list(filter(None, split_prices))
            if len(prices_separated) > 1:
                worksheet.write(f'E{row_index}', prices_separated[0])
                worksheet.write(f'F{row_index}', prices_separated[1])
            else:
                worksheet.write(f'E{row_index}', prices_separated[0])
                worksheet.write(f'F{row_index}', 'No discount provided')

            row_index += 1

        workbook.close()

    def print_out_gathered_data(self):
        print(self.property_names)
        print(self.ratings)
        print(self.prices)



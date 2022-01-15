from BookingBot.booking_package.booking import Booking
from BookingBot.booking_package import search_vars as consts
# Initialize our Booking class
booking_obj = Booking()

booking_obj.land_first_page()

# If you want to change the currency type , swap it in the search_vars.py file
booking_obj.change_currency(currency=consts.wanted_currency)

# Select travel destination
booking_obj.select_travel_destination(travel_destination=consts.wanted_travel_destination)


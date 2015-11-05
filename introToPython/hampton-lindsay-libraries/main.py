__author__ = 'lindsayhampton'

# Import the Library file so as to access its files
import library

class MainHandler:
    # I know you said to always use underscores in naming conventions, but the assignment clearly states to use this name.

    def __init__(self):
        # Declare the attributes with classes from library.py
        self.library(library.Library)
        self.printer(library.Printer)

        # Declare variable based on User's Input
        # int() is required to be capable of calculating inputted information
        fahrenheit = int(raw_input("Enter a temperature in Fahrenheit:"))
        celsius = self.library.temp_conversion(fahrenheit)
        mph = int(raw_input("Enter a speed in Miles Per Hour(MPH):"))
        kph = self.library.kilo_conversion(mph)
        feet = int(raw_input("Enter a length in Feet:"))
        cm = self.library.length_conversion(feet)
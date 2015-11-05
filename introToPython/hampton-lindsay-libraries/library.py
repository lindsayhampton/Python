__author__ = 'lindsayhampton'

class Printer():
    # Constructor Function
    def __init__(self):

        # Declare variables for future use
        self.fahrenheit = 0
        self.celsius = 0

        self.mph = 0
        self.kph = 0

        # Function to display information in log
        def display_info(self):
            # Requires str() because variables used are integers
            print str(self.fahrenheit) + " degrees fahrenheit is the equivalent of " + str(self.celsius) + " degrees celsius."
            print str(self.mph) + " miles per hour is the equivalent of " + str(self.kph) + " kilometers per hour."


class Library():
    # Constructor Function
    def __init__(self):
        pass

    #Function to convert Fahrenheit to Celsius
    def temp_conversion(self, f):
        celsius = (f-32) / 1.8
        return celsius

    def kilo_conversion(self, k):
        kilo = k * 1.60934
        return kilo

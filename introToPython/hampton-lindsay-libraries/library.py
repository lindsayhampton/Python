__author__ = 'lindsayhampton'

class Printer():
    # Constructor Function
    def __init__(self):

        # Declare variables for future use
        self.fahrenheit = 0
        self.celsius = 0

        self.mph = 0
        self.kph = 0

        self.feet = 0
        self.cm = 0

        # Function to display information in log
        def display_info(self):
            print "The only countries in the world that do not rely on the metric system are Liberia, Myanmar, and the United States."
            print "Here's a handy guide of some conversions for you!"
            print " "
            # Requires str() because variables used are integers
            print str(self.fahrenheit) + " degrees fahrenheit is the equivalent of " + str(self.celsius) + " degrees celsius."
            print str(self.mph) + " miles per hour is the equivalent of " + str(self.kph) + " kilometers per hour."
            print str(self.feet) + " feet is the equivalent of " + str(self.cm) + " centimeters."


class Library():
    # Constructor Function
    def __init__(self):
        pass

    #Function to convert Fahrenheit to Celsius
    def temp_conversion(self, f):
        celsius = (f-32) / 1.8
        return celsius

    #Function to convert Miles Per Hour to Kilometers Per Hour
    def kilo_conversion(self, k):
        kilo = k * 1.60934
        return kilo

    #Function to convert Feet to Centimeters
    def length_conversion(self, l):
        centi = l * 2.54
        return centi
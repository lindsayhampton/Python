__author__ = 'lindsayhampton'

class Printer():
    # Constructor Function
    def __init__(self):

        # Declare variables for future use
        self.fahrenheit = 0
        self.celsius = 0

        self.mph = 0
        self.kph = 0

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

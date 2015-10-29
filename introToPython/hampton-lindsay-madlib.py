# MadLib Lab 1
# By Lindsay Hampton

# Inputs for our Mad Lib:
story = raw_input("Would you like to hear a story? ")
year = raw_input("Enter a year from the past: ")
number = raw_input("Enter a number: ")
funnyWord = raw_input("Enter a funny word: ")
animal1 = raw_input("Enter an animal: ")
instrument = raw_input("Enter an instrument: ")
animal2 = raw_input("Enter a new animal: ")
verb1 = raw_input("Enter a verb: ")
object1 = raw_input("Enter an object: ")
adjective = raw_input("Enter an adjective: ")
animal3 = raw_input("Enter a new animal: ")
verb2 = raw_input("Enter a new verb: ")
object2 = raw_input("Enter a new object: ")
object3 = raw_input("Enter a new object: ")

# Created arrays to organize similar information
answers = [year, number, funnyWord, animal1, instrument, animal2, verb1, object1, adjective, animal3, verb2, object2, object3]
animal = [animal1, animal2, animal3]
object = [object1, object2, object3]
verb = [verb1, verb2]

# Function to combine funny words as a string
def diddle(funnyWord):
    diddle = str(funnyWord + " " + funnyWord)
    print diddle

# Stringify the year
age = str(2015 - int(year))


# Conditional Loop w/ Logical Operator
if story == "yes" or "Yes" or "YES":
    print madLib
else:
    print "Okay, maybe next time."

# Loop to show user the words they chose
for a in answers:
    print "You chose the word " + a + "."
# MadLib Lab 1
# By Lindsay Hampton

# Inputs for our Mad Lib:
year = raw_input("Enter a year from the past: ")
number = raw_input("Enter a number: ")
funnyWord = raw_input("Enter a funny word: ")
animal1 = raw_input("Enter an animal: ")
instrument = raw_input("Enter an instrument: ")
animal2 = raw_input("Enter a new animal: ")
verb1 = raw_input("Enter a past-tense verb: ")
object1 = raw_input("Enter an object: ")
adjective = raw_input("Enter an adjective: ")
animal3 = raw_input("Enter a new animal: ")
verb2 = raw_input("Enter a new past-tense verb: ")
object2 = raw_input("Enter a new object: ")
object3 = raw_input("Enter a new object: ")

# Created arrays to organize similar information
answers = [year, number, funnyWord, animal1, instrument, animal2, verb1, object1, adjective, animal3, verb2, object2, object3]
animal = [animal1, animal2, animal3]
object = [object1, object2, object3]
verb = [verb1, verb2]

# Function to combine funny words
def diddle(funny):
    diddle = funny + " " + funny
    print diddle

# Stringify the year
age = str(2015 - int(year))

# The Mad Lib Itself

madLib1 = "When I was "+age+" years old, I had "+number+" favorite nursery rhymes. But I've got to say, my favorite " \
        "nursery rhyme of all time was called Hey "+ funnyWord + " " + funnyWord +" and it went something like this: "
madLib2 = "Hey "+ funnyWord + " " + funnyWord + ", the " + animal[0] + " and the " + instrument + ","
madLib3 = "The "+ animal[1] + ""


# Conditional Loop w/ Logical Operator
if int(year) > 2015:
    print "Sorry, your year was invalid."
else:
     print madLib1

# Loop to show user the words they chose
print "These are the answers that you chose: "
for a in answers:
    print "You chose the word " + a + "."
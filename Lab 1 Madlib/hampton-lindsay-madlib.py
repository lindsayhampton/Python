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
verb = {"one": verb1, "two": verb2}

# Function to combine funny words
def diddle(funny):
    diddle = funny + " " + funny
    return diddle

# Stringify the year
age = str(2015 - int(year))

# Print line space to break up logs
print " "

# The Mad Lib Itself

madLib1 = "When I was "+age+" years old, I had "+number+" favorite nursery rhymes. But I've got to say, my favorite " \
        "nursery rhyme of all time was called Hey '"+ diddle(funnyWord) +"' and it went something like this: "
madLib2 = "'Hey "+ diddle(funnyWord) + ", the " + animal[0] + " and the " + instrument + ","
madLib3 = "The "+ animal[1] + " " + verb["one"] + " over the " + object[0] + "."
madLib4 = "The "+ adjective + " " + animal[2] + " " + verb["two"] + " to see such sport,"
madLib5 = "And the "+ object[1] + " ran away with the " + object[2] +"!'"



# Conditional Loop w/ Logical Operator
if int(year) > 2015:
    print "Sorry, your year was invalid."
else:
     print madLib1
     print madLib2
     print madLib3
     print madLib4
     print madLib5

# Loop to show user the words they chose
# Print line space to break up logs
print " "
print "These are the answers that you chose: "
for a in answers:
    print "You chose the word " + a + "."
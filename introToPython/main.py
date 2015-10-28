#variabled
first_name = "Lindsay"
last_name = "Hampton"
year_born = 1999

#print /first_name + " " + last_name

# Casting
# str() converts x to string
# int() converts c to integer
# print "You are " + str(2015 - year_born) + " years old!"

# Conditional Statements
# use tabs instead of {}, also colon
# if year_born < 1994:
#     print "they are old enough to embibe"
# elif year_born < 1996:
#     print "they are too drink, but not too young to serve in a war"
# else:
#     print "too young for booze or war"

# LOOPS
# no ++ or -- in Python... instead use += or -=
# for NUM in range (START, STOP, INC AMOUNT):

students = ["Lindsay", "Clay", "James", "John", "Sergej", "Sean", "Vance", "Selena"]
students.append("Karl")

# for i in range(0,9):
#     #print "hello there!"
#     #print "happy birthday!"
#     print students[i]+" you are going to do awesome in this class!"

# for s in students:
#     print s + ", you're going to do awesome in this class!"
#
# i = 0
# while i<9:
#     print students[i]
#     i+=1

# DICTIONARY
# dictionary_name = {'key': value, 'key':value}
student_movie = {'Selena':'American History X', 'James':'The Patriot', 'Clay':'Bourne Identity'}
# print student_movie['Selena']

# FUNCTIONS
def area(x,y):
    a = x * y
    print a

# area(20, 60) # function invocation

# USER INPUT
name = raw_input("Please enter your name: ")
print name + ", it is very nice to meet you!"

age = raw_input("Please enter your age: ")
print str(2015 - int(age)) + " was the year you were born."

# Logical Operators
# && = and
# || = or
# != = not
parents_with_them = true
if year_born < 1994 :
    print "they can drink"
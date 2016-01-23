people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."
    
if people <= cats and people <= dogs:
    print "Pets outnumber people"


""" Study Drills
    1. What do you think the if does to the code under it?
       The if makes the execution of the code conditional on the statement 
       after the if
    2. Why does the code under the if need to be indented four spaces?
       It needs to be indented because Python is a white-space sensitive 
       language. This helps to know that the code is conditional on the if
       statement.
       A colon at the end of a line is how you tell Python you are going to 
       create a new "block" of code, and then indenting four spaces tells 
       Python what lines of code are in that block. This is exactly the same
       thing you did when you made functions in the first half of the book.
    3. What happens if it isn't indented?
       There is an error message: IndentationError. Otherwise the compiler 
       might think that the code was not part of the if statement and always 
       execute it
    4. Can you put other boolean expressions from Exercise 27 in the 
       if-statement? Try it.
       See line 30,31
    5. What happens if you change the initial values for people, cats, and 
       dogs?
       You can print different statements based on the relative values of the
       variables.
"""

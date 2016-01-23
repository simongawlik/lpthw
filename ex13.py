# import the sys module
from sys import argv
'''
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

""" Study Drill 1
    Try giving fewer than three arguments to your script. See that error you 
    get? See if you can explain it.
    
jharvard@appliance (~/learn_python_the_hard_way): python ex13.py apple orange
Traceback (most recent call last):
  File "ex13.py", line 4, in <module>
    script, first, second, third = argv
ValueError: need more than 3 values to unpack

    argv is trying to unpack the arguments in the command line into the 
    variables but it is given fewer than 3 arguments. The last variables will
    therefore not be assigned and would produce undefined behavior
    
    
    Study Drill 2
    Write a script that has fewer arguments and one that has more. Make sure 
    you give the unpacked variables good names.
    """

script, first, second = argv

print "The script is called:", script
print "The first argument to the command line was:", first
print "The second argument to the command line was:", second


script, first, second, third, fourth = argv

print "The script is called:", script
print "The first argument to the command line was:", first
print "The second argument to the command line was:", second
print "The third argument to the command line was:", third
print "The fourth argument to the command line was:", fourth

""" Study Drill 3
    Combine raw_input with argv to make a script that gets more input from a 
    user
    """
'''
script, arg = argv

print "You are executing program:", script
print "You gave the following argument:", arg
age = raw_input("How old are you? ")
print "%r" % age


""" Study Drill 4
    Remember that modules give you features. Modules. Modules. Remember this 
    because we'll need it later.
    """

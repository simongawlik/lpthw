print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
    
""" Study Drills 1
    Go online and find out what Python's raw_input does:
    
    If the prompt argument is present, it is written to standard output without
    a trailing newline. The function then reads a line from input, converts it 
    to string (stripping a trailing newline), and returns that. When EOF is 
    read, EOFError is raised.
    
    
    Study Drills 2
    Can you find other ways to use it? Try some of the samples you find.
    """
# print_odds.py
# Prints some odd numbers, use raw_input to delay execution (to debug)

for x in xrange(1, 20, 2):
    print x

raw_input("Press <enter> to continue")

""" Study Drills 3 
    Write another "form" like this to ask some other questions.
    """
print "What school did you attend or are you attending?",
school = raw_input()
print "What color are your eyes?",
eyecolor = raw_input()
print "Where do you live?",
city = raw_input()

print "So, you're at/ went to %r, have %r eyes, and live in %r." % (
    school, eyecolor, city)
    
""" Study Drills 4
    Related to escape sequences, try to find out why the last line has '6\'2"'
    with that \' sequence. See how the single-quote needs to be escaped because
    otherwise it would end the string?
    """

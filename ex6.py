# substituting number into string and assigning string to variable x
x = "There are %d types of people." % 10
# assigning string to variable binary
binary = "binary"
# assigning string to variable do_not
do_not = "don't"
# substituting the two string variables into a string and assigning string to y
y = "Those who know %s and those who %s." % (binary, do_not)

# print variable x
print x
# print variable y
print y

# substitute x with quotation marks into another string and printing it
print "I said: %r." % x
# substitute y without quotation marks into another string and printing it
print "I also said: %s." % y

# assigning boolean value False to variable hilarious
hilarious = False
# assigning a partial string to a variable. the variable requires another input
joke_evaluation = "Isn't that joke so funny?! %r"

# calling variable and adding parameter
print joke_evaluation % hilarious

# assigning string to w
w = "This is the left side of..."
# assigning string to e
e = "a string with a right side."

# printing e concatenated onto w
print w + e


# Study Drills 2
# 1) line 8 (twice)
# 2) line 16
# 3) line 18
# 4) 

# Study Drills 3
# Yes, the other variables do not store strings and the python string formatting
# options print their types.

# Study Drills 4
# Adding two strings works the same as string concatenation

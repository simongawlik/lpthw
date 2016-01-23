def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
    
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"


""" Study Drills
    1. If you aren't really sure what return does, try writing a few of your
       own functions and have them return some values. You can return anything 
       that you can put to the right of an =.
    2. At the end of the script is a puzzle. I'm taking the return value of one
       function and using is as the argument of another function. I'm doing 
       this chain so that I'm kind of creating a formula using the functions.
       It looks really weird, but if you run the script you can see the 
       results. What you should do is try to figure out the normal formula that
       would recreate this same set of operations.
       
       # 35 + 74 - 50 / 2 * 180
       
    3. Once you have the formula worked out for the puzzle, get in there and 
       see what happens when you modify the parts of the functions. Try to 
       change it on purpose to make another value.
    4. Do the inverse. Write a simple formula and use the function in the same 
       way to calculate it.
       
       # 35 * 10 + 12 / 4 * 15
"""

what2 = add(multiply(35, 10), divide(multiply(12, 15), 4))

print "what2 is: ", what2

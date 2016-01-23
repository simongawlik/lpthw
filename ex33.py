
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1
    print "Numbers now: ", numbers
    print "At the botton i is %d" % i


print "The numbers: "

for num in numbers:
    print num

""" Study Drills
    1. Convert this while-loop to a function that you can call, and replace 6
       in the test (i < 6) with a variable.
    2. Use this function to rewrite the script to try different numbers
    
n = 6
numbers = []

def whilelessthan(number):
    i = 0
    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


whilelessthan(n)
print "The numbers: "
for num in numbers:
    print num
    
    3. Add another variable to the function arguments that you can pass in that
       lets you change the + 1 on line 8 so you can change how much it
       increments by.
    4. Rewrite the script again to use this function to see what effect that 
       has.
       
n = 7
incr = 1
numbers = []

def whilelessthan(number, inc):
    i = 0
    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


whilelessthan(n, incr)
print "The numbers: "
for num in numbers:
       
    5. Write it to use for-loops and range. Do yo need the inrementor in the
       middle anymore? What happens if you do not get rid of it?
       If you don't get rid of it it will increment by twice the value of incr

n = 7
incr = 1
numbers = []

def forlessthan(number, inc):
    for i in range (0, number, inc):
        print "At the top i is %d" % i
        numbers.append(i)
        
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


forlessthan(n, incr)
print "The numbers: "
for num in numbers:
    print num
"""

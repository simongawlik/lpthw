people = 30
cars = 40
trucks = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

if cars > people or trucks < cars:
    print "My head hurts... I'll ride a bike"

""" Study Drills
    1. Try to guess what elif and else are doing.
       elif defines another if statement whose conditional is evaluated after 
       the first if-statement and every elif statement that came before it. If
       any of those statements are successfully evaluated the elif statement 
       will not be.
       else is the catch-all statement whose code is executed if none of the if
       or elif statements before it were executed.
    2. Change numbers of cars, people, and trucks and then trace through each
       if-statement to see what will be printed.
    3. Try some more complex boolean expressions like cars > people or trucks <
       cars.
    4. Above each line write an English description of what the line does.
    
"""

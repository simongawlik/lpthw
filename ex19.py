# creates a function that takes two inputs
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints a string that includes the first input
    print "You have %d cheeses!" % cheese_count
    # prints a string that includes the second input
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # prints string
    print "Man that's enough for a party!"
    # prints string and newline
    print "Get a blanket.\n"


# prints string
print "We can just give the function numbers directly:"
# calls function with two integers
cheese_and_crackers(20, 30)


# prints string
print "OR, we can use variables from our script:"
# stores integer in variable
amount_of_cheese = 10
# stores second integer in another variable
amount_of_crackers = 50

# calls function with two variables that hold integers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# prints string
print "We can even do math inside too:"
# calls function with two expressions (additions of two integers)
cheese_and_crackers(10 + 20, 5 + 6)

# prints string
print "And we can combine the two, variables and math:"
# calls function with 2 expressions (addition of integer and varholding int)
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


""" Study Drills
    1. Go back through the script and type a comment above each line explaining
       in English what it does.
    2. Start at the bottom and read each line backward, saying all the 
       important characters.
    3. Write at least one more function of your own design, and run it 10 
       different ways
       
"""
def pots_and_pans(pots_count, pans_count):
    print "There are %d pots and %d pans" % (pots_count, pans_count)
    
number_of_pots = 4
number_of_pans = 5
number_of_pans_string = '3'

pots_and_pans(2, 2)
pots_and_pans(2 + 2, 5)
pots_and_pans(3, 5 ** 2) 
pots_and_pans(number_of_pots, 23)
pots_and_pans(number_of_pots, number_of_pans)
pots_and_pans(number_of_pots + 1, 22)
pots_and_pans(45, number_of_pans)
pots_and_pans(53, number_of_pans ** 2)
pots_and_pans(number_of_pots, int(number_of_pans_string))
pots_and_pans(number_of_pots * number_of_pans / number_of_pans, number_of_pans)

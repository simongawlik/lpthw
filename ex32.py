the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have the use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = range(0,6)#[]

'''
# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
'''
# now we can print the out too
for i in elements:
    print "Element was: %d" % i
    
""" Study Drills
    1. Take a look at how you used range. Look up the range function to 
       understand it.
       Counts from 0 to 5 in 1-sized steps.
    2. Could you have avoided that for-loop entirely on line 22 and just
       assigned range(0,6) directly to elements?
       YES!!
    3. Find the Python documentation on lists and read about them. What other
       operations can you do to lists besides append?
       len([list])              : length
       [list1] + [list2]        : concatenation
       [list] * n               : repetition
       elt in [list]            : membership
       for x in [list]:         : iteration
       cmp(list1,list2)         : compares elements of both lists
       max(list)                : returns item from list with max value
       list(seq)                : converts tuple into list
       list.count(obj)          : count of how many times obj occurs in list
       list.extend(seq)
       list.sort([func])        : sorts objects of list, use compare func if 
                                    given
       etc.
"""

import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')


# print out some cities
print '-' * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city


"""
When to Use Dictionaries or Lists
1. You have to retrieve things based on some identifier, like names,
   addresses, or anything that can be a key.
2. You don't need things to be in order. Dictionaries do not normally
   have any notion of order, so you have to use a list for that.
3. You are going to be adding and removing elements and their keys.

Study Drills
1.  Do this same kind of mapping with cities and states/regions in your
    country or some other country.
    
    TODO
    
2.  Find the Python documentation for dictionaries and try to do even
    more things to them.
    
    TODO

3.  Find out what you can't do with dictionaries. A big one is that
    they do not have order, so try playing with that.
    
    TODO
    
4.  Read about Python's assert feature and then take the hashmap code
    and add assertions for each of the tests I've done instead of 
    print. For example, you can assert that the first get operation 
    returns "New York" instead of just printing that out.

    TODO
    
5.  Did you notice that the list function listed the items I added in a
    different order than they were added? This is an example of how
    dictionaries don't maintain order, and if you analyze the code 
    you'll understand why.
    
    TODO
    
6.  Create a dump function that is like list but which dumps the full
    contents of every bucket so you can debug it.
    
    TODO
    
7.  Make sure you know what the hash function does in that code. It's a
    special function that converts strings to a consistent integer. 
    Find the documentation for it online. Read about what a "hash 
    function" is in programming.
    
    TODO 
"""
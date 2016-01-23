ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", 
              "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]     # whoa! fancy
print stuff.pop()
print ' '.join(stuff)       # what? cool!
print '#'.join(stuff[3:5])  # super stellar!


"""
Study Drills

1.  Take each function that is called, and go through the steps for
    function calls to translate them to what Python does. For example,
    more_stuff.pop() is pop(more_stuff).
    
    stuff.append(next_one) is append(stuff, next_one)
    stuff.pop() is pop(stuff)
    ' '.join(stuff) is join(' ', stuff)
    '#'.join(stuff[3:5]) is join('#', stuff[3:5])
    
2.  Translate these two ways to view the function calls in English. For
    example, more_stuff.pop() reads as, "Call pop on more_stuff." 
    Meanwhile, pop(more_stuff) means, "Call pop with argument 
    more_stuff." Understand how they are really the same thing.
    
    Call append on stuff with argument next_one
    Call append with arguments stuff and next_one
    Call pop on stuff
    Call pop with argument stuff
    Call join on ' ' with argument stuff
    Call join with arguments ' ' and stuff
    Call join on '#' with argument stuff[3:5]
    Call join with arguments '#' and stuff[3:5]
    
3.  Go read about "object-oriented programming" online. Confused? I was
    too. Do not worry. You will learn enough to be dangerous, and you 
    can slowly learn more later.
    
    
    
4.  Read up on what a "class" is in Python. Do not read about how other
    languages use the word "class." That will only mess you up.
    
    https://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
    
5.  Do not worry if you do not have any idea what I'm talking about.
    Programmers like to feel smart so they invented object-oriented
    programming, named it OOP, and then used it way too much. If you 
    think that's hard, you should try to use "functional programming."
    
    
      
6.  Find 10 examples of things in the real world that would fit in a 
    list. Try writing some scripts to work with them.

"""    
list0 = ["apples", "oranges", "bananas"]
list1 = [1, 2, 3, 4]
list2 = ["hello", "salut", "aloha", "hallo", "ahoi"]
list3 = ["bag", "box", "container"]
list4 = ["Iron Man", "Captain America", "Hulk", "Thor"]
list5 = ["Hacker News", "Slashdot", "io9"]
list6 = ["wood", "drywall", "cement", "pipes"]
list7 = ["requirements", "design", "develop", "test", "deploy"]
list8 = ["Game of Thrones", "Silicon Valley", "John Oliver"]
list9 = ["TOS", "TNG", "DS9", "Voyager"]

list0.extend(["grapes", "pineapple"])
print list0

# countdown
list1.insert(0, 0)
list1.append(5)
print list1

list2.sort(reverse=True)
print list2

list5.pop()
print list5
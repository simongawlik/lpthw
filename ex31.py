print "You enter a dark room with three doors.  Do you go through door #1 or door # 2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear
        
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understading revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

# added as part of study drill
elif door == "3":
    print "A clown on a unicycle. What do you do?"
    print "1. Tell a joke to the clown."
    print "2. Tackle the clown off the unicycle."
    print "3. Call your mom. She must be worried by now."
    
    clown = raw_input("> ")
    
    if clown == "1":
        print "Your joke falls flat. The clown pulls a knife and stabs you.  Good job!"
    elif clown == "2":
        print "The clown was wearing a rigged vest. You both explode.  Good job!"
    elif clown == "3":
        print "You get no reception. You wake up from your nightmare."
    else:
        print "That doesn't work. The clown tickles you to death.  Good job!"
    
else:
    print "You stumble around and fall on a knife and die.  Good job!"

""" Study Drills
    1. Make new parts of the game and change what decisions people can make. 
       Expand the game out as much as you can before it gets ridiculous.
    2. Write a completely new game. Maybe you don't like this one, so make your
       own. This is your computer, do what you want.
"""

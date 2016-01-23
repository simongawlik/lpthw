from sys import exit

def gold_room():
    print "This room is full of gold.  How much to you take?"
    
    choice = raw_input("> ")
    try:
        how_much = int(choice)
    except ValueError:
        dead("Man, learn to type a number.")
    
    if how_much < 50 and how much > 0:
        print "Nice, you're not greedy, you win!"
        exit(0)
    elif how_much <= 0:
        print "What are you doing? This is not a bank!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Ctulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    choice = raw_input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    choice = raw_input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

""" Study Drills
    1. Draw a map of the game and how you flow through it.
    2. Fix all of your mistakes, including spelling mistakes.
    3. Write comments for the functions you do not understand.
    4. Add more to the game. What can you do to both simplify and expand it?
    5. The gold_room has weird way of getting you to type a number. What are
       all the bugs in this way of doing it? Can you make it better than what
       I've written? Look at how int() works for clues.
       In this way of doing it, we won't accept any number that doesn't contain
       a 1 or 0. If a string contains a 1 or 0, it thinks we actually typed a
       number but it might have just been something like "1asd0"
       
"""
    

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


"""
Study Drills

1.  Write some more songs using this and make sure you understand that
    you're passing a list of strings as the lyrics.
"""
amazing_grace = Song(["Amazing grace, how sweeet the sound",
                      "That saved a wretch like me",
                      "I once was blind but now I see"])
                      
turtles = Song(["Hey, jetzt kommen die Heroturtles",
                "Superstarke Heroturtles",
                "Immer auf der Lauer",
                "Und immer etwas schlauer"])

amazing_grace.sing_me_a_song()
turtles.sing_me_a_song()
"""    
2.  Put the lyrics in a separate variable, then pass that variable to 
    the class to use instead.
"""
prince_lyrics = [
    "Now, this is a story all about how",
    "My life got flipped turned upside down",
    "And I'd like to take a minute",
    "Just sit right there",
    "I'll tell you how I became the prince of a town called Bel Air"
]

prince = Song(prince_lyrics)
prince.sing_me_a_song()    
""" 
3.  See if you can hack on this and make it do more things. Don't worry
    if you have no idea how, just give it a try, see what happens. 
    Break it, trash it, trash it, you can't hurt it.
    
    TODO
    
4.  Search online for "object-oriented programming" and try to overflow
    your brain with what you read. Don't worry if it makes absolutely
    no sense to you. Half of that stuff makes no sense to me too.
    
    TODO
    
"""
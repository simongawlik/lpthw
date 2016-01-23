from sys import argv

script, user_name, password = argv
prompt = 'You say > '

print "You gave the password %s." % password

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

''' Study Drill 2
    Change the propmt variable to something else entirely.
    
    Also works for ints
    
    Study Drill 3
    Add another argument and use it in your script, the same way you did in the
    previous exercise with first, second = ARGV.
    
    Study Drill 4
    Make sure you understand how I combined a """ style multiline string with 
    the % format activator as the last print.
    '''

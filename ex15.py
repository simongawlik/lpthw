# this imports the sys module, and the argv feature in particular
from sys import argv

# this breaks the arguments from the command line into separate variables
script, filename = argv

# this tries to open a file with the given name in the current directory
txt = open(filename)

# this prints the filename
print "Here's your file %r:" % filename
# this reads the contents of the file and then prints them
print txt.read()
# closes file
txt.close()

print "Type the filename again:"
# this reads input after a prompt and saves it to a variable
file_again = raw_input("> ")

# this tries to open a file with the given name in the current directory
txt_again = open(file_again)

# this reads the contents of the file and then prints them
print txt_again.read()
# closes file
txt.close()

''' Study Drill 1
    Above each line, write out in English what that line does.
    
    Study Drill 2
    If you are not sure ask someone for help or search online. Many times 
    searching for "python THING" will find answers to what that THING does in 
    Python. Try searching for "python open."
    
    Study Drill 3
    I used the word "commands" here, but commands are also called "functions" 
    and "methods." You will learn about functions and methods later in the 
    book.
    
    Study Drill 4
    Get rid of lines 10-15 where you use raw_input and run the script again
    
    This just prints the text once and does not prompt the user to enter the 
    filename once more.
    
    Study Drill 5
    Use only raw_input and try the script that way. Why is one way of getting 
    the filename better than the other?
    
    This is better than just taking input through the command line. We can 
    remind the user what input we need from her instead of relying on her to
    remember in which order to provide the command line arguments.
    
    Study Drill 6
    Start python to start the Python shell, and use open from the prompt just 
    like in this program. Notice how you can open files and run read on them 
    from within python?
    
    txt = open("ex15_sample.txt")
    print txt.read()
    
    Study Drill 7
    Have your script also call close() on the txt and txt_again variables. It's
    important to close files when you are done with them.
    
    Close frees up system resources taken up by the open file
    '''

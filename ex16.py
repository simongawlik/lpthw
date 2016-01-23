from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# we open the file, creating it if it doesn't exist and truncating it to 0 
# bytes if it does. Then, on the next line, we truncate it to 0 bytes
target = open(filename, 'w')

print "Trunctating the file.  Goodbye!"
# truncating again at 0th byte. we don't need this.
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
""" these write commands were removed for just one write
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
target.write("%s\n%s\n%s\n" % (line1, line2, line3)) 

print "And finally, we close it."
target.close()

""" Study Drills
    2. Write a script similar to the last exercise that uses read and argv to 
       read the file you just created.
"""
target_again = open(filename)
print target_again.read()
target_again.close()
""" 3. There's too much repetition in this file. Use strings, formats, and 
       escapes to print out line1, line2, and line3 with just one 
       target.write() command instead of six.
    4. Find out why we had to pass a 'w' as an extra parameter to open. Hint:
       open tries to be sage by making you explicitly say you want to write a 
       file.
       The most commonly-used values of mode are 'r' for reading, 'w' for 
       writing (truncating the file if it already exists), and 'a' for 
       appending. Passing in a 'w' will immediately overwrite the file!
       
    5. If you open a file with 'w' mode, then do you really need the 
       target.truncate()? Read the documentation for Python's open function and
       see if that's true.
       No, see above.

"""

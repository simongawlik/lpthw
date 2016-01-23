from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)


""" Study Drills
    1. Write English comments for each line to understand what that line does.
    2. Each time print_a_line is run, you are passing a variable current_line.
       Write out what current_line is equal to on each function call, and trace
       how it becomes line_count in print_a_line.
       
       current_line is equal to 1, 2, and 3 in the three function calls. As it 
       gets passed to the function it is "renamed" to line_count.
       
    3. Find each place a function is used, and check its def to make sure that 
       you are giving it the right arguments.
       
       
       
    4. Research online what the seek function for file does. Try pydoc file and
       see if you can figure it out from there.
       
       seek(offset[, whence]) -> None.  Move to new file position.
 |      
 |    Argument offset is a byte count.  Optional argument whence defaults to
 |    0 (offset from start of file, offset should be >= 0); other values are 1
 |    (move relative to current position, positive or negative), and 2 (move
 |    relative to end of file, usually negative, although many platforms allow
 |    seeking beyond the end of a file).  If the file is opened in text mode,
 |    only offsets returned by tell() are legal.  Use of other offsets causes
 |    undefined behavior.
 |    Note that not all file objects are seekable.
       
    5. Research the shorthand notation += and rewrite the script to use += 
       instead.
"""

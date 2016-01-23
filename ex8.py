formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing,",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# Study Drill 2
# The last line of output uses both single-quotes and double-quotes for 
# individual pieces because the third string also contains a single-quote. If
# we used single-quotes for it, the program may not know when the string really
# ends.

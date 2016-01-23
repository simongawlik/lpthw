True and True                           # True
False and True                          # False
1 == 1 and 2 == 1                       # False
"test" == "test"                        # True
1 == 1 or 2 != 1                        # True
True and 1 == 1                         # False
False and 0 != 0                        # False
True or 1 == 1                          # True
"test" == "testing"                     # False
1 != 0 and 2 == 1                       # False
"test" != "testing"                     # True
"test" == 1                             # False
not (True and False)                    # True
not (1 == 1 and 0 != 1)                 # False
not (10 == 1 or 1000 == 1000)           # False
not (1 != 10 or 3 == 4)                 # False
not ("testing" == "testing" and "Zed" == "Coold Guy")           # True
1 == 1 and (not (3 == 4 or 3 == 3))                             # False
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))                # False
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))  # False


""" Study Drills
    1. There are a lot of operators in Python similar to != and ==. Try to find
       as many "equality operators" as you can. They should be like < or <=.
       >=   greater than or equal to
       >    greater than
       <=   less than or equal to
       <    less than
       <>   not equal to
       
    2. Write out the names of each of these equality operators. For example, I
       call != "not equal."
    3. Play with the Python by typing out new boolean operators, and before you
       press Enter try to shout out what it is. Do not think about it. Shout 
       the first thing that comes to mind. Write it down, then press Enter, and
       keep track of how many you get right and wrong.
       
       
    4. Throw away the piece of paper from 3 away so you do not accidentally try
       to use it later.
"""

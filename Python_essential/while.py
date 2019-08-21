#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5 

# The input() function allows user input
# Use the parameter to write a message before the input:

while pw != secret:
    count += 1
    if count > max_attempt: 
        # break will break out of the loop and skip the else clause(because condition is still true)
        # continue will shortcut the loop and go back up to the test
        break
    
    pw = input(f"{count} What's the secret word? ")
"""If the else statement is used with a while loop, the else statement is executed when the condition becomes false"""

else:
    auth = True

print("Authorized" if auth else "Game Over")
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
        break
    
    pw = input(f"{count} What's the secret word? ")
else:
    auth = True
"""
If the else statement is used with a while loop, 
the else statement is executed when the condition becomes false
"""
print("Authorized" if auth else "Game Over")
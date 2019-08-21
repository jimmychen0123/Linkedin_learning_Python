#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

checkAll = False

for pet in animals:

    if pet == 'dog': 
        continue
    if pet == 'velociraptor': 
        break
    print(pet)

# If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating all elemets in the list.

else:
    checkAll = True

print('All the animals are showed' if checkAll else 'Animal Missing!!')


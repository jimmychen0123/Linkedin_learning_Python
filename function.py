#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten(5 ,6.5)
    print('---------------------------')
    x = 8
    y = x 
    y = 3
    print(f'The id of x is {id(x)}')
    print(f'The id of y is {id(y)}')
    print()

    z =['list is mutable']
    q = z
    q[0] = 'when assigning a mutable variable, we are actually assigning a reference to the mutable'
    print(f'The id of z is {id(z)}')
    print(f'The id of q is {id(q)}')
    print(f'in main: z is {z}')
    print(f'in main: q is {q}')
    print()

    doggy(x)
    print(f'in main: x is {x}')
   

# Give the default argument and keep the argument with default value at the end of the list 

def kitten(a, b = 6, c = 7):
    print('Meow.')
    print(a, b, c)

# 
def doggy(a):
    # call by value : when passing a variable in a function, the function operates on a copy of the variable, so the value is passed, but not the object.
    # if 'a' was actually a copy of what was being passed to doggy function, we would expect a different id number.
    # An integer is not mutable, so it can not be changed. When assigning a new integer value to a variable, we are actually assigning an differnet object.
     
    print(f'1: The id of a is {id(a)}') 
    a = 8
    print('woof')
    print(f'In doggy function: a is {a}')
    print(f'2: The id of a is {id(a)}')

# __name__ is a special variable that return the name of the current module
# if this file had been included in another execution unit by the import statement, then this file will be running as module and variable will have the name of the module 

if __name__ == '__main__': main()

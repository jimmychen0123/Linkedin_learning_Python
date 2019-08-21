#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import Decimal 

block = """
-----------------------------------------------------
"""
x = 7 / 3
print('x is {}'.format(x))
print(type(x))
print(block)

#use double divide sign to have integer divison
y = 7 // 3
print('y is {}'.format(y))
print(type(x))


#use built-in format method for string
#positional argument, the order can be changed by putting index inside the curly bracket
#Also by having colon after the index, we can align the space or leading zero to the right or left to the argument
x = 'seven "{1:<05}" "{0:>019}"'.format(8, 9)
print('x is {}'.format(x))
print(type(x))
print(block)

#----------------------------------------------------
#formating string
a = 8
b = 9

y = f'seven {a} {b}'

print(y)
print(block)

#----------------------------------------------------
x = .1 +.1 +.1 - .3
print('x is {}'.format(x))
print(block)

#Never use floating number for money
a = Decimal('.10')
b = Decimal('.30')
c = a + a + a - b

print('c is {}'.format(c))
print(block)





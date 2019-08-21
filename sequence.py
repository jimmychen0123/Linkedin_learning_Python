#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# List is mutable
x = [ 1, 2, 3, 4, 5 ]
x[0] = 42
for i in x:
    print('i is {}'.format(i))

print()

# Tuple is immutable

y = (1, 2, 3, 4, 5)

for t in y:
    print('t is {}'.format(t))

print()

# class range is immutable 
"""
The advantage of the range type over a regular list or tuple is that a range object will always take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the start, stop and step values, calculating individual items and subranges as needed).

"""
z = list(range(5, 30, 5))

for r in z:
    print('r is {}'.format(r))

print()
# dictionary is a set of key : value pairs
d = {'one': 1, 'two': 2, 'three': 3}
d['three'] = 42 
for k, v in d.items():
    print('k: {}, v: {}'.format(k,v))
print()

# 
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)

print('x is {}'.format(x))
print(type(x))
print(type(x[1]))

# x and y are differnet object, thus differnet id
print(id(x))
print(id(y))

# the element of index 0 in both x and y are the same object, thus same id 
print(id(x[0]))
print(id(y[0]))

"""
The is keyword is used to test if two variables refer to the same object.

The test returns True if the two objects are the same object.

The test returns False if they are not the same object, even if the two objects are 100% equal.

Use the == operator to test if two variables are equal.

"""
if x is y:
    print('yep, same object')
else: 
    print('nope, differenct object')

if isinstance(x, tuple):
    print('It is a tuple')
elif isinstance(x, list):
    print('It is a list')
else:
    print('nope')




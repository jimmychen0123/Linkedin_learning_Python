#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 0x0a
y = 0x02
z = x & y


print(x)
print(y)
print(z)
# lowercase hexadecimal string prefixed with “0x”
# A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. 
# with leading zero and 2 or 8 character space, x for hexadecimal display, b for binary display
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

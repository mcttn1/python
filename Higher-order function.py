# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 21:06:37 2018

@author: huashuo
"""

print(abs(-10))

print(abs)

x=abs(-10)
print(x)

f=abs
print(f(-10))

# =============================================================================
# abs=10
# print(abs(-10))
# =============================================================================

def add(x, y, f):
    return f(x) + f(y)

print(add(-5,6,abs))
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 19:34:37 2018

@author: huashuo
"""

from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abs',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))


from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))

print(isinstance(iter([]),Iterator))
print(isinstance(iter('abc'),Iterator))


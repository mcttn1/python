# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:39:26 2018

@author: huashuo
"""
# #迭代
# =============================================================================
# #在Python中，迭代是通过for ... in来完成的
# #Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上
# #list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，
# #但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
# d={'a':1,'b':2,'c':3}
# for key in d:
#     print(key)
# #默认情况下，dict迭代的是key
# #如果要迭代value,可以用for value in d.values()
# for value in d.values():
#     print(value)
# #如果要同时迭代key和value，可以用for k, v in d.items()
# for k,v in d.items():
#     print(k,v)
# #字符串也是可迭代对象 
# for ch in 'asd':
#     print(ch)
# #只要作用于一个可迭代对象，for循环就可以正常运行    
# #那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断    
# from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance([1,2,3],Iterable))
# print(isinstance(123,Iterable))
# #如果要对list实现类似Java那样的下标循环怎么办？
# #Python内置的enumerate函数可以把一个list变成索引-元素对，
# #这样就可以在for循环中同时迭代索引和元素本身：
# for i,v in enumerate(['A','B','C']):
#     print(i,v)
# 
# =============================================================================


##练习
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L==[]:
        return(None,None)
    min1,max1=L[0],L[0]
    for num in L:
        if num<=min1:
            min1=num
        if num>=max1:
            max1=num
    return(min1,max1)
    
print(findMinAndMax([1,2,3,10]))












    
    
    











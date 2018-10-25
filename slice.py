# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:49:40 2018

@author: huashuo
"""
##切片
# =============================================================================
# #取一个list或tuple的部分元素
# #取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：
# L=['M','C','T','S','H','E']
# r=[]
# n=3
# for i in range(n):
#     r.append(L[i])
# 
# print(r)
# #对这种经常取指定索引范围的操作，用循环十分繁琐，
# #因此，Python提供了切片（Slice）操作符，能大大简化这种操作。 
# print(L[0:3])#从索引0开始取，直到索引3为止，但不包括索引3
# #如果第一个索引是0
# print(L[:3])
# print(L[-1])
# print(L[-2:])
# print(L[-2:-1]) 
# 
# #创建一个0-99的数列
# L=list(range(100))
# print(L)
# #可以通过切片轻松取出某一段数列。比如前10个数：
# print(L[0:10])
# print(L[-10:])
# #前11-20个数：
# print(L[10:20])
# #前10个数，每两个取一个：
# print(L[:10:2])
# #所有数，每5个取一个：
# print(L[::5])
# #只写[:]就可以原样复制一个list：
# print(L[:])
# #tuple也可以用切片操作，只是操作的结果仍是tuple：
# T=tuple(range(10))
# print(T)
# print(T[:3])
# #字符串也可以用切片操作，只是操作结果仍是字符串：
# S='asdjfkk'
# print(S[:3])
# print(S[::2])
# =============================================================================


##练习
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    l=len(s)
#    print(l)
    if s[0]==' 'and s[-1]==' ':
        print(s[1:l-1])
    elif s[0]==' 'and s[-1]!=' ':
        print(s[1:])
    elif s[0]!=' 'and s[-1]==' ':
        print(s[0:l-1])
    else:
        print(s)
        
s=' asdfghj ' 
trim(s)
s='hello '
trim(s)














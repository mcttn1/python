# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:45:47 2018

@author: huashuo
"""

def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','B','',None,'C',' '])))

s='  A '
print(s.strip())

def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
        
def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter() #初始序列
    while True:
        n=next(it) #返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it) #构造新序列
        
for n in primes():
    if n<1000:
        print(n)
    else:
        break
        


#练习
def is_palindrome(n):
    n=str(n)#转换为字符串
    return n==n[::-1]
print(list(filter(is_palindrome,range(1,1000))))

        



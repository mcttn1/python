# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:35:18 2018

@author: huashuo
"""

def f(x):
    return x*x

r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

L=[]
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)

#print(x*x for x in [1,2,3,4,5,6,7,8,9])

print(list(map(str,[1,2,3,4,5,6,7,8,9])))


from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7,9]))


def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))

def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

print(reduce(fn,map(char2num,'13579')))

#测试map的输出
for x in map(char2num,'13579'):
    print(x)


DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def char2num(s):
        return DIGITS[s]
    def fn(x,y):
        return x*10+y
    return reduce(fn,map(char2num,s))

print(str2int('3456'))



#练习
def normalize(name):
    return name.title()
print(list(map(normalize,['adam', 'LISA', 'barT'])))




def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)
print(prod([3,5,7,9]))  



def str2float(s):
    def fn(x,y):
        return x*10+y
    n=s.index('.')
    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1)+reduce(fn,s2)/10**len(s2)
print(str2float('123.456'))





















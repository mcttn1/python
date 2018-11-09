# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:33:04 2018

@author: huashuo
"""

L=[x*x for x in range(10)]
print(L)

G=(x*x for x in range(10))
print(G)

print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
#print(next(G))

for n in G:
    print(n)
    
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
print(fib(6))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o=odd()
print(next(o))
print(next(o))
print(next(o))

for n in fib(6):
    print(n)


g=fib(6)
while True:
    try:
        x=next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break


def Triangles(num):
    L,n=[1],0
    while n<num:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
        n=n+1
        
l=Triangles(10)
for n in l:
    print(n)












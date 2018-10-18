# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:40:11 2018

@author: huashuo
"""

# =============================================================================
# #如果一个函数在内部调用自身本身，这个函数就是递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# 
# print(fact(5))
# print(fact(100))
# #递归函数的优点是定义简单，逻辑清晰
# #使用递归函数需要注意防止栈溢出
# #fact(10000)#RecursionError: maximum recursion depth exceeded in comparison
# #解决递归调用栈溢出的方法是通过尾递归优化
# #尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# #这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
# #上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了
# #要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num==1:
#         return product
#     return fact_iter(num-1,num*product)
# 
# print(fact(1000))
# =============================================================================


# #练习

#汉诺塔的移动可以用递归函数非常简单地实现。
#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
#然后打印出把所有盘子从A借助B移动到C的方法，例如：

def move(n,a,b,c):
     if n==1:
          print('move',a, '-->',c)
          return
          
     move(n-1,a,c,b)
     move(1,a,b,c)
     move(n-1,b,a,c)

move(3, 'A', 'B', 'C')




















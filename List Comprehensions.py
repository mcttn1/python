# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 21:16:05 2018

@author: huashuo
"""

##列表生成式
# =============================================================================
# #Python内置的非常简单却强大的可以用来创建list的生成式
# #要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #可以用list(range(1, 11))
# print(list(range(1,11)))
# #如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环
# 
# L=[]
# for x in range(1,11):
#     L.append(x*x)
# print(L)
# #但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
# #写列表生成式时，把要生成的元素x * x放到前面，
# #后面跟for循环，就可以把list创建出来
# print([x*x for x in range(1,11)])
# 
# 
# #for循环后面还可以加上if判断，如筛选出仅偶数的平方：
# print([x*x for x in range(1,11) if x%2==0])
# 
# #使用两层循环，生成全排列:
# print([m+n for m in 'ABC' for n in 'XYZ'])
# 
# #运用列表生成式，可以写出非常简洁的代码
# #如：列出当前目录下的所有文件和目录名，可以通过一行代码实现：
# import os
# print([d for d in os.listdir('.')])# os.listdir可以列出文件和目录
# #for循环其实可以同时使用两个甚至多个变量，
# #比如dict的items()可以同时迭代key和value：
# #列表生成式也可以使用两个变量来生成list：
# d={'x':'A','y':'B','z':'C'}
# print([k+'='+v for k,v in d.items()])
# 
# #把一个list中所有的字符串变成小写：
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])
# 
# =============================================================================

##练习
#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
        

L2=[s.lower() for s in L1  if isinstance(s,str)==True]    


if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')














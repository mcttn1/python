# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:49:54 2018

@author: huashuo
"""

#条件判断
#计算机可以自己做条件判断
#比如，输入用户年龄，根据年龄打印不同的内容
age=3
if age>=18:
    print('your age is',age)
    print('you are an adult')
#也可以给if添加一个else语句
elif age>=6:#可以用elif做更细致的判断
    print('your age is',age)
    print('you are a teenager')
else:
    print('your age is',age)
    print('you are a teenager')

#if判断条件还可以简写,只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x=''
if x:
    print ('True')
  
    
# =============================================================================
# #有问题的条件判断
# birth=input('birth:')#用input()读取用户的输入，
# if birth<2000:      #会报错，input返回数据类型是str，str不能和int比较  
#     print('00前')
# else:
#     print('00后')
# =============================================================================
#改
# =============================================================================
# s=input('birth:')
# birth=int(s)
# if birth<2000:      
#     print('00前')
# else:
#     print('00后') 
# =============================================================================


#练习
# =============================================================================
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果
# =============================================================================
hight=1.75
weight=80.5
BMI=weight/(hight**2)
print(BMI)
if BMI<18.5:
    print('过轻')
elif BMI<25:
    print('正常')
elif BMI<28:
    print('过重')
elif BMI<32:
    print('肥胖')
else:
    print('严重肥胖')
    

















































    
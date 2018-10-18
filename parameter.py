# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:52:31 2018

@author: huashuo
"""

#Python的函数定义,除了正常定义的必选参数外，还可以使用默认参数、
#可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# #位置参数
# =============================================================================
# #我们先写一个计算x2的函数
# def power(x):
#     return x*x
# #参数x就是一个位置参数,当我们调用power函数时，必须传入有且仅有的一个参数x
# print(power(5))
# 
# #计算x4、x5……,可以把power(x)修改为power(x, n)，用来计算xn
# def power(x,n=2):#默认参数就排上用场了。由于我们经常计算x2，
#                  #所以，完全可以把第二个参数n的默认值设定为2
#     s=1
#     while n>0:
#         s=s*x
#         n=n-1
#     return s
# #可以计算任意数的n次方
#     
# print(power(2,10))
# #修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，
# #调用函数时，传入的两个值按照位置顺序依次赋给参数x和n
# 
# print(power(5))#TypeError: power() missing 1 required positional argument: 'n'
# #默认计算x的2次方，默认参数可以简化函数的调用
# =============================================================================

# #默认参数
# =============================================================================
# #使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
# #当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# #我们写个一年级小学生注册的函数，需要传入name和gender两个参数
# def enroll(name,gender):
#     print('name=',name)
#     print('gender=',gender)
# #调用enroll函数
# enroll('M','F')
# 
# #如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
# #我们可以把年龄和城市设为默认参数：
# def enroll(name,gender,age=7,city='SH'):
#     print('name=',name)
#     print('gender=',gender)
#     print('age=',age)
#     print('city=',city)
# enroll('M','F')
# 
# #大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数
# #只有与默认参数不符的学生才需要提供额外的信息：
# enroll('C','F',6)
# enroll('T','M',city='SZ')#没有输入age参数时，需要将city的参数名写出来
# =============================================================================

# =============================================================================
# def add_end(L=[]):
#     L.append('END')
#     return L
# 
# print(add_end([1,2,3]))#正常调用时，结果似乎不错
# print(add_end(['x','y','z']))
# print(add_end())#当你使用默认参数调用时，一开始结果也是对的
# print(add_end())#但是，再次调用add_end()时，结果就不对了：
# print(add_end())#返回['END', 'END', 'END']
# =============================================================================

# =============================================================================
# #函数似乎每次都“记住了”上次添加了'END'后的list
# #定义默认参数要牢记一点：默认参数必须指向不变对象！
# #要修改上面的例子，我们可以用None这个不变对象来实现：
# def add_end(L=None):
#     if L is None:
#         L=[]
#     L.append('END')
#     return L
# print(add_end())#返回['END']
# print(add_end())#无论调用多少次，都不会有问题：返回['END']
# =============================================================================

# #可变参数
# =============================================================================
# #给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……
# #要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，
# #我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
# def calc(numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum
# 
# print(calc([1,2,3]))
# print(calc((1,3,5,7)))
# #如果利用可变参数，调用函数的方式可以简化成这样：
# #把函数的参数改为可变参数：
# def calc(*numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum
# #在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# #但是，调用该函数时，可以传入任意个参数，包括0个参数：
# print(calc(1,2,3))
# print(calc(1,3,5,7))
# print(calc())
# #如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
# nums=[1,2,3]
# print(calc(nums[0],nums[1],nums[2]))
# 
# #这种写法当然是可行的，问题是太繁琐，
# #所以Python允许你在list或tuple前面加一个*号，
# #把list或tuple的元素变成可变参数传进去：
# print(calc(*nums))
# 
# =============================================================================

# #关键字参数
# =============================================================================
# #可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# #而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
# 
# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
#     
# print(person('M',30))
# print(person('C',25,city='SH'))
# print(person('T',23,gender='F',job='Engineer'))
# 
# #和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
# extra={'city':'Beijing','job':'Engineer'}
# 
# print(person('J',24,city=extra['city'],job=extra['job']))
# 
# #上面复杂的调用可以用简化的写法：
# print(person('J',24,**extra))
# #注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
# =============================================================================

# #命名关键字参数
# =============================================================================
# #对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# #至于到底传入了哪些，就需要在函数内部通过kw检查。
# #仍以person()函数为例，我们希望检查是否有city和job参数：
# 
# def person(name,age,**kw):
#     if 'city' in kw:
#         #有city参数
#         pass
#     if 'job' in kw:
#         #有job参数
#         pass
#     print('name:',name,'age:',age,'other:',kw)
# 
# #但是调用者仍可以传入不受限制的关键字参数：
# print(person('P',33,city='Beijing',zipcode=123456))
# 
# #如果要限制关键字参数的名字，就可以用命名关键字参数，
# #例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# def person(name,age,*,city,job):
#     print(name,age,city,job)
# #和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，
# #*后面的参数被视为命名关键字参数    
# 
# print(person('TT',18,city='SH',job='IT'))
# 
# #如果函数定义中已经有了一个可变参数，
# #后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# def person(name,age,*args,city,job):
#     print(name,age,city,job)
# #命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# #person('Jack',24,'Beijing','IT')#TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
# 
# #命名关键字参数可以有缺省值，从而简化调用：
# def person(name,age,*,city='Beijing',job):
#     print(name,age,city,job)
#     
# print(person('JACK',24,job='IT'))
# 
# #使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# #如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
# 
# def person(name,age,city,job):
#     #缺少*，city和job被视为位置参数
#     pass
# =============================================================================

# #参数组合
# =============================================================================
# #在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# #但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 
# def f1(a,b,c=0,*args,**kw):
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
#     
# def f2(a,b,c=0,*,d,**kw):
#      print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
#      
# print(f1(1,2))
# print(f1(1,2,c=3))
# print(f1(1,2,3,'a','b'))
# print(f1(1,2,3,'a','b',x=99))
# print(f1(1,2,3,'a','b',x=99,y=3))
# print(f2(1,2,d=99,ext=None))
# 
# #最神奇的是通过一个tuple和dict，你也可以调用上述函数：
# args=(1,2,3,4)
# kw={'d':99,'x':'#'}
# print(f1(*args,**kw))
# 
# args=(1,2,3)
# kw={'d':88,'x':'#'}
# print(f2(*args,**kw))
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
# =============================================================================

#练习
#以下函数允许计算两个数的乘积，请稍加改造，
#变成可接收一个或多个数并计算乘积：
def product(x, y):
    return x * y

def product(*numbers):
    multiply=1
    for n in numbers:
        multiply=multiply*n
    return multiply

nums=[3,4,5,6,7]
print(product(*nums))
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))










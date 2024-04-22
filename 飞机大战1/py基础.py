# python是面向对象的解释型高级编程程序
# python是强类型的动态脚本语言
# x="123456789"
# print(x[1:6:2])
# print(x,111)

# -*- coding UTF-8 -*-

# x = '123456'
# print(id(x))
#
# a,b,c = 'a','b','c'
# del b
# print(a,c)


# a=[1]
# b=['1']
# if a[0] == b[0]:
#     print(a[0],1,b[0])
# else:
#     print(a[0],0,b[0])

# for x in 'i am a man'.split(' '):
#     print(x)
# else:
#     print(0)
# 打开a.txt。如果没有者创建啊。txt并输入111，自动关闭文件
# with open('a.text','a') as g :
#     g.write('1111')
# a = [1,2,3,4,5,6,7]
# print(a[1:5])
# print(a[-4:-1])
# print(a[:1])
# while True:
#     print(3)
# else:
# 	print('在while正常跑完时执行,没有break')
# range(1,10)
# x = [x for x in range(1,10) if x%2 == 1]
# print(x)
# 列表推倒式
# 生成字符串
# print(['the %s' %d for d in range(1,10)])
# # 生成元组
# print([(x,y) for x in range(1,3) for y in range(1,3)])
# # 生成字典
# print({x:x**2 for x in range(1,10)})
# 删除列表中元素
# del x[:]
# 删除列表对象
# del x

# sort排序 翻转列表 reverse
# a=[1,3,2,4,5,6,7,8,9,10]
# a.sort()
# b = a[:]
# print(a)
# print(b)
# a.reverse()
# print(a)

# # 创建一个空集合
# my_set = set()
#
# # 创建一个带有初始值的集合
# my_set_with_values = {1, 2, 3, 4, 5}

# # 创建集合
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
#
# # 计算交集
# intersection = set1 & set2
# print("交集:", intersection)
#
# # 计算并集
# union = set1 | set2
# print("并集:", union)
#
# # 计算差集
# difference = set1 - set2
# print("差集:", difference)
# # update用法
# set1.update('23456')  # 将set1更新为包含set1和set2的所有元素
# print(set1)

# 创建一个空字典
# my_dict = {}
#
# # 创建包含初始键值对的字典
from segno.cli import func

# my_dict = {'apple': 2, 'banana': 3, 'orange': 5}
# get方法
# print(my_dict.get('apple'))  # 输出 2
# print(my_dict.get('apples','33') ) # 输出 33

#in检索字典中是否存在键
# if 'apple'in my_dict :
#     print(my_dict['apple'])
# else:
#     print('没有这个键')

#
# # 通过键访问对应的值
# print(my_dict['apple'])  # 输出 2
# # 添加新的键-值对
# my_dict['pear'] = 4
#
# # 修改已有键的值
# my_dict['banana'] = 6
# # 使用del语句删除键-值对
# del my_dict['apple']
#
# print(my_dict)
# # 使用pop()方法删除键-值对，并返回被删除的值
# popped_value = my_dict.pop('orange')
# print(popped_value)
# # 获取所有键
# keys = my_dict.keys()
# print(keys)
# # 获取所有值
# values = my_dict.values()
# print(values)
# # 获取所有键值对
# items = my_dict.items()
# print(items)

# 元组
# my_tuple = (1, 2, 3,2,2,2,2)
# num = tuple(set(my_tuple))
# print(my_tuple.count(2))
# print(my_tuple.index(3))
# print(num)
#函数
# def my_func(x,y):
#     return x+y
# print(my_func(2,3))
# globals()函数返回全局作用域的变量和函数的字典
# global_var = 10
# global_var = globals()
# print(global_var)
# #函数转成元组输出
# def test(*kwargs):
#     return kwargs
# print(test(11,[2,2,3],))
#函数转成字典输出
# def test2(**kwargs):
#     return kwargs
# print(test2(a=1,b=2,c=3))

# 获取指定对象的所有属性和方法
# print(dir(test2.__code__))
#查看该函数有哪些参数
# a = test2.__code__.co_varnames
# 查看该函数来自那个文件
# a =test2.__code__.co_filename
# print(a)

# 匿名函数
# 定义一个匿名函数，输入一个数字，输出其平方
# square = lambda x: x ** 2
# print(square(3))

# -*- coding: utf-8 -*-
# class test(object): #所有的class都是object的派生类
#
# 	a = 1 #属性
# 	#当定义一个class的内置方法时，方法的参数的第一个永远是self。
# 	def __init__(self,var1): #构造函数
# 		self.var1 = var1 #这里的 self.var1 为全局变量
# 	#get被称之为test对象的方法
# 	def get(self,a=None):
# 		return self.var1
#
# 	def __del__(self): #析构函数
# 		del self.arg1
#
# 	pass


#使用
# t = test('test str heiheihei')
# print(t.get())
#捕获异常
# try :
#     a = 1/0
# except Exception as e:
#     print(e)
# finally:
#     print('finally')
#引发异常
# try:
#     raise Exception('引发异常')
# except Exception as e:
#     print(e)
#自定义异常
class MyException(Exception):
    pass
def my_func():
    raise MyException('自定义异常')
try:
    my_func()
except MyException as e:
    print(e)
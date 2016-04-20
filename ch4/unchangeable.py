# -*- coding: utf-8 -*
# 参数默认值
i = 5
def my_fun(num=i):
    """默认值只被赋值一次，传递了不可变的对象"""
    print num
i = 6
my_fun()

def append_list(a, l=[]):
    """默认值只被赋值一次,传递了可变的对象"""
    l.append(a)
    return l
print append_list(1)
print append_list(2)
print append_list(3)

def append_list_2(a, l=None):
    """将传递的可变的对象换成NOne,函数内部进行初始化，可避免每次调用会影响该对象"""
    if l is None:
        l = []
    l.append(a)
    return l
print append_list_2(1)
print append_list_2(2)
print append_list_2(3)

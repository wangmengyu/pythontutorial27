# -*- coding: utf-8 -*
def fib(number):
    """打印上限是指定数值的fib序列"""
    a, b = 0, 1
    while a < number:
        print a
        a, b = b, a+b
fib(2000)

f = fib  # fib是用户自定义函数类型，可以赋予别名
f(100)  # 调用别名函数

def fib_list(number):
    """返回一个包换fib序列的列表"""
    result = []
    a, b = 0, 1
    while a < number:
        result.append(a)
        a, b = b, a + b
    return result
f100 = fib_list(100)
print f100
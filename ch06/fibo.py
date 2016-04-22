# -*- coding: utf-8 -*
# Fibonacci 数列 module
def print_fib(n):
    """打印fib序列，n为上限"""
    a, b = 0, 1
    while (a < n):
        print a
        a, b = b, a+b
# 调用方式
# >>> import fibo
# >>> fibo.print_fib(1000)
# 函数可以赋予本地变量
# >>> print_fib = fibo.print_fib
# >>> print_fib(1000)

def collect_fib(n):
    """收集fib序列，n为上限"""
    result = []
    a, b = 0, 1
    while (a < n):
        result.append(a)
        a, b = b, a+b
    return result
# 导入调用方式
#>>> import fibo
#>>> result = fibo.collect_fib(1000)
#>>> print result

# 也可以用这种语法，把模块中的符号放到当前全局符号表
#>>> from fibo import print_fib, collect_fib
#>>> print_fib(100)

# 导入模块中所有函数到当前符号表， 除了'_'开头的命名 （不推荐做法）
#>>> from fibo import *
#>>> print collect_fib(100)

#在解释器中重新加载模块。因为每次导入只会导入一次，修改了代码需要reload
#>>> reload(fibo)
#<module 'fibo' from 'fibo.py'>
#>>> print collect_fib(100)


if __name__ == '__main__':
    # 以下代码会在python fib.py n 时候被执行, n是上限
    import sys
    print_fib(int(sys.argv[1]))















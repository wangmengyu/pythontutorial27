# -*- coding: utf-8 -*
# 函数式编程内置函数 filter
# filter(function, sequence)
# 返回一个序列 （不对原序列操作），序列中包含给定序列中所有调用function(item)后返回值是True的元素
# 如果sequence是str, unicode,tuple则总是返回相同类型，否则返回list

def f(x):
    """当x可以被3或者5整除的话返回true"""
    return x % 3 == 0 or x % 5 == 0
l = range(10)
print filter(f, l)# 返回过滤好的序列 [0, 3, 5, 6, 9]
print l# 不修改原序列 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]







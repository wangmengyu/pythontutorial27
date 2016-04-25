# -*- coding: utf-8 -*
# dir()函数， 用户搜索模块定义，返回一个排好序的字符串类型的存储列表

import fibo, sys
print dir(fibo)
print dir(sys)
#无参数，返回当前定义的命名列表
print dir()
#内置函数和变量名在模块__builtin__中定义：
import __builtin__
dir(__builtin__)

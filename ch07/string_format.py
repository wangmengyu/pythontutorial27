# -*- coding: utf-8 -*
import math
def rjust_square_cute(l):
    """用法rjust方法打印平方和立方"""
    for item in l:
        print repr(item).rjust(2), repr(item ** 2).rjust(3), repr(item ** 3).rjust(4)
rjust_square_cute(range(1, 11))


def format_square_cute(l):
    """用string.format方法打印平方和立方"""
    for item in l:
        print '{0:2d} {1:3d} {2:4d}'.format(item, item ** 2, item ** 3)
format_square_cute(range(1, 11))

# 参数定位
print '{0} and {1}'.format('spam', 'eggs') # spam and eggs
print '{1} and {0}'.format('eggs', 'spam') # spam and eggs

# 参数按照关键词参数使用
print 'The {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')
# The spam is absolutely horrible.

# 定位与关键词组合使用
print 'THe story of {0}, {1} and {other}.'.format('Bill', 'Manfred', other='Georg')
# THe story of Bill, Manfred and Georg.

# !s 对应 str(), !r 对应 repr() 在格式化之前转换值
print 'The value of PI is approximately {}.'.format(math.pi)
print 'The value of PI is approximately {!r}.'.format(math.pi)
# :之后可以指定格式化精度
print 'The value of PI is approximately {0:.3f}.'.format(math.pi)
# :之后可以指定字段的最小宽度
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for key, value in table.items():
    print '{0:10} => {1:10d}'.format(key, value)

#很长的格式化字符串，用命名来引用被格式化的变量，而不是位置。
#传入一个字典，用中括号来访问
print 'Jack: {0[Jack]:d}; Sjoerd:{0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)
#用**标志将这个字典以关键字参数的方式传入
print 'Jack: {Jack:d}; Sjoerd:{Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)
# -*- coding: utf-8 -*
# 元祖: 元素值可以重复
t = 12345, 54321, 'hello', 12345
print t
x, y, z, a = t # 元祖分配给等同数量的变量
print x, y, z, a

# 元祖可以是嵌套的
u = t, (1, 2, 3, 4, 5)
print u

# 元祖不可变.但是元祖可以包含多类型对象
v = ([1, 2, 3], [3, 4, 5])
print v
v[0][0] = 2
print v

empty = () # 空元祖
print len(empty)
singleton = 'hello', #只有一个元素的元祖，需要加逗号
print len(singleton)


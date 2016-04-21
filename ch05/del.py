# -*- coding: utf-8 -*
a = [66.25, 333, 333, 1, 1234.5]
del a[0] #删除0号位置元素
print a
del a[2:4] #删除2-4号位元素
print a
del a[:] #清空所有元素
print a
del a #删除变量，之后不可以再次引用
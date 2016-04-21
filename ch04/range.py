# -*- coding: utf-8 -*-
print range(10)
# 默认从0开始, 10是结束索引 [0,1,2,3,4,5,6,7,8,9]
print range(5, 10)
# [5,6,7,8,9]
print range(0, 10, 3)
# 从0开始到10结束,步长为3  [0,3,6,9]
print range(-10, -100, -30)
# [-10, -40, -70]

a = ['Mary', 'had', 'a', 'little', 'lamb']
# 结合range和len循环列表
for i in range(len(a)):
    print i, a[i]

# 同样的用 enumerate 也是可以有相同效果
for index, item in enumerate(a):
    print index, item
# -*- coding: utf-8 -*
# 内置函数map(f, sequence) 对sequence中每个元素进行f函数处理后组成新序列返回，不操作原序列
def cube(x):
    return x ** 3
seq = range(1, 8)
print map(cube, seq) # [1, 8, 27, 64, 125, 216, 343]
print seq #[1, 2, 3, 4, 5, 6, 7]
# -*- coding: utf-8 -*
# reduce(f, seq，default_value) 根据f处理头两个元素，再以返回值和第三个参数调用，依次执行下去。
def f (x, y):
    """返回两个数的和"""
    return x+y
seq = [1, 2, 3]
print reduce(f, seq) #6
print seq #[1, 2, 3]

#如过设定了第三个参数，即使是空序列也会返回第三个默认参数
seq = []
print reduce(f, seq, 0) #0
print seq #[]

#内置求和函数sum
seq = [1, 2, 3]
print sum(seq)
print seq

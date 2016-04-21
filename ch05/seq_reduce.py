# -*- coding: utf-8 -*
# reduce(f, seq) 根据f处理头两个元素，再以返回值和第三个参数调用，依次执行下去。
def f (x, y):
    """返回两个数的和"""
    return x+y
seq = [1, 2, 3]
print reduce(f, seq) #6
print seq #[1, 2, 3]
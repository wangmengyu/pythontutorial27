# -*- coding: utf-8 -*
#  收集序列1 - 10 的平方
def f(seq):
    """使用普通的循环完成列表的收集"""
    l = []
    for i in seq:
        l.append(i ** 2)
    return l


print f(range(1, 11))


def f_comprehension(seq):
    """使用列表推导式 [deal_item_sentence for or if loop or if condition]"""
    return [item ** 2 for item in seq]


print f_comprehension(range(1, 11))


def collect_def(seq_1, seq_2):
    return [(x, y) for x in seq_1 for y in seq_2 if x != y]


print collect_def([1, 2, 3], [3, 1, 4])

vec = [-4, -2, 0, 2, 4]


def double_num(seq):
    """返回×2的序列"""
    return [item * 2 for item in seq]


print double_num(vec)


def exclude_negative(seq):
    """返回非负数的序列"""
    return [item for item in seq if item > 0]


print exclude_negative(vec)


def abs_seq(seq):
    """返回绝对值的序列"""
    return [abs(item) for item in seq]


print abs_seq(vec)


def double_tuple(seq):
    """（元素，元素的平方）元祖组成的序列"""
    return [(item, item ** 2) for item in seq]


print double_tuple(range(6))


def flat_seq(seq):
    """平铺2元序列"""
    return [sub_item for item in seq for sub_item in item]


print flat_seq([[1, 2], [3, 4], [5, 6]])

from math import pi


def print_pi(n):
    """收集小数精确，从一位小数到n位小数序列"""
    return [round(pi, i) for i in range(1, abs(n) + 1)]


print print_pi(6)


def change_cavalcade(matrix):
    """交换矩阵的行和列，收集同列的序列，把序列组和而成新的序列"""
    column_num = len(matrix[0])
    return [[row[i] for row in matrix] for i in range(column_num)]

def change_cavalacade_common(matrix):
    """交换矩阵的行和列，收集同列的序列，把序列组和而成新的序列, 通用做法"""
    result = []
    column_num = len(matrix[0])
    for i in range(column_num):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        result.append(new_row)
    return result
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print change_cavalcade(matrix)
print change_cavalacade_common(matrix)

def change_cavalcade_zip(matrix):
    """用内置ZIP方法，该方法收集多个序列，把相同列的组成元祖。返回序列"""
    return zip(*matrix)
print change_cavalcade_zip(matrix)

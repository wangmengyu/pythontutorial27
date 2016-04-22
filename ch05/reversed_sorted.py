# -*- coding: utf-8 -*
# reversed()函数 ： 逆向循环序列, 不改变原序列，生成一个新的已逆转的序列
def reverse_print_list(l):
    """逆序打印序列"""
    for item in reversed(l):
        print item
l = range(1, 10, 2)
reverse_print_list(l)

#sorted()函数， 不改动原来的序列，生成一个新的已排序的序列
def sort_list(l):
    """排序序列，输出元素"""
    for item in sorted(l):
        print item
l = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
sort_list(l)

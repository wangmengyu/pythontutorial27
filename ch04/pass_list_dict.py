# -*- coding: utf-8 -*
# 传递列表参数
def print_list(num1, num2, num3):
    """形参有3个，传递一个列表具有相同个数元素"""
    print num1, num2, num3
param = [1, 3, 5]
print_list(*param)# 传参时在变量名前加*代表要展开列表成各个元素来传参

# 传递字典参数
def print_dict(key1='1', key2='2',key3='3'):
    """形参有3个，传递一个字典具有相同个数元素"""
    print key1, key2, key3
param_dict = {'key1': 'x', 'key2': 'y', 'key3': 'z'}
print_dict(**param_dict)# 传参时在变量名前加**代表要展开字典成各个元素来传参


# -*- coding: utf-8 -*
#enumerate()函数， 在序列循环中，逐一获取元素的位置和值
def enumerate_list(l):
    """循环遍历序列，输出索引和值"""
    for key, value in enumerate(l):
        print key, value
l1 = ['a', 'b', 'c']
enumerate_list(l1) #列表可用
l2 = ('a', 'b', 'c')
enumerate_list(l2) #元祖可用

#zip()函数，同时循环两个或更多序列，进行元素打包
def print_qa(q_list, a_list):
    """打印问题和他的答案，使用zip函数"""
    for q, a in zip(q_list, a_list):
        print "What's your "+q
        print a

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
print_qa(questions, answers)

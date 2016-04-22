# -*- coding: utf-8 -*
# slice copy = 切片复制
# 当需要在循环中修改序列的时候，需要循环 原序列的切片复制，因为循环不会隐士的创建副本，而是直接用的原序列
def insert_large_word(l):
    """在序列头部插入长度大于6的元素"""
    for item in l[:]: #使用原序列的切片复制
        if len(item) > 6:
            l.insert(0, item) #循环内部对原序列做修改
words = ['cat', 'window', 'defenestrate']
insert_large_word(words)
print words


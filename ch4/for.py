# -*- coding: utf-8 -*-
# 循环一个列表，并且，打印每个元素的长度
words = ['cat', 'window', 'defenestrate']
for item in words:
    print item, len(item)
print id(words)
# 错误范例： 把长度超过6的单词一次插入到序列头部，由于没有用切片复制原来的列表
# index每次到最后个元素发现要插入到列表最前端，死循环
print 'Wrong way:'
words = ['cat', 'window', 'defenestrate']
cnt = 0
for index, item in enumerate(words):
    if len(item) > 6:
        words.insert(0, item)
        print index
        print words
        cnt += 1
    if cnt > 10:
        break
print 'Right way:'
words = ['cat', 'window', 'defenestrate']
# 正确范例，使用切片复制原来的列表来循环，循环的集合长度不会变, 不会死循环
for index, item in enumerate(words[:]):
    if len(item) > 6:
        words.insert(0, item)
        print index
        print words

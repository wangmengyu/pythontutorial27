# -*- coding: utf-8 -*
# 关键字with处理文件，文件用完后会自动关闭
with open('test.md') as f:
    for line in f:
        print line
print f.closed # True 文件已被自动关闭





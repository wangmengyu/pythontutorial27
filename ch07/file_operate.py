# -*- coding: utf-8 -*
# 函数open()返回文件对象，open(filename, mode)
import os.path
fname = 'test.md'
print os.path.isfile(fname)

f = open(fname, 'r')
print f
# 读取整个文件
print f.read()
print 'twice read'
print f.read()

#f.readline() 读取单独一行
f = open(fname, 'r')
print f.readline()
print f.readline()
print f.readline()

#f.readlines() 返回一个列表，包含文件中所有的数据行
#print f.readlines()
#通过遍历文件来读取行，内存高效，快速，简洁
for line in f:
    print(line)

f = open(fname, 'a+') # 追加方式写入
#f.write(string) 方法将写入内容到文件，返回None：
print f.write('#This is a test\n')









# -*- coding: utf-8 -*
#f.tell()返回整数，代表文件对象在文件中的指针位置
f = open('test.md', 'r+')
f.write('0123456789abcdef')
#f.seek(offset, from_what) 改变文件对象指针,
#   from_what = 1 表示当前文件指针开始，
#   from_what=2表示文件末尾，
#   from_what = 0 表示从文件开始
#指针移动到5的位置
f.seek(5)
#读取一个长度字符
print f.read(1) #指针在6上
f.seek(-3, 1) # 从6上向前移动3格，结果3
print f.read(1) # 3

#关闭文件引用
f.close()












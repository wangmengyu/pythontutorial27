# -*- coding: utf-8 -*
# json 序列化
import json
str = json.dumps([1,'xxxx','ddddd'])
print str
#json.dump(s，f) 将对象s序列化后写入文件

d = {'a':1, 'b':2, 'c':3}
f = open('test.md', 'w')
json.dump(d, f)
f = open('test.md', 'r')
d = json.load(f)
print d




# -*- coding: utf-8 -*
# 短路操作符， and 和 or，
# 表达式可以赋值给一个变量， 它的值是最后一个执行到的元素的值
str1, str2, str3 = '', 'Trondheim', 'Hammer Dance'
non_null = str1 or str2 or str3
print non_null

# 比较序列和其他类型
# 其实是按元素一个个比较，
print (1, 2, 3) < (1, 2, 4)# True
print [1, 2, 3] < [1, 2, 4]# True
print 'ABC' < 'C' < 'Pascal' < 'Python' #True
print (1, 2, 3, 4) < (1, 2, 4) #True
print (1, 2) < (1, 2, -1) #True
print (1, 2, 3) == (1.0, 2.0, 3.0)#True
# 如果元素是相同类型，就递归字典比较，如果是不同类型 列表 < 字符串 < 元祖
print (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4) #Ture
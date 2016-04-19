# -*- coding: utf-8 -*-
# 打印2到10之间的素数
for n in range(2, 10):#第一层循环
    for x in range(2, n): #第2层循环
        if n % x == 0:
            print n,'=',x, '*', n/x
            break #跳出当前循环, 且不会执行else子句
    else:# 第2层循环的else子句, 只有当循环结束时执行, 而且在break跳出循环的时候, 是不会被执行的
        print n, ' is a prime number'

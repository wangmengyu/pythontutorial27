# -*- coding: utf-8 -*
# 字典
tel = {'jack': 4098, 'sape':4139}
tel['guido'] = 4127
print tel
print tel['jack']
del tel['sape'] #删除元素
tel['irv'] = 4127 #添加元素
print tel
print tel.keys() #输出键列表
print 'guido' in tel #判断键guido是否存在于tel

#dict()函数，将由key,value组成的元祖的元素的序列，转换成字典
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# 当关键字都是简单字符串(不包含空格)， 可以通过关键字参数指定key=value：
d2 = dict(scape=4139, guido=4127, jack=4098)
print d
print d2

#字典推导式
def dict_square(tuple_data):
    """把指定的元祖的元素按照 元素值-KEY，元素值的平方-VALUE的格式收集个字典"""
    return {item: item ** 2 for item in tuple_data}
print dict_square((2, 4, 6))



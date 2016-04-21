# -*- coding: utf-8 -*
# 集合 ： 元素值不可重复
# 功能： 关系测试，消除重复元素， 并集，交集，差集，对称差集
# set() 创建集合

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket) # 去掉重复元素
print fruit
print 'orange' in fruit
print 'Crabgrass' in fruit

#示范两个集合的操作
a = set('abracadabra')
b = set('alacazam')
print a # 去掉重复元素, 返回一个包含字母列表的集合 set(['a', 'r', 'b', 'c', 'd'])
print b # 去掉重复元素， 返回一个包含字母列表的集合set(['a', 'c', 'z', 'm', 'l'])
print a - b # 在于a但是不存在于b的元素集合 set(['r', 'b', 'd'])
print a | b # 在a或者b中的元素集合 set(['a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'])
print a & b # 在a而且在b中的元素集合 set(['a', 'c'])
print a ^ b # 在a或者b中, 但不是a,b中都有 set(['b', 'd', 'm', 'l', 'r', 'z'])

#集合推导式
def letter_not_in(str,exclude_str):
    return {item for item in str if item not in exclude_str}
print letter_not_in('aasccdfeddewed', 'abc')











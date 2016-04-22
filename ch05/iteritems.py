# -*- coding: utf-8 -*
# iteritems()在遍历字典时， 同时得到KEY-VALUE对
def iter_dict(dict):
    """利用dict.iteritems()字典对象的方法打印字典的键-值对"""
    for key, value in dict.iteritems():
        print key, value
dict = {'gallahad': 'the pure', 'robin': 'the brave'}
iter_dict(dict)



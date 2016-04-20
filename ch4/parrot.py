# -*- coding: utf-8 -*
# 关键词参数，形如keyword = value来调用
def parrot(voltage, state='state', action='action',type='type'):
    print voltage
    print state
    print action
    print type
parrot(1000)
parrot(voltage=1000) # 1个关键词参数
parrot(voltage=1000, action='ACTION') #2个关键词参数
parrot(action='VVVVOOOM', voltage=100000) #2个关键词参数
parrot('test', 'STATE', 'ACTION') #3位置参数



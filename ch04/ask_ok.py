# -*- coding: utf-8 -*
# 参数默认值
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    """用户输入指定次数字符串，命中yes和no的就进行退出，超出"""
    while (True):
        ok = raw_input(prompt)
        if ok in ['yes', 'y', 'ye']:
            return True
        elif ok in ['no', 'n', 'nop', 'nope']:
            return False
        retries -= 1
        if retries < 0:
            raise IOError('Invalid input')
        print complaint


ask_ok('Do you really want to quit?')
ask_ok('Do you really want to quit?', 2)
ask_ok('Do you really want to quit?', 2, 'Come on, only yes or no!')



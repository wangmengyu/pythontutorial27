# -*- coding: utf-8 -*
while True:
    try:
        x = int(raw_input('Please enter a number:'))
        print 'Your input number is:', x
        break
    except ValueError: #如果用户输入的不是数字会报错，循环会继续
        print 'Oops! That was no valid number. Try again...'
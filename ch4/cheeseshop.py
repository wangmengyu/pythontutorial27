# -*- coding: utf-8 -*
# 形参 *name，接收展开的元祖
# 形参 **name，接受展开的键值对字典
# *name 必须出现在 **name 之前
def cheeseshop(kind, *arguments, **keywords):
    """分别输出 字符串，展开的元祖，展开的字典"""
    print "-- Do you have any", kind, "?"
    print "-- I'msorry, we're all out of", kind
    for arg in arguments:
        print arg
    keys = sorted(keywords.keys())
    print '-' * 40
    for kw in keys:
        print kw, ':', keywords[kw]

cheeseshop('Limburger', #第一个参数
           "It's very runny, sir", #元祖参数
           "It's really very ,Very runny, Sir.", #元祖参数
           shopkeeper="Michael Palin",#字典KEY=VALUE对
           client="John Cleese",#字典KEY=VALUE对
           sketch="Cheese Shop Sketch"#字典KEY=VALUE对
           )

# -*- coding: utf-8 -*
def multiple_item(separator, *args):
    print separator.join(args)
multiple_item('&', 'a=1', 'b=2', 'c=3')
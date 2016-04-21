# -*- coding: utf-8 -*
# 把list当作队列使用，先进先出
# 使用collections.deque可以快速在首尾两端插入和删除
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print queue.popleft()
print queue
print queue.popleft()
print queue



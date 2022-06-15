"""
#implementing Queue using list
#
q = []
q.append("A")
q.append("B")
q.append("C")
print(q)

q.pop(0)
print(q)


#impelementing Queue using collection.deque
#instead of append and pop unlike list here we use append
#and popleft. It is faster than list O(1) for append and pop
from collections import deque
q = deque()
q.append("A")
q.append("B")
q.append("C")
print(q)
q.popleft()
print(q.popleft())
print(q)

"""

# implememnting queue using queue.Queue
# inbuilt-functions are:
# maxsize, put, get, empty, full, qsize
# get_nowait, put_nowait

from queue import Queue
q = Queue(maxsize=4)

q.put("A")
q.put("B")
q.put("C")
q.put("D")

print(q.full())
q.get(False)
q.get()
print(q.full(),q.empty())
print(q.qsize())
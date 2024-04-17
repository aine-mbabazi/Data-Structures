from collections import deque
fruits = deque()
fruits.append('pawpaw')
fruits.append('jackfruit')
fruits.append('mangoes')
fruits.append('apple')
print("Initial queue")
print(fruits)
print("\nElements dequeued from the queue")
print(fruits.pop())
print(fruits.pop())
print(fruits.pop())
print(fruits.pop())

# Implementation of queue using queue
from queue import Queue
q = Queue(maxsize = 4)
print(q.qsize()) 
q.put('apple')
q.put('beans')
q.put('cabbage')
q.put('dates')

print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())


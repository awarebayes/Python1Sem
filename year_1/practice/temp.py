import heapq
from random import randint

heap = []
for i in range(10):
    r = randint(10,100)
    if r not in heap:
        heapq.heappush(heap, r)

print(heap)
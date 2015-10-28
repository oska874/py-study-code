# -*- coding: utf-8 -*-

import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

print (heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

print(heapq.nsmallest(3,[2,3,1,4,9,5,7,6,0]))
print(heapq.nlargest(3,[2,3,1,4,9,5,7,6,0]))

print(heapq.merge([1,2,3],[5,3,4],[6,4,'r']).next())

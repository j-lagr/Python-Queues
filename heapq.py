from heapq import heappush

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)

from heapq import heappop

print(heappop(fruits))
print(fruits)
import heapq
import sys
input = lambda : sys.stdin.readline().rstrip()

h = []
heapq.heapify(h)
n = int(input())
for i in range(n):
  data = int(input())
  if data == 0:
    if not h:
      print(0)
    else:
      print(heapq.heappop(h)[1])
  else:
    heapq.heappush(h, (-data, data))
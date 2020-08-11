# # 풀이 1
# # 최대힙 이용 -> 메모리 초과..
# import heapq
# import sys
# input = lambda: sys.stdin.readline()
# h = []
# n = int(input())
# for _ in range(n):
#   for data in map(int, input().split()):
#     heapq.heappush(h, (-data, data))
# print(h[n-1][1])

# import heapq
# import sys
# input = lambda : sys.stdin.readline().rstrip()




# # -------------------------------
# # 풀이 2
# # 최소힙 이용
# # 모든 값을 넣으면 시간초과가 발생해서
# # n*n의 큰 값 n번 째를 찾을 수 있는 20번까지만 반복했다.
# # 그런데,,, 여전히 메모리 초과. . . 

# h = []
# n = int(input())
# for n in map(int, input().split()):
#   heapq.heappush(h, n)

# for _ in range(1, n):
#   for data in map(int, input().split()):
#     heapq.heappush(h, data)
#     heapq.heappop(h)
# print(heapq.heappop(h))


# # -------------------------------
# # 풀이 3
# # 정렬 이용
# # 초기값으로 n개 저장
# # 순서대로 n개만 저장하고 그 다음 행 추가해서 비교
# [19, 15, 13, 12, 11, 9, 8, 7, 6, 5]
# [31, 26, 21, 19, 16, 15, 13, 12, 11, 10]
# [48, 35, 31, 28, 26, 25, 21, 19, 16, 14]
# [52, 49, 48, 41, 35, 32, 31, 28, 26, 20]


import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int, input().split()))
for i in range(n-1):
  temp = sorted(list(map(int, input().split())) + arr,reverse=True)
  print(temp)
  arr = temp[:n]
print(arr[n-1])
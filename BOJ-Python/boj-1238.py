# boj-1238 파티
# 알고리즘 스터디


### 시간초과

# 문제 해결
# 플로이드 와샬
# 최단 시간, 단방향


# import sys
# input = sys.stdin.readline

# INF = int(1e9)
# n, m, x = map(int, input().split()) # 마을, 도로 수, 파티할 마을
# graph = [[INF] * (n+1) for _ in range(n+1)]

# # 시작, 끝, 소요시간 
# for _ in range(m):
#   a, b, t = map(int, input().split())
#   # 시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.
#   graph[a][b] = t

# for k in range(1, n+1):
#   for i in range(1, n+1):
#     if graph[i][k] != INF:
#       for j in range(1, n+1):
#         if i == j :
#           graph[i][j] = 0 
#         else:
#           graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# max_value = -1
# for i in range(1, n+1):
#   max_value = max(max_value, graph[i][x] + graph[x][i])
# print(max_value)



### 맞았습니다 !

# 문제해결
# 다익스트라 -> 우선순위 큐

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m, x = map(int, input().split()) 

graph = [[] for _ in range(n+1)] # 노드 (이동가능한 노드, 거리)
distance = [INF] * (n+1) # 최단거리 테이블

for _ in range(m):
  a, b, t = map(int, input().split())
  graph[a].append((b, t))

def dijkstra(start) : 
  q = [] # (거리, 노드)
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: # 최단거리 테이블 값과 현재 거리 값 비교
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(x)
temp = [0]
for i in range(1, n+1):
  temp.append(distance[i])
distance = [INF] * (n+1)

for i in range(1, n+1):
  dijkstra(i)
  temp[i] += distance[x]
  distance = [INF] * (n+1)
  
print(max(temp))
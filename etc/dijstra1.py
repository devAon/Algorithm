import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[]for _ in range(n+1)] # 노드 정보
visited = [False] * (n+1) # 방문 여부 확인
distance = [INF] * (n+1) # 최단 거리 테이블

for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b, c))


# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijstra(start):
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]

  for i in range(n-1):
    now = get_smallest_node()
    visited[now] = True

    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
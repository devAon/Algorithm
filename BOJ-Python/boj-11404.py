# 플로이드
# 왜 플로이드 알고리즘을 사용했나? 양방향 가능. 간선. 최소비용
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신(대각선) 0으로 초기화
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j :
      graph[i][j] = 0

# 각 간선에 대한 정보 입력받아 초기화
for _ in range(m):
  a, b, c = map(int, input().split())
  if c < graph[a][b]: # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
    graph[a][b] = c

# 플로이드 와샬
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == INF:
      print("0", end = " ")
    else:
      print(graph[i][j], end = " ")
  print()
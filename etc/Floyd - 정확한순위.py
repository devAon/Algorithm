# 최단 경로 계산 문제
# 방향 그래프로 학생들의 성적 비교 표현 (성적 낮은 학생 -> 성적 높은 학생)
# A에서 B로 도달이 가능하거나, B에서 A로 도달이 가능하면 '성적비교'가 가능한 것 
# A에서 B로 도달이 불가능하거나, B에서 A로 도달이 불가능하면 '성적비교'가 불가능한 것 

# 학생의 수 N이 500 이하의 정수이므로, O(N^3) 시간 복잡도인 플로이드와샬 사용 가능
# 플로이드 수행 후, 서로 도달 가능한지 체크해서 가능할 경우의 횟수 출력

INF= int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기에서 자기 자신 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  a,b = map(int, input().split())
  graph[a][b] = 1



#점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
result = 0
for a in range(1, n+1):
  cnt = 0
  for b in range(1, n+1):
    if graph[a][b] != INF or graph[b][a] != INF:
      cnt += 1
    
  if cnt == n:
    result += 1
print(result)
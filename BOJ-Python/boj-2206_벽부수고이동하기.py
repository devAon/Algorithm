# BSF 최단 경로 구해라!
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

# dist[n][m][z] z는 벽을 부순 횟수(z==0 벽 부수준 적 없음, z==1 있음 )
dist = [[[0]*2 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0,0,0))
dist[0][0][0] = 1 # 출발점도 이동으로 계산되기 때문에 1
while q:
    x,y,z = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0 and dist[nx][ny][z] == 0:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx, ny, z))
            if z == 0 and arr[nx][ny] == 1 and dist[nx][ny][z] == 0:
                dist[nx][ny][z+1] = dist[x][y][z] + 1
                q.append((nx, ny, z+1))

if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0:
    print(min(dist[n-1][m-1][0], dist[n-1][m-1][1]))
elif dist[n-1][m-1][0] != 0:
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1] != 0:
    print(dist[n-1][m-1][1])
else:
    print(-1)
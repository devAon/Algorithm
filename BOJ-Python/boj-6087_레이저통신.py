# BFS C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값
# C -> C 가는데 필요한 직선의 개수 -1 == 설치해야하는 거울 개수
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
w, h = map(int, input().split())
a = [input() for _ in range(h)]

sx = sy = ex = ey = -1
for i in range(h):
    for j in range(w):
        if a[i][j] == 'C':
            if sx == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j

q = deque()
q.append((sx, sy))
dist = [[-1] * w for _ in range(h)]
dist[sx][sy] = 0
while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        while 0 <= nx < h and 0 <= ny < w:
            if a[nx][ny] == '*':
                break
            if dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
            nx += dx[k]
            ny += dy[k]
print(dist[ex][ey] - 1)
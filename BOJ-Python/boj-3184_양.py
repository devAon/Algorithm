from collections import deque
import sys
input = lambda: sys.stdin.readline()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a, visited, x, y):
    ocnt, vcnt = 0,0
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    if a[x][y] == 'o': ocnt += 1
    elif a[x][y] == 'v': vcnt += 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx,ny = x + dx[k], y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and a[nx][ny] != '#':
                q.append((nx, ny))
                visited[nx][ny] = True
                if a[nx][ny] == 'o': ocnt += 1
                elif a[nx][ny] == 'v': vcnt += 1
    if ocnt <= vcnt: ocnt = 0
    else: vcnt = 0
    return ocnt, vcnt
r, c = map(int, input().split())
a = [input() for _ in range(r)]
visited = [[False] * c for _ in range(r)]
ocnt, vcnt = 0, 0
for i in range(r):
    for j in range(c):
        if a[i][j] in 'ov':
            if not visited[i][j]:
                o, v = bfs(a, visited, i, j)
                ocnt += o
                vcnt += v
print(ocnt, vcnt)
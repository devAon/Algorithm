from collections import deque
import sys
input=lambda:sys.stdin.readline()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, team,cnt):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = dx[k] + x, dy[k] + y
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and a[nx][ny] == team:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt

def dfs(x, y, team, cnt):
    visited[x][y] = True
    for k in range(4):
            nx, ny = dx[k] + x, dy[k] + y
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and a[nx][ny] == team:
                    visited[nx][ny] = True
                    cnt = dfs(nx, ny, team, cnt+1)
    return cnt

m,n = map(int, input().split())
a = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

wcnt, bcnt = 0, 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            ans = dfs(i, j, a[i][j],1) # dfs 풀이
            #ans = bfs(i, j, a[i][j],1) # bfs 풀이
            if a[i][j] == 'W': wcnt += ans ** 2
            else: bcnt += ans ** 2
print(wcnt, bcnt)
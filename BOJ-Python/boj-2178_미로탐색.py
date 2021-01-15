from collections import deque
n,m = map(int, input().split())
d = [list(map(int, input())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if d[nx][ny] == 0:
                continue
            if d[nx][ny] == 1:
                d[nx][ny] = d[x][y] + 1
                queue.append((nx, ny))
    return d[n-1][m-1]
print(bfs(0,0))
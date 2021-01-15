from collections import deque
import sys
input = lambda:sys.stdin.readline()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(x, y, z):
    q = deque()
    q.append([x, y, z])
    visited[x][y][z] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if d[nx][ny][nz] == 'E':
                    print(f'Escaped in {visited[x][y][z]} minute(s).')
                    return 
                if visited[nx][ny][nz] == 0 and d[nx][ny][nz] == '.':
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q.append([nx, ny, nz])
    print("Trapped!")
    return

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0: break

    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    d = []
    for _ in range(l):
        d.append([ list(map(str, input().strip()))  for _ in range(r) ])
        input()
    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if d[i][j][k] == 'S':
                    bfs(i, j, k)
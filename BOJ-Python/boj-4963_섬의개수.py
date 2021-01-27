# BFS
from collections import deque
import sys
input = lambda:sys.stdin.readline()
sys.setrecursionlimit(10**6)

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

# DFS - 메모리초과
# def dfs(x,y):
#     visited[x][y] = 1
#     for k in range(8):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < h and 0 <= ny < w:
#             if data[nx][ny] == 1 and visited[nx][ny] == 0:
#                 dfs(nx, ny)

def bfs(x, y, cnt):
    q = deque()
    q.append((x,y))
    visited[x][y] = cnt
    while q:
        x,y = q.popleft()
        for k in range(8):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if data[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = cnt
    
while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0: break
    
    data = [ list(map(int, input().split())) for _ in range(h)]
    visited = [ [0] * (w) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if data[i][j] == 1 and visited[i][j] == 0: # 섬 && 방문X
                cnt += 1
                bfs(i, j, cnt)
                #dfs(i, j)
    print(cnt)
# DFS
import sys
sys.setrecursionlimit(10**6)
dx = [-1,1,0,0]
dy=  [0,0,-1,1]
def dfs(a, visited, x, y , d):
    visited[x][y] = True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if  0<=nx<n and 0<=ny<n and not visited[nx][ny] and a[nx][ny] in d:
            dfs(a, visited, nx, ny, d)
n = int(input())
a = [input() for _ in range(n)]
visited = [[False]*n for _ in range(n)]
acnt,bcnt = 0,0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            acnt+=1
            dfs(a, visited, i, j, a[i][j])
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bcnt+=1
            if a[i][j] == 'B':
                dfs(a, visited, i, j, a[i][j])
            else:
                dfs(a, visited, i, j, 'RG')
print(acnt, bcnt)

# BFS (DFS보다 시간 더 오래 걸림..)
# from collections import deque
# dx = [-1,1,0,0]
# dy=  [0,0,-1,1]
# def bfs(a, visited, x, y , d):
#     q = deque()
#     q.append([x,y])
#     visited[x][y] = True
#     while q:
#         x,y  = q.popleft()
#         for k in range(4):
#             nx, ny = x+dx[k], y+dy[k]
#             if  0<=nx<n and 0<=ny<n and not visited[nx][ny] and a[nx][ny] in d:
#                 q.append([nx, ny])
#                 visited[nx][ny] = True
# n = int(input())
# a = [input() for _ in range(n)]
# visited = [[False]*n for _ in range(n)]
# acnt,bcnt = 0,0
# for i in range(n):
#     for j in range(n):
#         if not visited[i][j]:
#             acnt+=1
#             bfs(a, visited, i, j, a[i][j])
# visited = [[False]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if not visited[i][j]:
#             bcnt+=1
#             if a[i][j] == 'B':
#                 bfs(a, visited, i, j, a[i][j])
#             else:
#                 bfs(a, visited, i, j, 'RG')
# print(acnt, bcnt)
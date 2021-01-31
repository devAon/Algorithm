from collections import deque
import sys
input = lambda:sys.stdin.readline()

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(arr, x, y):
    h = len(arr)
    w = len(arr[0])
    dist = [[-1]*w for _ in range(h)]
    q = deque()
    q.append((x,y))
    dist[x][y] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < h and 0 <= ny < w and dist[nx][ny] == -1 and arr[nx][ny] != '*':
                if arr[nx][ny] == '#':
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                else:
                    q.appendleft((nx, ny))
                    dist[nx][ny] = dist[x][y]
    return dist

t = int(input())
for _ in range(t):
    h,w = map(int, input().split())
    arr = ['.'+input()+'.' for _ in range(h)]
    h += 2
    w += 2
    arr = ['.'*w] + arr+ ['.'*w]
    
    x1=x2=y1=y2 = -1
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '$':
                if x1 == -1:
                    x1,y1 = i,j
                else:
                    x2,y2 = i,j
    d0 = bfs(arr, 0,0)
    d1 = bfs(arr, x1, y1)
    d2 = bfs(arr, x2, y2)
    
    ans = h*w
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                continue
            if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
                continue
            cur = d0[i][j]+d1[i][j]+d2[i][j]
            if arr[i][j] == '#':
                cur -= 2
            ans = min(ans, cur)
    print(ans)
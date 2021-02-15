from collections import deque
dx = [-1,-1,-2,-2,1,1,2,2]
dy = [-2,2,-1,1,-2,2,-1,1]
t = int(input())
for _ in range(t):
    n = int(input())
    sx,sy = map(int, input().split())
    ex,ey =  map(int, input().split())
    if sx==ex and sy==ey:
        print(0)
        continue
    check = [[-1]*n for _ in range(n)]
    q= deque()
    q.append((sx, sy))
    check[sx][sy] = 0
    while q:
        x,y = q.popleft()
        if x == ex and y == ey:
            break
        for k in range(8):
            nx, ny = dx[k]+x, dy[k]+y
            if 0<=nx<n and 0<=ny<n:
                if check[nx][ny] == -1:
                    check[nx][ny] = check[x][y] + 1
                    q.append((nx,ny))
    print(check[ex][ey])
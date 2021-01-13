import sys
sys.setrecursionlimit(10000)
n = int(input())
d = [list(map(int,input())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global h
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if d[x][y] == 1:
        d[x][y] = 0
        h += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

house = []
cnt = 0
for i in range(n):
    for j in range(n):
        h = 0
        if dfs(i,j) == True:
            cnt += 1
            house.append(h)
house.sort()
print(cnt)
for h in house: print(h)
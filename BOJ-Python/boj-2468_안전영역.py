import sys
sys.setrecursionlimit(10**6)
input = lambda:sys.stdin.readline()
n = int(input())
d = [list(map(int, input().split())) for _ in range(n)] 
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = [] 
big= max(max(d))
def rain(num):
    global visited
    for i in range(n):
        for j in range(n):
            if d[i][j] <= num:
                visited[i][j] = 1
def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if visited[x][y] == 0:
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False
for i in range(big+1):
    visited =[[0]*n for _ in range(n)]
    rain(i)
    cnt = 0
    for j in range(n):
        for k in range(n):
            if dfs(j,k) == True:
                cnt += 1
    result.append(cnt)
print(max(result))
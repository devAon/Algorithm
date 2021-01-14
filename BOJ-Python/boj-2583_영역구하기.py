import sys
sys.setrecursionlimit(10**8)
input = lambda:sys.stdin.readline()
def dfs(x,y):
    global each
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if d[x][y] == 0:
        d[x][y] = 1
        each += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False
if __name__ == '__main__':
    m,n,k = map(int, input().split())
    d = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        ly,lx,ry,rx = map(int, input().split())
        for i in range(lx, rx):
            for j in range(ly, ry):
                d[i][j] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    area = []
    cnt = 0 # 영역의 개수
    for i in range(m):
        for j in range(n):
            each = 0 # 각 영역의 넓이
            if dfs(i, j) == True:
                cnt += 1
                area.append(each)
    area.sort()
    print(cnt)
    for a in area: print(a, end = ' ')
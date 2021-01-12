import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    global result
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return -1 # False
    if d[x][y] == 1:
        result += 1
        d[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

if __name__ == '__main__':
    n,m,k = map(int, input().split())
    d = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        d[x-1][y-1] = 1
    answer = []
    for i in range(n):
        for j in range(m):
            result = 0
            if dfs(i,j) == True:
                answer.append(result)
    print(max(answer))
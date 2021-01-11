import sys
sys.setrecursionlimit(10000)

def dfs(d, v, visited):
    visited[v]= True
    for i in d[v]:
        if not visited[i]:
            dfs(d, i, visited)

n,m = map(int, input().split())
d = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = 0

for _ in range(m):
    u,v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)

for i in range(1,n+1):
    if not visited[i]:
        dfs(d,i,visited)
        result += 1
print(result)
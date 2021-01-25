from collections import deque
def bfs(s):
    q = deque([s])
    visited[s] = True
    result = 0
    while q:
        result += 1
        for _ in range(len(q)):
            v = q.popleft()
            if v == b:
                return result -1
            for i in d[v]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
    return -1
n = int(input())
a,b = map(int, input().split())
d=[[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    x,y = map(int, input().split())
    d[x].append(y)
    d[y].append(x)
visited = [False] * (n+1)
print(bfs(a))
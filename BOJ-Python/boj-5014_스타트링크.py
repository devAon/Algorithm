from collections import deque
def bfs():
    q = deque([s-1])
    check[s-1] = 1
    while q:
        x = q.popleft()
        if x == g-1:
            return check[x]-1
        for nx in [x+u, x-d]:
            if 0 <= nx < f and not check[nx]:
                check[nx] = check[x]+1
                q.append(nx)
    return "use the stairs"
f,s,g,u,d = map(int, input().split())
check = [0] * (f)
print(bfs())
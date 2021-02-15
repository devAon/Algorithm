from collections import deque
a,b = map(int, input().split())
q= deque()
q.append((a,1))
while q:
    now, cnt = q.popleft()
    if now == b:
        print(cnt)
        exit()
    if now*2 <= b:
        q.append((now*2, cnt+1))
    t = int(str(now)+"1")
    if t <= b:
        q.append((t, cnt+1))
print(-1)
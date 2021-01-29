from collections import deque
import sys
MAX = 200000
sys.setrecursionlimit(MAX)

n,k = map(int, input().split())
dist = [-1] * MAX  # 이동한 거리
check = [False] * MAX # 방문체크
move = [-1]*MAX # from[next]=now

q = deque([n])
dist[n] = 0
check[n] = True
while q:
    now = q.popleft()
    for nxt in [now*2, now+1, now-1]:
        if 0 <= nxt < MAX and check[nxt] == False:
            q.append(nxt)
            check[nxt] = True
            dist[nxt] = dist[now] + 1
            move[nxt] = now
print(dist[k])
def print_move(n,m):
    if n != m:
        print_move(n, move[m])
    print(m, end = ' ')
print_move(n,k)
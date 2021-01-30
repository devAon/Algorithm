from collections import deque
import sys
MAX = 10001
sys.setrecursionlimit(MAX)
input = lambda : sys.stdin.readline()

def via_print(n, m):
    if n == m:
        return
    via_print(n, via[m])
    print(how[m], end='')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        visited = [False] * MAX  # 방문여부 체크
        dist = [-1] * MAX  # 최단거리 기록
        via = [-1] * MAX  # 어디서 어디로 이동했는지 기록
        how = [''] * MAX # DSLR 중 어떤 방법으로 이동했는지 기록
            
        q = deque([n])
        dist[n] = 0
        visited[n] = True
        via[n] = -1
        while q:
            now = q.popleft()
            # D: nxt = (n*2)%10000
            # S: nxt = (n-1) if n-1 == -1 :v nxt = 9999
            # L: nxt = (n%1000)*10 + (n//1000)
            # R: nxy = (n%10)*1000 + (n//10)

            for index, nxt in enumerate([(now * 2) % 10000, now - 1, (now % 1000) * 10 + (now // 1000), (now % 10) * 1000 + (now // 10)]):
                if nxt == -1: nxt = 9999
                if not visited[nxt]:
                    q.append(nxt)
                    dist[nxt] = dist[now] + 1
                    visited[nxt] = True
                    via[nxt] = now
                    if index == 0: how[nxt] = 'D'
                    elif index == 1: how[nxt] = 'S'
                    elif index == 2: how[nxt] = 'L'
                    elif index == 3: how[nxt] = 'R'

        via_print(n,m)
        print()
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

t = int(input())
for _ in range(t):
    h,w = map(int, input().split())
    a = [ '.'+input()+'.' for _ in range(h)]
    h += 2
    w += 2
    a = ['.'*w] + a + ['.'*w]
    key = set(input())

    q = deque()
    q.append((0,0))
    door = [ deque() for _ in range(26)]
    visited = [[False] *w for _ in range(h)]
    visited[0][0] = True
    ans = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and a[nx][ny] != '*':
                data = a[nx][ny]
                visited[nx][ny] = True
                
                if data == '.':
                    q.append((nx, ny))
                elif data == '$':
                    ans += 1
                    q.append((nx, ny))
                elif 'A' <= data <= 'Z' : # 문
                    if data.lower() in key: # 키가 있으면
                        q.append((nx, ny))
                    else: # 키 없으면
                        door[ord(data)-ord('A')].append((nx, ny))
                elif 'a' <= data <= 'z': # 키 줍줍
                    q.append((nx, ny))
                    if data not in key:
                        key.add(data)
                        q.extend(door[ord(data)-ord('a')])
    print(ans)
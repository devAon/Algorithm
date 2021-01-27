# BFS 
from collections import deque
import sys
input = lambda: sys.stdin.readline()

def bfs(i, c): # 정점, 색상
    q = deque([i])
    visited[i] = True
    color[i] = c
    while q:
        i = q.popleft()
        for j in arr[i]:
            if not visited[j]:
                visited[j] = True
                q.append(j)
                color[j] = 3- color[i]
            else:
                if color[i] == color[j]:
                    return False
    return True

if __name__ == '__main__':
    k = int(input())
    for _ in range(k): # 테스트 케이스 
        v,e = map(int, input().split())
        color = [0] * (v+1)
        arr = [[] for _ in range(v+1)]
        for _ in range(e):
            a,b = map(int, input().split())
            arr[a].append(b)
            arr[b].append(a)
        
        answer = True
        visited = [False] * (v+1)
        for i in range(1, v+1):
            if not visited[i]:
                if not bfs(i, 1): # return False이면 종료
                    answer = False
                    break
        print('YES' if answer else 'NO')



# DFS -> 메모리 초과
# from collections import deque
# import sys
# input = lambda: sys.stdin.readline()
# sys.setrecursionlimit(10**6)

# def dfs(i, c): # 정점, 색상
#     color[i] = c
#     for j in arr[i]:
#         if color[j] == 0:
#             if not dfs(j, 3-c):
#                 return False
#         elif color[i] == color[j]:
#             return False
#     return True

# if __name__ == '__main__':
#     k = int(input())
#     for _ in range(k): # 테스트 케이스 
#         v,e = map(int, input().split())
#         color = [0] * (v)
#         arr = [[] for _ in range(v)]
#         for _ in range(e):
#             a,b = map(int, input().split())
#             arr[a-1].append(b-1)
#             arr[b-1].append(a-1)
        
#         answer = True
#         for i in range(0, v):
#             if color[i] == 0:
#                 if not dfs(i, 1):
#                     answer = False
#         print('YES' if answer else 'NO')

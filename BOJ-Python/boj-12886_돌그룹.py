from collections import deque
a,b,c = map(int, input().split())
visited = [[False]*1501 for _ in range(1501)]
tot = a+b+c
def dfs():
    global a,b,c
    q = deque()
    q.append([a,b])
    visited[a][b] = True
    while q:
        a,b = q.popleft()
        c = tot-a-b
        if a==b==c: 
            return 1
        for na, nb in ((a,b),(a,c),(b,c)):
            if na < nb:
                nb -= na
                na += na
            elif na > nb:
                na -= nb
                nb += nb
            else: continue
            nc = tot-na-nb
            a = min(min(na,nb), nc)
            b = max(max(na, nb), nc)
            if not visited[a][b]:
                q.append((a,b))
                visited[a][b] = True
    return 0
if tot%3 != 0: print(0)
else:
    print(dfs())


# from collections import deque, defaultdict
# stones = list(map(int, input().split()))
# visited = defaultdict(bool)
# tot = sum(stones)
# def dfs():
#     q = deque([stones])
#     visited[tuple(stones)] = True
#     while q:
#         a,b,c = q.popleft()
#         if a==b==c: 
#             return 1
#         for x,y in ((a,b),(a,c),(b,c)):
#             if x == y: continue
#             elif x < y:
#                 y -= x
#                 x += x
#             elif x > y:
#                 x -= y
#                 y += y
#             z = tot-x-y
#             if not visited[(x,y,z)] :
#                 visited[(x,y,z)] = True
#                 q.append([x,y,z])
#     return 0
# if tot%3 != 0: print(0)
# else:
#     print(dfs())
# print(visited)
# print(len(visited))
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
blocks = (
    ((0, 1), (0, 2), (0, 3)),
    ((1, 0), (2, 0), (3, 0)),
    ((0, 1), (1, 0), (1, 1)),
    ((1, 0), (2, 0), (2, 1)),
    ((1, 0), (2, 0), (2, -1)),
    ((0, 1), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((1, 0), (1, 1), (1, 2)),
    ((-1, 2), (0, 1), (0, 2)),
    ((0, 1), (0, 2), (1, 0)),
    ((0, 1), (0, 2), (1, 2)),
    ((1, 0), (1, 1), (2, 1)),
    ((-1, 1), (0, 1), (1, 0)),
    ((-1, 1), (-1, 2), (0, 1)),
    ((0, 1), (1, 1), (1, 2)),
    ((0, 1), (0, 2), (1, 1)),
    ((1, -1), (1, 0), (1, 1)),
    ((-1, 1), (0, 1), (1, 1)),
    ((1, 0), (1, 1), (2, 0))
)
answer = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            ok = True
            s = data[i][j]
            for dx, dy in block:
                nx = dx + i
                ny = dy + j
                if 0 <= nx < n and 0 <= ny < m:
                    s += data[nx][ny]
                else: 
                    ok = False
                    break
            if ok and answer < s:
                answer = s
print(answer)
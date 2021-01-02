N, L = map(int, input().split())
position = list(map(int, input().split()))
position.sort()

start = 0
result = 0
for p in position:
    if start < p:
        start = p + L - 1
        result += 1
print(result)
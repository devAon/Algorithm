from itertools import combinations
n,s = map(int, input().split())
d = list(map(int, input().split()))
result = 0
for i in range(1, n+1):
    c = list(combinations(d, i))
    for j in range(len(c)):
        if s == sum(c[j]): result += 1
print(result)
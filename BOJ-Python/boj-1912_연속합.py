n = int(input())
d = list(map(int, input().split()))
for i in range(1, len(d)):
    d[i] = max(d[i], d[i-1]+d[i])
print(max(d))
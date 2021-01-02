N = int(input())
weight = [ int(input()) for _ in range(N)]
weight.sort(reverse=True)

result = 0
for i in range(N):
    t = weight[i] * (i+1)
    result = max(t, result)
print(result)
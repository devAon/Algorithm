N, K = map(int, input().split())
coins = [ int(input()) for _ in range(N)]
coins.sort(reverse = True)

result = 0
for coin in coins:
    if coin <= K:
        cnt = K // coin
        K = K - (coin * cnt)
        result += cnt
    if K == 0: break
print(result)
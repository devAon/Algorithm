def prime(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

n = int(input())
arr = list(map(int, input().split()))
result = 0
for a in arr:
    if prime(a) == True: result +=1
print(result)
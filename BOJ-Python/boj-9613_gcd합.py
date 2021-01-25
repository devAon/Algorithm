# from itertools import combinations
# def gcd(a,b):
#     if b == 0: return a
#     else: return gcd(b,a%b)
# t = int(input())
# for _ in range(t):
#     arr = list(map(int, input().split()))
#     arr.pop(0)
#     c = list(combinations(arr, 2))
#     result = 0
#     for a,b in c:
#         result += gcd(a,b)
#     print(result)

def gcd(a,b):
    if b == 0: return a
    else: return gcd(b,a%b)
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    n = arr[0]
    c = arr[1:]
    result = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            result += gcd(c[i], c[j])
    print(result)
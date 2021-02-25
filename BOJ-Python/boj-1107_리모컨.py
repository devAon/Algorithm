enable = { str(i) for i in range(10)}
n = int(input())
m = int(input())
if m != 0:
    enable -= set(map(str, input().split()))
ans = abs(100-n)
for num in range(1000001):
    num = str(num)
    for i in range(len(num)):
        if num[i] not in enable:
            break
        elif i == len(num)-1:
            ans = min(ans, abs(n-int(num))+len(str(num)))
print(ans)
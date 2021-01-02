n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
d = [] # 각 집중국의 수신 가능영역의 거리
for i in range(1, len(arr)):
    d.append(arr[i]-arr[i-1])
d.sort()
for i in range(k-1):
    if len(d) == 0:
        break
    else:
        d.pop()
print(sum(d))

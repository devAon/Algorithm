t = int(input())
d = [0] * 11
d[0]=d[1]=1
d[2]=2
for i in range(3, 11):
    d[i] = d[i-1]+d[i-2]+d[i-3]
for _ in range(t):
    n = int(input())
    print(d[n])

# 다른 사람 풀이
# d[i-1]+d[i-2]+d[i-3] 대신, arr에 있는 값들 중 뒤에서 부터 3개의 합
# N = int(input())
# arr=[1,2,4]
# for i in range(4,11):
#     arr.append(sum(arr[-3:]))
# for _ in range(N):
#     T = int(input())
#     print(arr[T-1])
def check(password):
    ja, mo = 0,0
    for p in password:
        if p in 'aeoui': mo += 1
        else: ja += 1
    if ja >= 2 and mo >= 1: return 1
    return 0

# 만들 암호 길이, 주어진 알파벳, 현재까지 만든 암호, 사용할지 말지 결정하는 알파벳의 index
def go(l, alpha, password, i):
    if l == len(password):
        if check(password):
            print(password)
            return
    if i >= len(alpha): return
    go(l, alpha, password+alpha[i], i+1) # 사용
    go(l, alpha, password, i+1) # 사용 안함

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
go(l, alpha, '', 0)


# 조합사용
# from itertools import combinations
# l,c = map(int, input().split())
# a= list(map(str, input().split()))
# a.sort()
# u=0
# for c in combinations(a, l):
#     cnt = 0
#     for check in c:
#         if check in ['a','e', 'i', 'o', 'u']:
#             cnt += 1
#     if cnt >= 1 and cnt<=l-2:
#         print(''.join(c))
# 조합 풀이
from itertools import combinations
while True:
    k, *s = list(map(int, input().split()))
    if k == 0: break
    for c in combinations(s, 6):
        print(' '.join(map(str, c)))
    print()


# 완전탐색 풀이
def go(s, i, lotto):
    if len(lotto)==6:
        print(' '.join(map(str, lotto)))
        return
    if i==len(s):
        return
    go(s, i+1, lotto+[s[i]])
    go(s, i+1, lotto)

while True:
    k,*s=list(map(int, input().split()))
    if k == 0: break
    go(s, 0, [])
    print()

# 입력으로 주어진 로또 배열, 선택할지 말지 결정해야하는 인덱스, 현재까지 포함한 수의 개수
# go(s, i, cnt):

# 1) 정답을 찾은 경우
# cnt == 6
# 2) 불가능한 경우
# i  == len(s)
# 3) 다음 경우 (선택하는 것은 다른 배열을 사용)
# i번째 사용  O : go(s, i+1, cnt + 1)
#             x : go(s, i, cnt)

# 로또 s집합(총 k개) 에서 6개 선택.
# 사전 순 출력.
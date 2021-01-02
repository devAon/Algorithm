cnt = 0
while True:
    L,P,V = map(int, input().split())
    if L+P+V == 0 : break

    result = (V // P) * L
    result += min((V % P), L)
    cnt += 1
    print("Case %d: %d" %(cnt, result))
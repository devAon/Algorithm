import sys
input = lambda: sys.stdin.readline()
N, K = map(int, input().split())
schedule = list(map(int, input().split()))
multitap = []
result = 0
for i in range(K):
    if schedule[i] in multitap:
        continue
    elif len(multitap) < N:
        multitap.append(schedule[i])
        continue
    else:
        a = 0
        for j in range(N):
            try:
                if a < schedule[i+1:].index(multitap[j]):
                    a = schedule[i+1:].index(multitap[j])
                    b = j
            except:
                a = 0
                b = j
                break
        multitap[b] = schedule[i]
        result += 1
print(result)
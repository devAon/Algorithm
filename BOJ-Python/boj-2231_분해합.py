n = int(input())
for i in range(1, n+1):
    d = list(map(int, str(i)))
    answer = i + sum(d)
    if answer == n:
        print(i)
        break
    if answer != n and i == n:
        print(0)
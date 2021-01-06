data = [int(input()) for _ in range(9)]
data.sort()
for i in range(8, -1, -1):
    rest = sum(data)-data[i]-100
    if rest in data:
        data.remove(data[i])
        data.remove(rest)
        break
for n in data:
    print(n)
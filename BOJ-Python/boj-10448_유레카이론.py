k = [n*(n+1)//2 for n in range(1, 46)]
eureka = [0] * 1001
for x in k:
    for y in k:
        for z in k:
            if x+y+z <= 1000:
                eureka[x+y+z] = 1
n = int(input())
for _ in range(n):
    print(eureka[int(input())])
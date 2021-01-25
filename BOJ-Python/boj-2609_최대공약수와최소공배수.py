def gcd1(a,b): # 최대공약수 O(N)
    gcd = 1
    for i in range(2, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def gcd2(a,b): # 유클리드 호제법-재귀 O(logN)
    if b == 0:
        return a
    else:
        return gcd2(b, a%b)

def gcd3(a,b): # 유클리드 호제법-반복문 O(logN)
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a,b): # 최소공배수
    gcd = gcd2(a,b)
    return (a*b)//gcd

a,b = map(int, input().split())
#print(gcd1(a,b))
print(gcd2(a,b))
#print(gcd3(a,b))
print(lcm(a,b))
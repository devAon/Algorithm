def solution(clothes):
    dic =  {}
    for c in clothes:
        if c[1] in dic:
            dic[c[1]] += 1
        else:
            dic[c[1]]= 1
    cnt = 1
    for c in dic.values():
        cnt *= (c+1)
    return cnt-1

if __name__ == '__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))
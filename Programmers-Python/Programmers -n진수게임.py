# big = ["A","B","C","D","E","F"]
# def solution(n, t, m, p):
#     a="0"
#     i=0
#     #for i in range(t*m):
#     while True:
#         if len(a)>=t*m:
#             break
#         b=""
#         j=i
#         while (j):
#             if j%n>9:
#                 b=big[j%n-10]+b
#             else:
#                 b=str(j%n)+b
#             j=j//n
#         a=a+b
#         i=i+1
#     answer = a[p-1::m][:t]
#     return answer


def trans(n, num):
    arr = "0123456789ABCDEF"
    ret = ''
    if num == 0:
        return '0'
    while num > 0:
        ret = arr[num % n] + ret
        num = num // n
    return ret

def solution(n, t, m, p):
    answer = ''
    string = ''
    
    for i in range(t*m):
        string += trans(n, i)
        
    for s in range(p-1, t*m, m):
        answer += string[s]
    return answer


if __name__ == '__main__':
    n = 2 # 진법
    t = 4 # 미리 구할 숫자의 개수
    m = 2 # 게임에 참가하는 인원
    p = 1 # 튜브의 순서
    print(solution(n, t, m, p))
    n = 16  # 진법
    t = 16  # 미리 구할 숫자의 개수
    m = 2  # 게임에 참가하는 인원
    p = 1  # 튜브의 순서
    print(solution(n, t, m, p))
    n = 16  # 진법
    t = 16  # 미리 구할 숫자의 개수
    m = 2  # 게임에 참가하는 인원
    p = 2  # 튜브의 순서
    print(solution(n, t, m, p))

    n = 8  # 진법
    t = 8  # 미리 구할 숫자의 개수
    m = 2  # 게임에 참가하는 인원
    p = 2  # 튜브의 순서
    print(solution(n, t, m, p))
    

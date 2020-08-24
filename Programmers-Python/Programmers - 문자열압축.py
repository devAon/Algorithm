def solution(s):
    answer = len(s)
    
    for i in range(1, (len(s)//2) +1): # 압축 가능한 단위까지
        compressed = "" # 압축된 문자열
        prev = s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if prev == s[j:j+i]:
                cnt += 1
            else:
                compressed += str(cnt)+prev if cnt >= 2 else prev
                prev = s[j:j+i]
                cnt = 1
        compressed += str(cnt)+prev if cnt >= 2 else prev
        answer = min(answer, len(compressed))

    return answer


if __name__ == "__main__":
    s= "aabbaccc"
    print(solution(s))
    s= "ababcdcdababcdcd"
    print(solution(s))
    s= "abcabcdede"
    print(solution(s))
    s= "abcabcabcabcdededededede"
    print(solution(s))
    s= "xababcdcdababcdcd"
    print(solution(s))
# def solution(p):
#     if p=='': return p
#     r=True; c=0
#     for i in range(len(p)):
#         if p[i]=='(': c-=1
#         else: c+=1
#         if c>0: r=False
#         if c==0:
#             if r:
#                 return p[:i+1]+solution(p[i+1:])
#             else:
#                 return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))

# 균형 잡힌 괄호 문자열
def balance(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        elif p[i] == ')':
            cnt -= 1
        if cnt == 0:
            return i

# 올바른 괄호 문자열
def check(p):
    cnt = 0
    for s in p:
        if s == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True
        

def solution(p):
    answer = ''
    if p == answer:
        return answer

    index= balance(p)
    u = p[:index+1]
    v = p[index+1:]
    
    if check(u):
        answer = u + solution(v)
    else:
        answer='('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        temp = ""
        for s in u:
            if s == '(':
                temp += ')'
            else:
                temp += '('
        answer += temp
        
    return answer

if __name__ == '__main__':
    p = ")("
    print(solution(p))
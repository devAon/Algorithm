def solution(N, stages):
    answer = []
    result = []
    length = len(stages)
    
    for i in range(1, N+1):
        cnt = stages.count(i)
        
        if length == 0:
          fail = 0
        else:
          fail = cnt/length
        result.append((i, fail))
        
        length -= cnt
    
    result = sorted(result, key=lambda x : x[1], reverse = True)

    for data in result:
      answer.append(data[0])

    return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]

N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))



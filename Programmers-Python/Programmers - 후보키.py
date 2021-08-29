# def solution(relation):
#     answer_list = list()
#     for i in range(1, 1 << len(relation[0])):
#         tmp_set = set()
#         for j in range(len(relation)):
#             tmp = ''
#             for k in range(len(relation[0])):
#                 if i & (1 << k):
#                     tmp += str(relation[j][k])
#             tmp_set.add(tmp)

#         if len(tmp_set) == len(relation):
#             not_duplicate = True
#             for num in answer_list:
#                 if (num & i) == num:
#                     not_duplicate = False
#                     break
#             if not_duplicate:
#                 answer_list.append(i)
#     return len(answer_list)

from collections import deque
from itertools import combinations

def solution(relation):
    nr = len(relation)
    nc = len(relation[0])
    
    candidates = []
    for i in range(1, nc+1):
        candidates.extend(combinations(range(nc), i))
        
    final=[]
    for keys in candidates:
        temp=[tuple([item[key] for key in keys]) for item in relation]
        if len(set(temp))==nr:
            final.append(keys)
    
    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
    return len(answer)
    

if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))
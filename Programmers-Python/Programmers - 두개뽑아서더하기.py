from itertools import combinations
def solution(numbers):
    answer = []
    p = list(combinations(numbers, 2))
    for a, b in p:
        answer.append(a+b)
    return sorted(list(set(answer)))
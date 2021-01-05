def solution(people, limit):
    people.sort()
    answer = 0
    s, e = 0, len(people)-1
    while s <= e:
        answer += 1
        if people[s]+people[e] <= limit:
            s += 1
        e -= 1
    return answer

if __name__ == '__main__':
    people = [70, 50, 80, 50]
    limit = 100
    solution(people, limit) # 3
def solution(N, time):
    start = 0 # 회의 시작 시간
    cnt = 0 # 회의실 개수
    for t in time:
        if t[0] >= start:
            start = t[1]
            cnt += 1
    return  cnt

if __name__ == '__main__':
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time = sorted(time, key=lambda x : x[0])
    time = sorted(time, key=lambda x : x[1])
    print(time)
    print(solution(N, time))

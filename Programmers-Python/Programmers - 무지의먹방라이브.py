import heapq

def solution(food_times, k):
    answer = 0
    
    if (sum(food_times) <= k):
      return -1
    
    sum_value = 0
    previous = 0
    length = len(food_times)

    # 우선순위큐에 food_times 모두 초기화
    q=  []
    for i in range(length):
      heapq.heappush(q, (food_times[i],i+1))

    while sum_value + ((q[0][0] - previous) * length) <= k:
      now = heapq.heappop(q)[0]
      sum_value += (now - previous)* length
      length -= 1
      previous = now

    result = sorted(q, key=lambda x:x[1])
    answer = result[(k-sum_value)%length][1]
    return answer

# main
food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
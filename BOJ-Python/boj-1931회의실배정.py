import sys
input = lambda : sys.stdin.readline()

def greedy(meeting):
  cnt = 0
  start = 0
  for time in meeting:
    if time[0] >= start: # 시작시간이 끝나는 시간보다 크거나 같을 경우
      start = time[1]
      cnt += 1
  return cnt

if __name__ == "__main__":
  n = int(input())
  meeting = []
  for i in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))
  
  meeting = sorted(meeting, key=lambda time: time[0])
  meeting = sorted(meeting, key=lambda time: time[1])
  print(greedy(meeting))
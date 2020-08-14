import sys
input = lambda: sys.stdin.readline()

def greedy(employee):
  cnt = 0
  standard = n+1
  for score in employee:
    if standard > score[1]:
      cnt += 1
      standard = score[1]
  return cnt

if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n = int(input())
    employee = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x:x[0])
    print(greedy(employee))
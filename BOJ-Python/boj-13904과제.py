import sys
input = lambda : sys.stdin.readline()

def greedy(assignment):
  score = [0] * 1001
  for d, w in assignment:
    for  i in range(d, 0, -1):
      if not score[i] : 
        score[i] = w
        break
  return sum(score)

if __name__ == "__main__":
  n = int(input())
  assignment = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x:-x[1])
  print(greedy(assignment))
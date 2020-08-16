import sys
input = lambda : sys.stdin.readline()

def binarySearch(n):
  start, end = 1, n
  while start <= end:
    mid = (start+end) // 2
    value = mid * (mid+1)
    if value > n*2:
      end = mid - 1
    else:
      start = mid + 1
  value = mid * (mid+1)
  if value > n*2: 
    mid -= 1
  return mid

if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n = int(input())
    print(binarySearch(n))
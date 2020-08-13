# 틀렸습니다 . . :(

# import sys
# input = lambda: sys.stdin.readline()
# def binarySearch(budget):
#   start, end = 0, max(budget)
#   if sum(budget) <= m:
#     print(end)
#   else:
#     while start <= end:
#       tot = 0
#       mid = (start+end)//2
#       for money in budget:
#           tot += min(money, mid)
#       if tot > m :
#         end = mid - 1
#       else:
#         start = mid + 1
#     print(mid)
# if __name__ == "__main__":
#   n = int(input())
#   budget = list(map(int, input().split()))
#   m = int(input())
#   binarySearch(budget)



# 맞았습니다
import sys
input = lambda: sys.stdin.readline()
def binarySearch(budget):
  start, end = 0, max(budget)
  result = 0

  if sum(budget) <= m:
    return end
  else:
    while start <= end:
      mid = (start + end) //2
      temp = [money if money < mid else mid for money in budget]
      if sum(temp) > m:
        end = mid - 1
      else:
        result = mid
        start = mid + 1
    return result

if __name__ == "__main__":
  n = int(input())
  budget = list(map(int, input().split()))
  m = int(input())
  print(binarySearch(budget))
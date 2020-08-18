data = input()
data = sorted(data)

total = 0
result = ''
for s in data:
  if s.isdigit():
    total += int(s)
  else:
    result += s
result += str(total)
print(result)

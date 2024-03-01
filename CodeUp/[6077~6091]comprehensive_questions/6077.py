num = int(input())
n = 0

for i in range(num+1):
  if(i % 2 == 0):
    n = n+i
  else:
    continue

print(n)
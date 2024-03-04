num = int(input())
sum = 0
n = 0

if(0 <= num <= 1000):
  while(sum < num):
    n = n+1
    sum = sum + n
  print(n)
else:
 exit()


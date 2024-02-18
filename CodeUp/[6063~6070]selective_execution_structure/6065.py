a, b, c = map(int, input().split())
list = [a, b, c]
for i in list:
  if (i % 2 == 0):  # 나머지 연산자
    print(i)

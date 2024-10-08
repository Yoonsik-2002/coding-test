num = int(input())

for i in range(1, num + 1):
  # 1부터 num + 1까지 1씩 증가하며 반복, python의 for문은 range(start, stop, step) 형식으로 인자를 지정할 수 있으며, for i in range(1, num + 1)과 같이 step 인자를 따로 명시하지 않고 생략한 경우, 기본적으로 1씩 증가한다.

  if (i % 10 == 3):
    print('X', end=' ')
  elif (i % 10 == 6):
    print('X', end=' ')
  elif (i % 10 == 9):
    print('X', end=' ')
  else:
    print(i, end=' ')

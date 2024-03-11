n = int(input(), 16)  # 16진수 형식의 입력을 받아와, 10진수로 변환하여, 변수 n에 저장

if (n < 10 & n > 15):
  exit()
else:
  for i in range(1, 16):
    print('%X' % n, '*%X=' % i, '%X' % (n * i), sep='')

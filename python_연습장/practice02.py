n = int(input(), 16)  # 입력된 16진수값을 10진수로 변환하여 변수 n에 저장

if (n < 10 & n > 15):
  exit()
else:
  for i in range(1, 16):
    print('%X' % n, '*%X=' % i, '%X' % (n * i),
          sep='')  #,을 기준으로 한 각 요소를 구분자 없이 이어서 출력

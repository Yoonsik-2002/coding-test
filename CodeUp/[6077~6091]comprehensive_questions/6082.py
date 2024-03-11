# 1부터, 입력받은 숫자까지의 숫자들의 값의 일의 자리 수, 십의 자리수 하나하나 비교하는 방식으로 구현한 369마스터 프로그램
# num = int(input())
# is_3_6_9 = True

# for i in range(1, num+1):
#     for j in range(0, len(str(i))):
#         if(str(i)[j] == '3'):
#             is_3_6_9 = True
#         elif(str(i)[j] == '6'):
#             is_3_6_9 = True
#         elif(str(i)[j] == '9'):
#             is_3_6_9 = True
#         else:
#             is_3_6_9 = False
#     if(is_3_6_9 == True):
#         print('X', end = ' ')
#     else:
#         print(i, end = ' ')

# 숫자에 규칙을 부여하여, 더욱 간결하게 구현한 369마스터 프로그램
num = int(input())

for i in range(1, num + 1):
  if (i % 10 == 3):
    print('X', end=' ')
  elif (i % 10 == 6):
    print('X', end=' ')
  elif (i % 10 == 9):
    print('X', end=' ')
  else:
    print(i, end=' ')

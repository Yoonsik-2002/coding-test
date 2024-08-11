# 테스트 케이스의 개수 입력
T = int(input())
money = [24, 10, 5, 1]

for _ in range(T):
    C = int(input())

    for i in range(len(money)):
        print(C // money[i], end=' ')
        C = C % money[i]
    print()

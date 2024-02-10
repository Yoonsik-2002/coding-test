num1, num2 = map(int, input().split())
print(bool(bool(num1 and not num2) or bool(not num1 and num2)))
"""
num1, num2 = map(int, input().split())
num1 = bool(num1)
num2 = bool(num2)

print((num1 and (not num2)) or ((not num1) and num2))
"""

# 이와같이, 참, 거짓이 서로 다를 때에만 True로 계산하는 논리연산을 XOR(exclusive of, 배타적 논리합) 연산이라고 한다.

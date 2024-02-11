num1, num2 = map(int, input().split())
num1 = bool(num1)
num2 = bool(num2)
print((num1 and num2) or (not num1 and not num2))

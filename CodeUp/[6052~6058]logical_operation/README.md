# [코드업 100제] 논리연산 - 6052
[문제 링크](https://codeup.kr/problem.php?id=6052)<br>

정수값이 입력 되었을 때, `True`/`False`로 평가해주는 프로그램<br>

`bool()`함수를 이용하면, 입력된 식이나 값을 평가해 불(boolean) 형의 값(`True` 혹은 `False`)를 반환해준다. python에서 정수값 `0`은 `False`로 평가되고, 그 외의 값들은 모두 `True`로 평가된다.<br>

![스크린샷(1)](https://github.com/Yoonsik-2002/coding-test/assets/83572199/2e590a08-5704-491e-a371-44d4d6e4f123)<br>

---

<br><br>

# [코드업 100제] 논리연산 - 6053
[문제 링크](https://codeup.kr/problem.php?id=6053)<br>

정수값이 입력 되었을 때, 그 `boolean`값을 반대로 출력하는 프로그램<br>

- ###### `not`예약어
  참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서 `not`예약어를 사용할 수 있다. 이러한 논리연산을 NOT연산이라 부르기도 한다.<br>

  이러한 `not`예약어를 `boolean`값이나 변수에 붙여, `not True`, `not False`, `not 변수`와 같은 계산을 하는 것이 가능하다.<br>

- ###### `boolean`값을 다루어 주는 예약어
  참, 거짓의 논리값인 `bool`값을 다루어주는 예약어로는 `not`, `or`, `and`가 있다.<br>
<br>

![스크린샷(2)](https://github.com/Yoonsik-2002/coding-test/assets/83572199/a3ce786c-02d6-42ab-950c-2978cf53aa65)<br>

---

<br><br>

# [코드업 100제] 논리연산 - 6058
[문제 링크](https://codeup.kr/problem.php?id=6058)<br>

2개의 정수값이 입력될 때, 그 `boolean`값이 모두 `False`일 때에만 `True`를 출력하는 프로그램<br>

해당 프로그램을 작성해 보면, 아래와 같이 작성하는 것이 가능하다.<br>

```python
num1, num2 = map(int, input().split())
num1 = bool(num1)
num2 = bool(num2)
print(not num1 and not num2)  # print(not(num1 or num2))
```

이때, 주석의 `print(not(num1 or num2))`를 한번 보도록 하자.<br>

- ###### 예약어 `or`이 `True`를 반환하는 경우
  예약어 `or`은 둘 중의 하나라도 `True`이거나, 둘 다 `True`인 경우, `True`를 반환한다. 해당 코드의 경우, `not()`에 의해, 그 반대인 `False`가 반환되게 된다.<br>

- ###### 예약어 `or`이 `False`를 반환하는 경우
  또, 예약어 `or`은 둘 다 `False`인 경우엔 `False`를 반환한다. 마찬가지로, 해당 코드의 경우, `not()`에 의해, 그 반대인 `True`가 반환되게 된다.<br>

  즉, 두 값이 모두 `False`일 때, `True`를 반환하게 되는 것이다.<br>
  그러므로, `print(not num1 and not num2)`를 대신해서 사용하는 것이 가능하게 된다.<br>

---

<br><br>

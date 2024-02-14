# [코드업 100제] 비트단위 논리연산 - 5069
[문제 링크](https://codeup.kr/problem.php?id=6059)

입력된 정수를 비트단위로 참/거짓을 바꾼후 정수로 출력하기<br>

- ###### 비트단위(bit-wise) 연산자의 종류
  `~` (bitwise not), `&` (bitwise and), `|` (bitwise or), `^` (bitwise xor),<br>
  `<<`(bitwise left), `>>` (bitwise right)<br>
<br><br>

컴퓨터에 저장되는 모든 데이터들은 2진수 형태로 바뀌어 저장된다. <br>

즉, 0과 1로만 구성되는 비트 단위들로 변환되어 저장되는데, 양의 정수는 2진수 형태로 바뀌어 저장되고, 음의 정수는 **'2의 보수 표현'** 방법으로 저장된다.<br>

- ###### python에서 2의 보수 표현법을 사용하여 5를 -5로 표현하는 과정
  1) 5를 이진수로 표현한다.
     5를 (4비트)이진수로 표현하면, `0101`로 표현하는 것이 가능하다.<br>
  2) 모든 비트를 반전시킨다.
     `0101`의 모든 비트를 반전시키면 `1010`이 된다.<br>
  3) 1을 더하여 준다.
     `1010`에 1을 이진수로 변환한 `0001`을 더하여 준다. 해당 계산의 결과는 `1011`이 된다.<br>
<br><br>

이러한 **'2의 보수 표현법'** 은 음수를 표현하기 위한 효율적인 방법으로, 이 방법은 컴퓨터에서 음수의 표현과 연산을 간편하게 처리할 수 있도록 도와준다. 2의 보수 표현법을 사용하는 이유는 다음과 같다.<br>

- ###### 1) 음수의 효율적 표현 -
   2의 보수 표현법을 사용하면, 음수를 양의 보수로 표현하는 것이 가능하다. 음수를 표현하기 위해 별도의 비트를 사용하지 않고, 양수와 동일한 비트로 표현하는 것이 가능한 것이다. **이는 메모리 공간을 절약하고, 효율적인 데이터 저장을 가능하게 만들어준다.** <br>

- ###### 2) 통일된 덧셈과 뺄셈처리 -
   2의 보수 표현법은 음수를 더하는 방식으로 뺄셈을 수행할 수 있는 장점이 있다.<br>

  즉, 덧셈과 뺄셈을 동일한 연산(더하기)을 사용하여 수행하기 때문에, 코드 작성이 간편해지고, 덧셈과 뺄셈을 통합적으로 다룰 수 있어, 오버플로우 문제 또한 피할 수 있다. (양수와 음수를 동일한 비트 수로 표현하기 때문)<br>

  예를 들어 설명하면, 다음과 같다. 먼저, 2의 보수 표현법에서 음수값을 표현하기 위해, 양수의 양수의 보수를 사용한다. 양수의 보수는 해당 양수값을 이진수로 변환한 뒤, 이를 반전시킨 값으로 표현된다.<br>

  이때, 이렇게 만들어진 양수의 보수(반전시킨 값)에 1을 더해주면, 음수값을 얻는 것이 가능하다.<br>
  <br>
   
  8비트로 표현된 숫자에서, -3을 양수의 보수를 사용하여 표현해 보도록 하겠다.<br>

  1) 먼저, 3을 8비트 이진수로 표현하면, `00000011`로 표현하는 것이 가능하다.
  2) 이제, -3을 표현하기 위해, 먼저 양수의 보수 개념을사용해 보도록 하겠다. 양수의 보수는 해당 양수값(`00000011`)을 반전시킨 값으로 표현하는 것이 가능하다.
      즉, `00000011`반전시킨 `11111100`이 3의 양의 보수가 되겠다.<br>
  3) 마지막으로, 이렇게 만들어진 양수의 보수에 1을 더해줌으로써, 음수값을 얻을 수 있다. `11111100`에 1을 8비트 2진수로 나타낸 `00000001`을 더해주면, `11111101`이 된다.
  <br>

  결과적으로, -3은 2의 보수로 표현할 경우, `11111101`이 된다. 이제, 뺄셈을 수행해 보면, `5-3`을 계산한다고 가정 하였을 시, `00000101`과 `11111101`을 더해주면 된다.<br>

  `000000101 + 11111101 = 00000010`으로, 해당 계산의 결과는 `00000010`이 된다.<br>

  이렇게 2의 보수 표현법을 사용하면, 음수를 더하는 방식으로 뺄셈을 수행할 수 있다. 이는 뺄셈 연산을 덧셈연산으로 대체할 수 있어, 컴퓨터에서 뺄셈을 보다, 간편하게 처리할 수 있는 장점을 제공하여준다.<br>
# [코드업 100제] 출력 - 6001
[문제 링크](https://codeup.kr/problem.php?id=6001)

python에서는 일반적으로, 명령어의 끝에 세미콜론(`;`)을 붙이지 않는다. **파이썬은 줄바꿈을 기준으로 문장을 구분하므로, 세미콜론을 사용하여 명령어를 구분하는 것은 선택사항이다.**<br>

python에서 세미콜론을 사용하는 경우, 아래와 같이, 한 줄에 여러개의 명령어를 작성하는 것이 가능하다.<br>

![스크린샷(1)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/72d323f8-a36c-442e-b01a-267a8c166fc0)<br>

---

<br><br>

# [코드업 100제] 출력 - 6002
[문제 링크](https://codeup.kr/problem.php?id=6002)

python에서 문장 사이에 공백을 포함하여 출력을 하고자 하는 경우, 아래와 같은 방법들을 사용하는 것이 가능하다.<br>

![스크린샷(3)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/ac5913bb-44d3-4662-8683-9cfc02116d7c)<br>

---

<br><br>

# [코드업 100제] 출력 - 6004
[문제 링크](https://codeup.kr/problem.php?id=6004)

python에서 문자열을 만드는 방법은 다양하다. 아래 정리를 한번 보도록 하자.<br>

- ##### 1) 작은 따옴표로 만들기
  ![298273862-6e3d07ff-c9bb-40e7-879f-d883eb935e3f](https://github.com/Yoonsik-2002/conding-test/assets/83572199/5da19d7f-64b4-4cd0-aabc-7ff94a71a23c)

- ##### 2) 큰 따옴표로 만들기
  ![스크린샷(5)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/f8ff437d-7010-4ecf-be84-80e7e0d60e59)

- ##### 3) 문자열에 작은 따옴표 넣기
  ![스크린샷(5)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/6a400fd9-1272-429a-85e8-2508ffc7efe1)

- ##### 4) 문자열에 큰 따옴표 넣기
  ![스크린샷(5)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/45e7dedf-fb2e-405f-956c-f267ccb060c6)<br>

---

<br><br>

# [코드업 100제] 출력 - 6007
[문제 링크](https://codeup.kr/problem.php?id=6007)

이스케이프 문자는 역슬래시(`\`)기호와 함께 조합하여 사용하는 문자를 의미한다.<br>

아래 코드를 한번 봐 보자. 아래 코드에서 에러가 발생하는 이유는 무엇일까?<br>

![스크린샷(6)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/d4a1f40d-5d1d-448b-910c-ed11d725c953)<br>

위 코드를 자세히 보면, 빈 문자열`""`과 문자열`" 라고 말했다."`가 연속적으로 나열되어 있다는 것을 알 수 있다. python에서는 이러한 자료<br>
(문자열)와 자료(문자열)의 단순한 나열을 허용하지 않는다.<br>

이와 같은 에러가 발생하지 않도록 하기 위해서는, 위에서 언급한 이스케이프 문자를 사용해 주어야 한다.<br>
<br>

역슬래시와 큰 따옴표를 조합한 이스케이프 문자(`\"`)를 사용하여, 해당 에러를 해결해 보았다. 아래 코드를 한번 봐 보자.<br>

![스크린샷(7)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/f35b7902-cba9-4890-973d-ff9665967201)<br>

위 코드의 경우, `\"안녕하세요\" 라고 말했다.` 라는 문자열을 둘러싸고 있는 양 끝의 큰 따옴표는 문자열을 만드는 기호로 쓰이게 되고, 이스케이프 문자 따옴표 `\"`는 문자열 내에 그대로 표시되는 단순한 따옴표로 쓰이게 된다.<br>

이스케이프 문자는 위 코드에서 사용한 `\"`말고도 다양한 종류가 존재한다. 아래 정리를 한번 참고하도록 하자.<br>
<br>

#### [다양한 이스케이프 문자]
- **`\n`** - 줄바꿈 (`\n`을 그대로 출력하고자 하는 경우 -> `\\n`)
-  **`\t`** - 탭(Tab)
-  **`\\`** - 역슬래시(`\`)

```python
# "C:\Download\'Hello'.py"의 출력

print("\"C:\\Download\\'Hello'.py\"")
# print("\"C:\\Download\\\'Hello\'.py\"")
```
<br>

![스크린샷(9)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/0eb67de8-d635-4d32-85f0-0aee622c554c)<br>

---
<br><br>

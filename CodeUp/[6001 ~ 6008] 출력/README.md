# [코드업 100제] 출력 - 6001
[문제 링크](https://codeup.kr/problem.php?id=6001)

python에서는 일반적으로, 명령어의 끝에 세미콜론(`;`)을 붙이지 않는다. **파이썬은 줄바꿈을 기준으로 문장을 구분하므로, 세미콜론을 사용하여 명령어를 구분하는 것은 선택사항이다.**<br>

python에서 세미콜론을 사용하는 경우, 아래와 같이, 한 줄에 여러개의 명령어를 작성하는 것이 가능하다.<br>

![스크린샷(1)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/72d323f8-a36c-442e-b01a-267a8c166fc0)<br>
<br>

---

<br><br>

# [코드업 100제] 출력 - 6002
[문제 링크](https://codeup.kr/problem.php?id=6002)

python에서 문장 사이에 공백을 포함하여 출력을 하고자 하는 경우, 아래와 같은 방법들을 사용하는 것이 가능하다.<br>

![스크린샷(3)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/ac5913bb-44d3-4662-8683-9cfc02116d7c)<br>
<br>

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
  ![스크린샷(5)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/45e7dedf-fb2e-405f-956c-f267ccb060c6)
<br>

---

<br><br>

# [코드업 100제] 출력 - 6007
[문제 링크](https://codeup.kr/problem.php?id=6007)

이스케이프 문자는 역슬래시(`\`)기호와 함께 조합하여 사용하는 문자를 의미한다.<br>

아래 코드를 한번 보자.<br>

![스크린샷(6)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/f08284f7-9666-4d33-ba68-bd4bc535ea23)<br>

에러가 발생하는 이유는 위 코드를 자세히 보면 알 수 있다. 빈 문자열`""`과 `"라고 말했습니다"`라는 문자열이 연속적으로 나열되어있는데, python에서는 이러한 자료(문자열)와 자료(문자열)의 단순한 나열을 허용하지 않는다.<br>
<br>

따라서, 이러한 에러가 발생하지 않도록 만들어주기 위해서는 아래와 같이 역슬래시(`\`)를 활용한 이스케이프 문자를 사용해 주어야 한다.<br>

![스크린샷(7)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/b6464250-cb2a-4296-9e1b-4066ef2e0e52)<br>

위 코드의 경우는, 큰따옴표를 통해 만들어진 문자열(자료)의 단순한 나열로 인해 발생하는 에러를 해결하기 위해 역슬래시와 큰 따옴표를 조합한 이스케이프 문자를 활용하였다.<br>

이스케이프 문자의 종류는 위 코드에서 사용한 것 말고도, 다양한 종류가 존재한다.<br>

#### [다양한 이스케이프 문자]
- **`\n`** - 줄바꿈(`\n`을 그대로 출력하고 싶은 경우 -> `\\n`)
- **`\+`** - 탭(Tab)
- **`\\`** - 역슬래시
<br>

```python
# "C:\Download\'Hello'.py" 의 출력
print("\"C:\\Download\\\'Hello\'.py\"")
```
<br>

![스크린샷(8)](https://github.com/Yoonsik-2002/conding-test/assets/83572199/b51e9bdf-5a62-47cd-b03a-23123608fee6)<br>
<br>

---

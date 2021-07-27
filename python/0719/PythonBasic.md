# [Python 기초]

## Python 개발 환경

### Python 특징

##### ⋅ 인터프리터 언어 (Interpreter)

  ⋅ 소스 코드를 컴파일하지 않고, 한 줄씩 소스코드를 읽어서 바로 실행  
  ⋅ 컴파일 언어에 비해 느릴 수 있지만 빌드 과정이 없이 바로 실행 가능함

##### ⋅ 객체 지향 프로그래밍 (Object Oriented Programming)

  ⋅ 파이썬은 모두 객체로 이루어져 있음

##### ⋅ 동적 타이핑 (Dynamic Typing)

  ⋅ 변수에 별도의 타입 지정이 필요 없음

### Python 개발 환경

##### ⋅ 대화형 환경

  ⋅ Python 기본 Interpreter  
  ⋅ Python Jupyter Notebook

##### ⋅ 스크립트 실행

  ⋅ .py 파일을 작성하고 IDE 혹은 Text editor 활용

### Python Interpreter / IDLE

##### ⋅ 인터프리터가 대화형 모드로 동작

  ⋅ 프롬프트(>>>)에 코드를 작성하면 해당 코드가 실행됨  
  ⋅ 여러 줄의 코드가 작성되는 경우 보조 프롬프트(...)가 사용됨

> Python이 설치된 환경에서는 기본적으로 활용 가능하나 디버깅 및 코드 편집, 반복 실행이 어려움

![image-20210727133937481](PythonBasic.assets/image-20210727133937481.png)

### Python Jupyter Lab

##### ⋅ 웹 브라우저 환경에서 코드를 작성할 수 있는 오픈소스

  ⋅ Syntax Highlighting, Indentation, Tab completion 등 편의 기능 제공함  
  ⋅ 브라우저에서 코드를 실행하고 결과를 확인할 수 있음  
  ⋅ HTML, LaTeX, PNG, SVG을 바탕으로 다양한 표현이 가능함  
  ⋅ Markdown을 기반으로 문서를 작성할 수 있음

> 데이터분석/머신러닝/딥러닝 시 많이 활용 가능하며, Google colab 등 유사한 환경의 서비스들도 있음



## Python 기초 문법

### 코드 스타일 가이드

##### ⋅ 코드를 '어떻게 작성할지'에 대한 가이드라인

  ⋅ PEP8 (https://www.python.org/dev/peps/pep-0008/)  - 파이썬에서 제안하는 스타일 가이드  
  ⋅ Google Style guide (https://google.github.io/styleguide/pyguide.html) 등 기업, 오픈소스 등에서 사용

### 주석(Comment)

##### ⋅ 한 줄 주석은 #으로 표현

```python
# 주석(comment)입니다.

# print('hello')
print('world')
```

> world

##### ⋅ 특수한 형태의 주석 'docstring'

  ⋅ 함수/클래스의 설명을 작성

```python
def foo():
	"""이 함수는 foo입니다.
	docstring으로 함수나 클래스의 기능을 설명합니다."""
```

### 코드 라인

##### ⋅ 코드는 1줄에 1문장(statement)이 원칙

##### ⋅ 문장(statement)은 파이썬이 실행 가능(executable)한 최소한의 코드 단위

  ⋅ 기본적으로 파이썬에서는 세미콜론(;)을 작성하지 않음  
  ⋅ 한 줄로 표기할 때는 세미콜론(;)를 작성하여 표기할 수 있음

```python
print('hello')
print('world')
```

> hello  
> world

```python
print('hello')print('world')
```

> SyntaxError: invalid syntax

```python
print('hello');print('world')
```

> hello  
> world



## 변수와 식별자

### 변수

##### ⋅ 변수는 할당 연산자(=)를 통해 값을 할당 (assignment)

##### ⋅ type() : 변수에 할당된 값의 타입

##### ⋅ id() : 변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리 주소

```python
x = 'world'
type(x)
id(x)
```

> str  
> 4645387184

### 할당 연산자(=)

##### ⋅ 같은 값을 동시에 할당할 수 있음

```python
x = y = 1004
print(x, y)
```

> 1004  1004

##### ⋅ 다른 값을 동시에 할당할 수 있음 (multiple assignment)

```python
x, y = 1, 2
print(x, y)
```

> 1  2

```python
x, y = 1
```

> TypeError: cannot unpack non-iterable int object

```python
x, y = 1, 2, 3
```

> ValueError: too many values to unpack (expected 2)

### 값 swap

##### ⋅ x = 10, y = 20 일 때, 각각 값을 바꿔서 저장하는 코드

```python
x, y = 10, 20
```

```python
# 1. 임시 변수 활용
tmp = x
x = y
y = tmp
print(x, y)
```

> 20  10

```python
# 2. Pythonic
y, x = x, y
print(x, y)
```

> 20  10

### 식별자 (identifiers)

##### ⋅ 변수, 함수, 모듈, 클래스 등을 식별하는데 사용하는 이름(name)

##### ⋅ 규칙

> ⋅ 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성  
> ⋅ 첫 글자에 숫자가 올 수 없음  
> ⋅ 길이제한이 없고, 대소문자를 구별  
> ⋅ 다음의 키워드(keywords)는 예약어(reserved words)로 사용할 수 없음

```
False, None, True, and, as, assert, async, await, break, class, continue,
def, del, elif, else, except, finally, for, from, global, if, import, in,
is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

##### ⋅ 내장함수나 모듈 등의 이름으로도 만들면 안됨

```python
print(5)
print = 'hi'
print(5)
```

> TypeError: 'str' object is not callable

 →  식별자(변수명)가 print인 문자열 hi로 활용됨



## 데이터 타입

### 숫자 (int)

##### ⋅ 모든 정수의 타입은 int

  ⋅ Python 3부터는 long 타입은 없고, 모두 int로 표기  
  ⋅ 여타 프로그래밍 언어, Python 2에서는 OS기준 32/64비트

##### ⋅ 매우 큰 수를 나타낼 때 오버플로가 발생하지 않음

  ⋅ 오버플로(overflow) : 데이터 타입별로 사용할 수 있는 메모리의 크기를 넘어서는 상황  
  ⋅ Arbitrary precision arithmetic(임의 정밀도 산술)을 통해 고정된 형태의 메모리가 아닌 가용 메모리들을 활용하여 모든 수 표현에 활용

```python
import sys
print(sys.maxsize)
```

> 9223372036854775807

```python
print(2 ** 63 - 1)
```

> 9223372036854775807

```python
print(sys.maxsize ** 10)
```

> 4455508415646675013373597242420117818453694838130159772560668808816707086990958982033203334310070688731662890013605553436739351074980172000127431349940128178077122187317837794167991459381249

```python
print(type(sys.maxsize ** 10))
```

> <class 'int'>

##### ⋅ 진수 표현

  ⋅ 2진수 : 0b  
  ⋅ 8진수 : 0o  
  ⋅ 16진수 : 0x

```python
print(0b10)
print(0o30)
print(0x10)
```

> 2  
> 24  
> 16

### 숫자 (float)

##### ⋅ 정수가 아닌 모든 실수는 float 타입

```python
print(11/2)
print(type(10/3))
```

> 5.5  
> <class 'float'>

##### ⋅ 부동소수점

  ⋅ 실수를 컴퓨터가 표현하는 방법 - 2진수(비트)로 숫자를 표현  
  ⋅ 이 과정에서 floating point rounding error가 발생하여, 예상치 못한 결과가 발생

```python
print(10**100/3)
```

> 3.333333333333333e+99

```python
print(1/-10**100)
```

> -1e-100

```python
print(1e-1)
print(type(1e-1))
```

> 0.1  
> <class 'float'>

### Floating point rounding error

##### ⋅ 부동소수점에서 실수 연산 과정에서 발생 가능

  ⋅ 값 비교하는 과정에서 정수가 아닌 실수인 경우 주의할 것

```python
# 왼쪽의 계산 결과와 오른쪽 값은 같은 값일까요?
print(3.14 - 3.02 == 0.12)
```

> False

```python
print(3.14 - 3.02)
```

> 0.1200000000000001

  ⋅ 매우 작은 수보다 작은지를 확인하거나 math 모듈 활용

```python
# 1. 임의의 작은 수
print(abs(a - b) <= 1e-10)
```

> True

```python
# 2. system상의 machine epslion
import sys
print(abs(a - b) <= sys.float_info.epsilon)
print(sys.float_info.epsilon)
```

> True  
> 2.220446049250313e-16

```python
# 3. Python 3.5이상
import math
math.isclose(a, b)
```

> True

### 숫자 (complex)

##### ⋅ 실수부와 허수부로 구성된 복소수는 모두 complex 타입

  ⋅ 허수부를 j로 표현

```python
a = 3+4j
print(type(a))
```

> <class 'complex'>

```python
a.real
a.imag
```

> 3.0  
> 4.0

### 문자열 (String)

##### ⋅ 모든 문자는 str 타입

```python
print('hello')
print(type('hello'))
```

> hello  
> <class 'str'>

##### ⋅ 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기

  ⋅ 문자열을 묶을 때 동일한 문장부호를 활용  
  ⋅ PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록함

```python
print('철수 "안녕"')
print("철수 '안녕'")
```

> 철수 "안녕"  
> 철수 '안녕'

### 이스케이프 시퀀스 (escape sequence)

##### ⋅ 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(\\)를 활용하여 구분

| 예약문자 |   내용 (의미)   |
| :------: | :-------------: |
|    \n    |     줄 바꿈     |
|    \t    |       탭        |
|    \r    |   캐리지리턴    |
|    \0    |    널(Null)     |
|   \\\\   |        \        |
|   \\'    | 단일인용부호(') |
|   \\"    | 이중인용부호(") |

```python
print('철수 \'안녕\'')
```

> 철수  '안녕'

```python
print('이 다음은 엔터.\n그리고 탭\t탭')
```

> 이  다음은  엔터.  
> 그리고  탭  탭

### String Interpolation

##### ⋅ 문자열을 변수를 활용하여 만드는 법

```python
# 1. %-formatting
print('Hello, %s' % name)
print('내 성적은 %d' % score)
print('내 성적은 %f' % score)
```

> Hello, Kim  
> 내 성적은 4  
> 내 성적은 4.500000

```python
# 2. str.format()
print('Hello, {}! 성적은 {}'.format(name, score))
```

> Hello, Kim!  성적은 4.5

```python
# 3. f-strings : python 3.6+
print(f'Hello, {name}! 성적은 {score}')
```

> Hello, Kim!  성적은 4.5

##### ⋅ f-string 사용 예

```python
import datetime
today = datetime.datetime.now()
print(today)
```

> 2021-06-24  15:01:21.704852

```python
f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일'
```

> '오늘은  21년  06월  24일'

```python
pi = 3.141592
f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2*2}'
```

> '원주율은 3.14. 반지름이 2일때 원의 넓이는 12.566368'

### 참/거짓 Boolean

##### ⋅ True/False 값을 가진 타입은 bool

##### ⋅ 비교/논리 연산을 수행함에 있어서 활용됨

##### ⋅ 다음은 모두 False로 변환

```
⋅ 0, 0.0, (), [], {}, '', None
```

##### ⋅ 값이 없음을 표현하기 위한 타입인 NoneType

```python
print(type(None))
```

> <class 'NoneType'>

```python
a = None
print(a)
```

> None



## 타입 변환

### 자료형 변환/타입 변환 (Type conversion, Typecasting)

##### ⋅ 파이썬에서 데이터타입은 서로 변환할 수 있음

  ⋅ 암시적 타입 변환 (Implicit) : 사용자가 의도하지 않고, 파이썬 내부적으로 타입 변환 하는 경우  
  ⋅ 명시적 타입 변환 (Explicit) : 사용자가 특정 함수를 활용하여 의도적으로 타입 변환 하는 경우

### 암시적 타입 변환

##### ⋅ bool

```python
True + 3
```

> 4

##### ⋅ Numbers (int, float, complex)

```python
3 + 5.0
```

> 8.0

```python
3 + 4j + 5
```

> (8+4j)

### 명시적 타입 변환

##### ⋅ int

  ⋅ str, float (str은 형식에 맞는 문자열만 정수로 변환 가능)

```python
'3' + 4
```

> TypeError: can only concatenate str (not "int") to str

```python
int('3') + 4
```

> 7

```python
int('3.5') + 5
```

> ValueError: invalid literal for int() with base 10: '3.5'

##### ⋅ float

  ⋅ str, int (str은 형식에 맞는 문자열만 변환 가능)

```python
'3.5' + 3.5
```

> TypeError: can only concatenate str (not "float") to str

```python
float('3')
```

> 3.0

```python
float('3/4') + 5.3
```

> ValueError: could not convert string to float: '3/4'

##### ⋅ str

  ⋅ int, float, list, tuple, dict => str



## 연산자

### 산술 연산자

##### ⋅ 기본적인 사칙연산 및 수식 계산

| 연산자 |   내용   |
| :----: | :------: |
|   +    |   덧셈   |
|   -    |   뺄셈   |
|   *    |   곱셈   |
|   /    |  나눗셈  |
|   //   |    몫    |
|   **   | 거듭제곱 |

```python
print(5 / 2)
print(4 / 2) # 나눗셈은 항상 결과가 float
print(5 // 2)
print(int(5/2))
print(5 % 2)
```

> 2.5  
> 2.0  
> 2  
> 2  
> 1

```python
print(divmod(5, 2)) # divmod는 몫과 나머지를 반환하는 함수
quotient, remainder = divmod(5, 2)
print(quotient, remainder)
```

> (2,  1)  
> 2  1

### 비교 연산자

##### ⋅ 값을 비교하며, True/False 값을 리턴함

| 연산자 |            내용             |
| :----: | :-------------------------: |
|   <    |            미만             |
|   <=   |            이하             |
|   >    |            초과             |
|   >=   |            이상             |
|   ==   |            같음             |
|   !=   |          같지않음           |
|   is   |    객체 아이덴티티(OOP)     |
| is not | 객체 아이덴티티가 아닌 겨우 |

```python
3 > 6
```

> False

```python
3.0 == 3
```

> True

```python
3 >= 0
```

> True

```python
# 특정 변수가 비어 있는지 확인하기 위해서는
# x == None이 아닌 x is None을 쓰는 것을 권장
x = 3
x is None
```

> False

### 논리 연산자

| 연산자  | 내용                           |
| ------- | ------------------------------ |
| A and B | A와 B 모두 True시, True        |
| A or B  | A와 B 모두 False시, False      |
| Not     | True를 False로, False를 True로 |

```python
print(True and True)
print(True and False)
print(True or False)
print(False or False)
```

> True  
> False  
> True  
> False

```python
print(not True)
print(not 0)
print(not 'hi')
```

> False  
> True  
> False

##### ⋅ 일반적으로 비교연산자와 함께 사용됨

```python
num = 100
num >= 100 and num % 3 == 1
```

> True

##### ⋅ 단축평가 : 결과가 확실한 경우 두번째 값은 확인하지 않음

```python
print(3 and 5)
print(0 and 3)
print(5 or 3)
print(0 or 3)
```

> 5  
> 0  
> 5  
> 3

### 복합 연산자

##### ⋅ 복합 연산자는 연산과 대입이 함께 이뤄짐

```python
cnt = 100
cnt += 1
print(cnt)
```

> 101

```python
cnt = 0
while cnt < 3:
	print(cnt)
	cnt += 1
```

> 0  
> 1  
> 2

### Concatenation

##### ⋅ +는 숫자가 아닌 자료형에서도 사용 가능함

```python
'hello, ' + 'world!'
```

> 'hello, world!'

##### ⋅ 특정 요소가 속해 있는지 여부를 확인

```python
'a' in 'apple'
```

> True

### Identity

##### ⋅ is 연산자를 통해 동일한 객체(object)인지 확인 가능함

```python
# 파이썬에서 -5부터 256까지 숫자의 id는 동일
a = 3
b = 3
print(a is b)
print(id(a), id(b))
```

> True  
> 2930693925232  2930693925232

```python
c = 257
d = 257
print(c is d)
print(id(c), id(d))
```

> False  
> 1821933996944  1821933996944

```python
# 특정 변수가 비어 있는지 확인하기 위해서는
# x == None이 아닌 x is None을 쓰는 것을 권장
x = 3
x is None
```

> False

### Indexing / Slicing

##### ⋅ []를 통해 값을 접근하고, [:]를 통해 슬라이싱 가능함

```python
'hello, world!'[0]
```

> 'h'

```python
'hello, world!'[1:5]
```

> 'ello'

### 연산자 우선 순위

##### ⋅ 다음은 주요 연산자의 우선 순위이며, 작성시 유의할 것

> ⋅  ()  
> ⋅  Slicing  
> ⋅  Indexing  
> ⋅  **  
> ⋅  단항 연산자(+, -) : 부호  
> ⋅  산술 연산자(\*, /, %)  
> ⋅  산술 연산자(+, -)  
> ⋅  비교 연산자, in, is  
> ⋅  not  
> ⋅  and  
> ⋅  or

```python
'apple'[3] in 'hello' and -3**3*0 > 4%2
```

> False



## 표현식/문장

### 표현식 (expression)

##### ⋅ 표현식은 평가(evaluate)되고, 값으로 변경

##### ⋅ 하나의 값으로 환원(reduce)될 수 있는 문장

##### ⋅ 식별자, 값, 연산자로 구성

```python
# 하나의 값(value)도 표현식(expression)이 될 수 있음
'hello'
```

> 'hello'

```python
radius = 10
3.14 * (radius - 5) ** 2
```

> 78.5

```python
# 표현식을 만드는 문법(syntax)은 일반적인 (중위표기) 수식의 규칙과 유사
# 아래와 같은 문장은 표현식이 될 수 없음
4 +
```

> SyntaxError: invalid syntax

### 문장 (statement)

##### ⋅ 파이썬이 실행 가능한 최소한의 코드 단위

##### ⋅ 모든 표현식(expression)은 문장(statement)

  ⋅ 표현식이 아닌 문장이 존재 (ex.  del 5)

```python
# 하나의 값(value)도 문장이 될 수 있음
'hello'
```

> 'hello'

```python
# 표현식(expression)도 문장이 될 수 있음
5 * 21 - 4
```

> 101

```python
# 실행 가능(executable)해야 하기 때문에 아래의 코드는 문장이 될 수 없음
name = '
```

> SyntaxError: EOL while scanning string literal


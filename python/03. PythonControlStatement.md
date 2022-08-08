# 제어문 (Control Statement)

> ##### · 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
>
> ##### · 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요
>
> ##### · 제어문은 순서도(flow chart)로 표현이 가능

## 조건문 (Conditional Statement)

### if 문

##### · if 문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

​	· expression에는 참/거짓에 대한 조건식  
​	· 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭을 실행  
​	· 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭을 실행  
​		· else는 선택적으로 활용 가능함

```python
if <expression>:
	# Code block (들여쓰기 주의!)
else:
	# Code block
```

```python
a = 5
if a > 5:
	print('5 초과')
else:
	print('5 이하')
print(a)
```

> 5  이하  
> 5

```python
# 실습 - 변수 num의 값의 홀수/짝수 여부 출력 (num은 input을 통해 입력 받기)
num = int(input('숫자 입력: '))
if num % 2:  # if num % 2 == 1:
	print('홀수입니다.')
else:
	print('짝수입니다.')
```

> [입력]  
> 5
>
> [출력]  
> 홀수입니다.

### if 복수 조건문

##### · 복수의 조건식을 활용할 경우 elif를 활용하여 표현

```python
if <expression>:
	# Code block
elif <expression>:
	# Code block
elif <expression>:
	# Code block
else:
	# Code block
```

```python
# 실습 - 미세먼지 농도 'dust' 값에 따라 등급을 출력
dust = 140

if dust > 150:
	print('매우나쁨')
elif dust > 80:  # '150>= dust > 80' 으로 작성할 필요가 없음
	print('나쁨')
elif dust > 30:
	print('보통')
else:
	print('좋음')
```

> 나쁨

### if 중첩 조건문

##### · 조건문은 다른 조건문에 중첩되어 사용될 수 있음

​	· 들여쓰기를 유의하여 작성할 것

```python
if <expression>:
	# Code block
	if <expression>:
		# Code block
else:
	# Code block
```

```python
# 실습 - 'dust' 값이 300이 넘는 경우와 음수인 경우 추가로 문장을 출력
dust = 500

if dust > 150:
	print('매우나쁨')
	if dust > 300:
		print('실외 활동을 자제하세요.')
elif dust > 80:
	print('나쁨')
elif dust > 30:
	print('보통')
else:
	if dust >= 0:
		print('좋음')
	else:
		print('값이 잘못 되었습니다.')  # 음수인 경우 출력
```

> 매우나쁨  
> 실외 활동을 자제하세요.

### 조건 표현식 (Conditional Expression)

##### · 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용

##### · 삼항 연산자(Ternary Operator)로 부르기도 함

```python
<true인 경우 값> if <expression> else <false인 경우 값>
```

```python
# 실습 - num이 정수일 때 절댓값을 저장
value = num if num >= 0 else -num
```

```python
# 실습 2 - 다음 조건문을 조건 표현식으로 작성

# 조건문
num = 2
if num % 2:
	result = '홀수입니다.'
else:
	result = '짝수입니다.'

# 조건 표현식
result = '홀수입니다.' if num % 2 else '짝수입니다.'
```



## 반복문 (Loop Statement)

### while 문

##### · while문은 조건식이 참인 경우 반복적으로 코드를 실행

​	· 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨  
​	· 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨  
​	· while문은 무한 루프를 하지 않도록 종료조건이 반드시 필요

```python
while <expression>:
	# Code block (들여쓰기 주의!)
```

```python
a = 0
while a < 5:
	print(a)
	a += 1
print('끝')
```

> 0  
> 1  
> 2  
> 3  
> 4  
> 끝

```python
# 실습 - 1부터 사용자가 입력한 양의 정수까지의 총합 출력
n = 0
total = 0
user_input = int(input())

while n <= user_input:
	total += n
	n += 1
print(total)
```

> [입력]  
> 5
>
> [출력]  
> 15

### for 문

##### · for문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable) 요소를 모두 순회함

​	· 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음

```python
for <변수명> in <iterable>:
	# Code block
```

```python
for fruit in ['apple', 'mango', 'banana']:
	print(fruit)
print('끝')
```

> apple  
> mange  
> banana  
> 끝

```python
# 실습 - 사용자가 입력한 문자를 한 글자씩 출력
chars = input()

for char in chars:
	print(char)
```

> [입력]  
> happy
>
> [출력]  
> h  
> a  
> p  
> p  
> y

```python
# 실습 2 - 조건문과 반복문을 활용하여 1~10까지 숫자 중 홀수만 출력
for i in range(1, 11):
	if i % 2:
		print(i)
```

> 1  
> 3  
> 5  
> 7  
> 9  

##### · 리스트 순회하기 - range

​	· 리스트의 길이(n)를 range로 하여 0 ~ n-1까지 숫자를 반복  
​	· 반복문 코드 블록에서 index 값과 리스트에 index  접근을 통해 활용

```python
members = ['민수', '영희', '철수']
```

```python
for i in range(len(members)):
	print(f'{i+1}번 {members[i]}')
```

> 1번  민수  
> 2번  영희  
> 3번  철수

##### · 리스트 순회하기 - enumerate

​	· 내장 함수 enumerate의 경우 (index, value) 형태의 tuple로 구성된 열거 객체를 반환

```python
for idx, member in enumerate(members):
	print(idx, member)
```

> 0  민수  
> 1  영희  
> 2  철수

```python
list(enumerate(members))  # 숫자와 값의 tuple로 생성
```

> [(0,  '민수'),  (1,  '영희'),  (2,  '철수')]

```python
list(enumerate(members, start=1))  # 기본값 0, start를 지정하면 해당 값부터 순차적으로 증가
```

> [(1,  '민수'),  (2,  '영희'),  (3,  '철수')]

### 반복문 제어

##### · break : 반복문을 종료

```python
n = 0
while True:
	if n == 3:
		break
	print(n)
	n += 1
```

> 0  
> 1  
> 2

```python
for i in range(10):
	if i > 1:
		print('0과 1만 필요해!')
		break
	print(i)
```

> 0  
> 1  
> 0과  1만  필요해!

##### · continue : 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

```python
for i in range(6):
	if i % 2 == 0:
		continue
	print(i)
```

> 1  
> 3  
> 5

##### · for - else : 끝까지 반복문을 실행한 이후 else문 실행

​	· break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음

```python
for char in 'apple':
	if char == 'b':
		print('b!')
		break
else:
	print('b가 없습니다.')
```

> b가 없습니다.

```python
for char in 'banana':
	if char == 'b':
		print('b!')
		break
else:
	print('b가 없습니다.')
```

> b!

### pass 문

##### · 아무것도 하지 않음

​	· 특별히 할 일이 없을 때 자리를 채우는 용도로 사용  
​	· 반복문 아니여도 사용 가능

```python
for i in range(5):
	if i == 3:
		pass
	print(i)
```

> 0  
> 1  
> 2  
> 3  
> 4

```python
# continue문 차이
for i in range(5):
	if i == 3:
		continue
	print(i)
```

> 0  
> 1  
> 2  
> 4
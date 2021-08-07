# 데이터 구조 (Data Structures)

> ##### · Algorithms + Data Structures = Programs (Niklaus Wirth, 파스칼 설계자 및 1984년 튜링상 수상자)
>
> ##### · 데이터에 편리하게 접근하고, 변경하기 위해 데이터를 저장하거나 조작하는 법
>
> ##### · 순서가 있는 데이터 구조
>
> > · 문자열(String)  
> > · 리스트(List)
>
> ##### · 순서가 없는 데이터 구조
>
> > · 세트(set)  
> > · 딕셔너리(Dictionary)



## 문자열

> ##### · 문자들의 나열 (sequence of characters)
>
> ##### · 문자열의 특징
>
> > · 변경할 수 없고 (immutable)  
> > · 순서가 있고 (ordered)  
> > · 순회 가능한 (iterable)

##### · Immutable

```python
a = 'my string?'
a[-1] = '!'
```

> TypeError :  'str' object does not support item assignment

##### · Iterable

```python
a = '123'
for char in a:
	print(char)
```

> 1  
> 2  
> 3

### 문자열 인덱스 (Index)

##### · 파이썬에서 문자열은 아래와 같이 접근할 수 있음

> ![image-20210805114100627](PythonDataStructures.assets/image-20210805114100627.png)

### 문자열 자르기 (Slicing)

##### · 파이썬에서 문자열은 아래와 같이 자를 수 있음

![image-20210805114444902](PythonDataStructures.assets/image-20210805114444902.png)

> ##### · s[2 : 5]  =>  'cde'
>
> ##### · s[-6 : -2]  =>  'defg'
>
> ##### · s[2 : -4]  =>  'cde'
>
> ##### · s[2 : 5 : 2]  =>  'ce'
>
> ##### · s[-6 : -1 : 3]  =>  'dg'
>
> ##### · s[2 : 5 : -1]  =>  ''
>
> ##### · s[5 : 2 : -1]  =>  'fed'
>
> ##### · s[ : 3]  =>  'abc'
>
> ##### · s[5 : ]  =>  'fghi'
>
> ##### · s[ : : ]  =>  'abcdefghi'
>
> ​	· s[0 : len(s) : 1]과 동일
>
> ##### · s[ : : -1]  =>  'ihgfedcba'
>
> ​	· s[-1 : -(len(s)+1) : -1]과 동일

### 문자열

##### · 문자들의 나열 (sequence of characters)

##### · 문자열의 특징

> · 변경할 수 없고 (immutable)  
> · 순서가 있고 (ordered)  
> · 순회 가능한 (iterable)

### 문자열 조회/탐색

##### · .find(x)

​	· x의 첫 번째 위치를 반환. 없으면 -1을 반환함

```python
'apple'.find('p')
```

> 1

```python
'apple'.find('k')
```

> -1

##### · .index(x)

​	· x의 첫 번째 위치를 반환. 없으면 오류 발생

```python
'apple'.index('p')
```

> 1

```python
'apple'.index('k')
```

> ValueError :  substring not found

### 문자열 변경

##### · .replace(old, new[ ,count])

​	· 바꿀 대상 글자를 새로운 글자로 바꿔서 반환  
​	· count를 지정하면, 해당 개수만큼만 시행

```python
'coone'.replace('o', 'a')
```

> 'caane'

```python
'wooooowoo'.replace('o', '!', 2)
```

> 'w!!ooowoo'

##### · .strip([chars])

​	· 특정한 문자들을 지정하면 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)

##### · 문자열을 지정하지 않으면 공백을 제거함

```python
'	와우!\n'.strip()
```

> '와우!'

```python
'	와우!\n'.lstrip()
```

> '와우!\n'

```python
'	와우!\n'.rstrip()
```

> '		와우!'

```python
'안녕하세요????'.rstrip('?')
```

> '안녕하세요'

##### · .split([chars])

​	· 문자열을 특정한 단위로 나눠 리스트로 반환

```python
'a,b,c'.split('_')
```

> ['a,b,c']

```python
'a b c'.split()
```

> ['a',  'b',  'c']

##### · 'separator' .join([iterable])

​	· 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환

```python
'!'.join('hello')
```

> ' h ! e ! l ! l ! o'

```python
' '.join(['3', '5'])
```

> '3  5'

### · 대소문자 변경

> ·  .capitalize()  :  앞글자를 대문자로  
> ·  .title()  :  '나 공백 이후를 대문자로  
> ·  .upper()  :  모두 대문자로  
> ·  .lower()  :  모두 소문자로  
> ·  .swapcase()  :  대 <-> 소문자로 변경

```python
msg = 'hI! Everyone, I\\'m hello'
print(msg)
print(msg.capitalize())
print(msg.title())
print(msg.upper())
print(msg.lower())
print(msg.swapcase())
```

> hI!  Everyone,  I'm  hello  
> Hi!  everyone,  i'm  hello  
> Hi!  Everyone,  I'M  Hello  
> HI!  EVERYONE, I'M  HELLO  
> hi!  everyone,  i'm  hello  
> Hi!  eVERYONE,  i'M  HELLO

### 문자열 관련 검증 메소드

> ·  .isalpha()  :  알파벳 문자 여부  ( *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함) )  
> ·  .isupper()  :  대문자 여부  
> ·  .islower()  :  소문자 여부  
> ·  .istitle()  :  타이틀 형식 여부

```python
print('abc'.isalpha())
print('ㄱㄴㄷ'.isalpha())
print('Ab'.isupper())
print('ab'.islower())
print('Title Title!'.istitle())
```

> True  
> True  
> False  
> True  
> True

##### · .isdecimal()  ⊆  .isdigit()  ⊆  .isnumeric()

```python
print('⅜'.isdecimal())
print('⅜'.isdigit())
print('⅜'.isnumeric())
```

> False  
> False  
> True

```python
print('③⑧'.isdecimal())
print('③⑧'.isdigit())
print('③⑧'.isnumeric())
```

> False  
> True  
> True

![image-20210807183943934](PythonDataStructures.assets/image-20210807183943934.png)



## 리스트

> ##### · 순서가 있는 시퀀스, 인덱스로 접근
>
> ##### · 문자열의 특징
>
> > · 변경 가능하고 (mutable)  
> > · 순서가 있고 (ordered)  
> > · 순회 가능한 (iterable)

### 값 추가 및 삭제

##### · .append(x) : 리스트에 값을 추가함

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe)
cafe.append('banapresso')
print(cafe)
```

> [ ' starbucks ' ,  ' tomntoms ' ,  ' hollys ' ]  
> [ ' starbucks ' ,  ' tomntoms ' ,  ' hollys ' ,  ' banapresso ' ]

##### · .extend(iterable) : 리스트에 iterable의 항목을 추가함

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.extend(['coffee'])
print(cafe)
cafe += ['banapresso']
print(cafe)
```

> [ ' starbucks ' ,  ' tomntoms ' ,  ' hollys ' ,  ' coffee ' ]  
> [ ' starbucks ' ,  ' tomntoms ' ,  ' hollys ' ,  ' coffee ' ,  ' banapresso ' ]

```python
# 문자열을 .extend로 추가하는 경우
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.extend('coffee')
print(cafe)
```

> [ ' starbucks ' ,  ' tomntoms ' ,  ' hollys ' ,  ' c ' ,  ' o ' ,  ' f ' ,  ' f ' ,  ' e ' ,  ' e ' ]
>
>   →  문자열 'coffee'의 항목들이 추가됨

##### · .insert(i, x) : 정해진 위치 i에 값을 추가함

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.insert(0, 'start')
print(cafe)
```

> [ ' start ' ,  ' starbucks ' ,  ' tomntoms ' ,  ' hollys ' ]

```
# 리스트 길이보다 큰 경우 맨 뒤에 추가
cafe = ['starbucks', 'tomntoms', 'hollys']

```




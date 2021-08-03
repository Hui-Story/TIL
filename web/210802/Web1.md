# Web 1

## 개발환경 설정

### Visual Studio Code

##### · HTML/CSS 코드 작성을 위한 Visual Studio Code 추천 확장 프로그램

> · Open in browser  /  Live Server  
> · Auto rename tag  
> · Highlight Matching Tag

###  크롬 개발자 도구

##### · 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공

##### · 주요 기능

> ##### · Elements - DOM 탐색 및 CSS 확인 및 변경
>
> ​	· Styles - 요소에 적용된 CSS 확인  
> ​	· Computed - 스타일이 계산된 최종 결과  
> ​	· Event Listeners - 해당 요소에 적용된 이벤트 (JS)
>
> ##### · Sources, Network, Performance, Application, Security, Audits 등

### 현재의 웹 표준

![image-20210803090932430](Web1.assets/image-20210803090932430.png)



## HTML (Hyper Text Markup Language)

> ##### 웹 페이지를 작성하기 위한(구조를 잡기 위한) 언어.  웹 컨텐츠의 의미와 구조를 정의

### Hyper Text

##### · Hyper : 텍스트 등의 정보가 동일 선상에 있는 것이 아니라 다중으로 연결되어 있는 상태

##### · Hyper Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

### Markup Language

> # \<h1\>HTML\</h1\>
>
> \<p\>HTML이란 Hyper Text Markup Language 의 약자이다.\</p\>
>
>
> ## \<h2\>Hyper Text.\</h2\>
>
> \<p\>Hyper Text란 기존의 선형적인 텍스트가 아닌 비 선형적으로 이루어진 텍스트를 의미하며, 이는 인터넷의 등장과 함께 대두되었다. 기본적으로 Hyper Link를 통해 텍스트를 이동한다.\</p\>
>
> \<p\>본문 : 이러한 Hyper Text는 인간이 기억하는 방식까지 바꾸고 있는데 이를 컬럼비아대 벳시 스패로 교수팀은 구글 효과(Google Effect)라고 이름붙이고, 해당 연구를 '사이언스' 지에 게재하였다.\</p\>
>
>
> ## \<h2\>구글 효과(Google Effect).\</h2\>
>
> \<p\>구글 효과란...\</p\>

##### · 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

##### · 프로그래밍 언어와는 다르게 단순하게 데이터를 표현하기만 한다.

##### · 대표적인 예 : HTML, Markdown



## HTML 기본 구조

### [기본 구조] html 요소

![image-20210803092247955](Web1.assets/image-20210803092247955.png)

### [기본 구조] head 요소

![image-20210803092315603](Web1.assets/image-20210803092315603.png)

### [기본 구조] body 요소

![image-20210803092345973](Web1.assets/image-20210803092345973.png)

### 메타 데이터를 표현하는 새로운 규약, Open Graph Protocol

##### · HTML 문서의 메타 데이터를 통해 문서의 정보를 전달

##### · 페이스북에서 만들었으며, 메타정보에 해당한느 제목, 설명 등을 쓸 수 있도록 정의

![image-20210803151057436](Web1.assets/image-20210803151057436.png)

### DOM (Document Object Model) 트리

![image-20210803151201681](Web1.assets/image-20210803151201681.png)

![image-20210803151229882](Web1.assets/image-20210803151229882.png)

##### · DOM은 문서의 구조화된 표현(Structured Representation)을 제공하며, 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공하여 그들이 문서 구조, 스타일 내용 등을 변경 할 수 있게 도움

##### · DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공

##### · Web Page의 객체 지향 표현

### 요소 (element)

```html
<h1>contents</h1>
```

##### · HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성

​	· 태그 (Element, 요소)는 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의

##### · 내용이 없는 태그들

​	· br,  hr,  img,  input,  link,  meta

##### · 요소는 중첩(nested)될 수 있음

​	· 요소의 중첩을 통해 하나의 문서를 구조화  
​	· 여는 태그와 닫는 태그의 쌍을 잘 확인해야함  
​	· 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음

### 속성 (attribute)

```html
<a href="https://google.com"></a>
```

##### · 속성을 통해 태그의 부가적인 정보를 설정할 수 있음

##### · 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공

##### · 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재

##### · 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음


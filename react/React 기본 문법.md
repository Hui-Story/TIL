[TOC]

# React 기본 문법 (with TypeScript)

> TypeScript를 적용한 React의 기본적인 문법에 대한 정리

<br>

## 1. (함수형) 컴포넌트 작성

### 1-1. 기본적인 컴포넌트 구조와 렌더링

- 리액트 컴포넌트는 **함수형, 클래스형**으로 작성할 수 있음
- **XML** 형식의 값을 반환해줄 수 있음 **(JSX)**

**Hello.tsx**

```tsx
import React from 'react'

// interface 를 통해 Props 의 타입 설정
interface HelloProps {
  color: string
  name: string
}

function Hello({ color, name }: HelloProps) {  // Props 비구조화 할당, Props 타입 적용
  return <div style={{ color }}>안녕하세요 {name}</div>
}

// Props 의 기본값 설정
Hello.defaultProps = {
  name: '이름없음'
}

export default Hello
```

> **비구조화 할당 **(구조 분해) 을 통해 `props.color` 대신 `color` 만으로 조회

**App.tsx**

```tsx
import React from 'react'
import Hello from './Hello'
import './App.css'

function App() {
  return (
    // Fragment 문법
    <>
      <Hello name="react" color="red"/>
      <Hello color="pink"/>
    	<div className="gray-box"></div>  // CSS 클래스 설정
    </>
  )
}

export default App
```

> **Fragment** : `<></>` 처럼 이름 없이 작성하면 별도의 엘리먼트를 생성하지 않음

> `class=` 대신 `className=` 으로 **CSS 클래스** 설정

**App.css**

```css
.gray-box {
  background: gray
  width: 64px
  height: 64px
}
```

**index.tsx**

```tsx
import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import App from './App'
import * as serviceWorker from './serviceWorker'

ReactDOM.render(<App />, document.getElementById('root'))

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister()
```

> **ReactDOM.render** : 브라우저에 있는 <u>실제 DOM 내부</u>에 리액트 컴포넌트를 렌더링

**public/index.html**

```html
<div id="root"></div>
```

> 해당 `div` 내부에 컴포넌트가 렌더링됨

<br>

### 1-2. `props.children` 활용 태그 사이의 값 조회

- **Wrapper 내부의 어떤 위치**에 children 을 렌더링할지 작성
- `props.children` 을 작성하지 않으면 children 이 표시되지 않음

**Wrapper.tsx**

```tsx
import React from 'react'

function Wrapper({ children }) {
  const style = {
    border: '2px solid black',
    padding: '16px',
  }
  
  return (
    <div style={style}>
      {children}
    </div>
  )
}

export default Wrapper
```

**App.tsx**

```tsx
import React from 'react'
import Hello from './Hello'
import Wrapper from './Wrapper'

function App() {
  return (
    <Wrapper>
      <Hello name="react" color="red"/>
      <Hello color="pink"/>
    </Wrapper>
  )
}

export default App
```

<br>

### 1-3. 조건부 렌더링

- **JSX** 에서 **null, false, undefined** 를 렌더링하게 되면 아무것도 나타나지 않음
- **삼항연산자** 또는 **&& 연산자**를 통해 조건부 렌더링 구현
  - 단순히 보여주거나 숨기는 경우 && 연산자가 간편

**Hello.tsx**

```tsx
import React from 'react'

function Hello({ color, name, isSpecial }) {
  return (
    // && 연산자 를 통한 조건부 렌더링
    <div style={{ color }}>
      {isSpecial && <b>*</b>}
      안녕하세요 {name}
    </div>
  )
}

Hello.defaultProps = {
  name: '이름없음'
}

export default Hello
```

**App.tsx**

```tsx
import React from 'react'
import Hello from './Hello'
import Wrapper from './Wrapper'

function App() {
  return (
    <Wrapper>
      <Hello name="react" color="red" isSpecial />
      <Hello color="pink"/>
    </Wrapper>
  )
}

export default App
```

> props 이름만 작성하고 **값을 생략**하면 `true` 로 간주 (`isSpecial={true}`와 같은 동일한 의미)

<br>

## 2. `useState` 활용 컴포넌트 상태 관리

- React 에서 객체를 수정할 경우 **불변성**을 지켜주어야 함

  - 불변성을 지켜주어야 업데이트를 감지하고, 업데이트 성능 최적화가 가능

    **잘못된 예시**

    ```tsx
    inputs[name] = value
    ```

    **바른 예시** (**Setter 함수** 활용)

    ```tsx
    setInputs({
      ...inputs,  // spread 문법 (기존 객체를 펼쳐서 복사)
      [name]: value
    })
    ```

- 상태의 **기본값**을 파라미터로 넣어서 호출할 수 있음

  - 첫번째 원소는 **현재 상태**, 두번째 원소는 **Setter 함수**

    ```tsx
    const numberState = useState(0)
    const number = numberState[0]
    const setNumber = numberState[1]
    ```

  - **배열 비구조화 할당**을 통하여 각 원소 추출 가능

    ```tsx
    const [number, setNumber] = useState(0)
    ```

- 상태가 `null` 이 될 수도 있는 경우에만 TypeScript `Generics` 활용 (이외에는 **자동으로 추론**)

  ```tsx
  interface Information = { name: string; description: string }
  const [info, setInformation] = useState<Information | null>(null)
  ```

### 2-1. 여러개의 input 상태 관리

> 여러개의 input 을 통한 **상태 변경**과 `placeholder` 를 통한 **설명 표시**하기

**InputSample.tsx**

```tsx
import React, { useState } from 'react'

function InputSample() {
  // inputs 가 null 이 될 수 있는 경우에 Generics 사용
  const [inputs, setInputs] = useState({
    name: '',
    nickname: ''
  })

  const { name, nickname } = inputs  // 비구조화 할당을 통해 값 추출

  // e 의 타입의 경우 JSX 에서 onChange 마우스 오버를 통해 확인
  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { value, name } = e.target  // 우선 e.target 에서 name 과 value 를 추출
    setInputs({
      ...inputs,  // 기존의 input 객체를 복사한 뒤 (spread 문법)
      [name]: value  // name 키를 가진 값을 value 로 설정
    })
  }

  const onReset = (e: React.MouseEvent<HTMLButtonElement>) => {
    setInputs({
      name: '',
      nickname: '',
    })
  }

  return (
    <div>
      <input name="name" placeholder="이름" onChange={onChange} value={name} />
      <input name="nickname" placeholder="닉네임" onChange={onChange} value={nickname}/>
      <button onClick={onReset}>초기화</button>
      <div>
        <b>값: </b>
        {name} ({nickname})
      </div>
    </div>
  )
}

export default InputSample
```

<br>

## 3. `useRef` 활용

### 3-1. 특정 DOM 선택

- DOM 을 직접 선택하는 `getElementById`, `querySelector` 와 같은 기능 구현
- Video.js, JWPlayer 같은 **HTML5 Video** 라이브러리나 D3, chart.js 같은 **그래프** 라이브러리에서도 활용

**InputSample.js**

```js
import React, { useState, useRef } from 'react'

function InputSample() {
  const [inputs, setInputs] = useState({
    name: '',
    nickname: ''
  })
  const nameInput = useRef()  // nameInput 이라는 Ref 객체 생성

  const { name, nickname } = inputs

  const onChange = e => {
    const { value, name } = e.target
    setInputs({
      ...inputs,
      [name]: value
    })
  }

  const onReset = () => {
    setInputs({
      name: '',
      nickname: ''
    })
    nameInput.current.focus()  // Ref 객체의 '.current' 를 통해 DOM 선택
  }

  return (
    <div>
      <input
        name="name"
        placeholder="이름"
        onChange={onChange}
        value={name}
        ref={nameInput}  // 선택할 DOM 에 ref 값으로 설정
      />
      <input
        name="nickname"
        placeholder="닉네임"
        onChange={onChange}
        value={nickname}
      />
      <button onClick={onReset}>초기화</button>
      <div>
        <b>값: </b>
        {name} ({nickname})
      </div>
    </div>
  )
}

export default InputSample
```

### 3-2. 컴포넌트 안의 변수로 배열 렌더링 관리

- `useRef` 는 컴포넌트 안에서 조회 및 수정 할 수 있는 **변수를 관리**할 수 있음
  - `useRef` 로 관리하고 있는 변수는 설정 후 **바로 조회 가능**
  - `state` 는 수정하는 함수를 호출한 뒤 <u>렌더링 이후 업데이트 된 상태</u> 조회 가능
- 다음과 같은 값을 관리할 수 있음
  - `setTimeout`, `setInterval` 을 통해서 만들어진 `id`
  - 외부 라이브러리를 사용하여 생성된 인스턴스
  - scroll 위치

#### 3-2-1. map 을 사용하여 배열 렌더링

> users 배열을 컴포넌트로 렌더링

**UserList.js**

```js
import React from 'react'

function User({ user }) {
  return (
    <div>
      <b>{user.username}</b> <span>({user.email})</span>
    </div>
  )
}

function UserList() {
  const users = [
    {
      id: 1,
      username: 'user1',
      email: 'user1@example.com'
    },
    {
      id: 2,
      username: 'user2',
      email: 'user2@example.com'
    },
    {
      id: 3,
      username: 'user3',
      email: 'user3@example.com'
    }
  ]

  return (
    <div>
      {users.map(user => (
        <User user={user} key={user.id} />
      ))}
    </div>
  )
}

export default UserList
```

- 고유한 값이 없는 경우 콜백함수의 두번째 파라미터 `index` 활용

  ```js
  <div>
    {users.map((user, index) => (
      <User user={user} key={index} />
    ))}
  </div>
  ```

#### 3-2-2. 배열의 항목 추가, 제거, 수정

> App 에 users 배열을 선언하고 UserList 에게 props 로 전달한 뒤 진행

**App.js**

```js
import React, { useRef, useState } from 'react'
import UserList from './UserList'
import CreateUser from './CreateUser'

function App() {
  const [inputs, setInputs] = useState({
    username: '',
    email: ''
  })
  const { username, email } = inputs
  const onChange = e => {
    const { name, value } = e.target
    setInputs({
      ...inputs,
      [name]: value
    })
  }
  const [users, setUsers] = useState([
    {
      id: 1,
      username: 'user1',
      email: 'user1@example.com',
      active: true
    },
    {
      id: 2,
      username: 'user2',
      email: 'user2@example.com',
      active: false
    },
    {
      id: 3,
      username: 'user3',
      email: 'user3@example.com',
      active: false
    }
  ])

  const nextId = useRef(4)  // 파라미터를 넣어주면 '.current' 의 기본값이 됨
  const onCreate = () => {
    const user = {
      id: nextId.current,  // nextId 값 조회
      username,
      email
    };
    setUsers(users.concat(user))  // concat 활용 (새로운 배열 생성)
    // setUsers([...users, user]) : spread 연산자 사용 (기존의 배열 수정)

    setInputs({
      username: '',
      email: ''
    })
    nextId.current += 1  // nextId 값 수정
  }

  const onRemove = id => {
    // user.id 가 파라미터로 일치하지 않는 원소만 추출해서 새로운 배열을 만듬
    // = user.id 가 id 인 것을 제거함
    setUsers(users.filter(user => user.id !== id));
  }
  const onToggle = id => {
    setUsers(
      users.map(user =>
        user.id === id ? { ...user, active: !user.active } : user
      )
    )
  }
  return (
    <>
      <CreateUser
        username={username}
        email={email}
        onChange={onChange}
        onCreate={onCreate}
      />
      <UserList users={users} onRemove={onRemove} onToggle={onToggle} />
    </>
  )
}

export default App
```

**CreateUser.js**

```js
import React from 'react'

function CreateUser({ username, email, onChange, onCreate }) {
  return (
    <div>
      <input
        name="username"
        placeholder="계정명"
        onChange={onChange}
        value={username}
      />
      <input
        name="email"
        placeholder="이메일"
        onChange={onChange}
        value={email}
      />
      <button onClick={onCreate}>등록</button>
    </div>
  )
}

export default CreateUser
```

**UserList.js**

```js
import React from 'react'

function User({ user, onRemove, onToggle }) {
  return (
    <div>
      <b
        style={{
          cursor: 'pointer',
          color: user.active ? 'green' : 'black'
        }}
        onClick={() => onToggle(user.id)}
      >
        {user.username}
      </b>
      &nbsp;
      <span>({user.email})</span>
      <button onClick={() => onRemove(user.id)}>삭제</button>
    </div>
  )
}

function UserList({ users, onRemove, onToggle }) {
  return (
    <div>
      {users.map(user => (
        <User
          user={user}
          key={user.id}
          onRemove={onRemove}
          onToggle={onToggle}
        />
      ))}
    </div>
  )
}

export default UserList
```

<br>

## 4. `useEffect` 활용

> 컴포넌트가 **마운트/언마운트/업데이트** 될 때 작업 설정

### 4-1. 마운트/언마운트 관리

- **마운트** 시에 하는 작업 예시
  - `props` 로 받은 값을 컴포넌트의 로컬 상태로 설정
  - 외부 API 요청 (REST API 등)
  - 라이브러리 사용 (D3, Video.js 등)
  - setInterval 을 통한 반복작업 혹은 setTimeout 을 통한 작업 예약
- **언마운트** 시에 하는 작업 예시
  - setInterval, setTimeout 을 사용하여 등록한 작업을 clear (clearInterval, clearTimeout)
  - 라이브러리 인스턴스 제거

**UserList.js**

```js
import React, { useEffect } from 'react'

function User({ user, onRemove, onToggle }) {
  useEffect(() => {
    console.log('컴포넌트가 화면에 나타남')
    // cleanup 함수 호출
    return () => {
      console.log('컴포넌트가 화면에서 사라짐')
    }
  }, [])
  return (
    (...)
  )
}

function UserList({ users, onRemove, onToggle }) {
  return (
    (...)
  )
}

export default UserList
```

### 4-2. 업데이트 관리 (deps 값 지정)

- `deps` 에 특정 값을 넣을 경우, **처음 마운트 될 때** 호출이 되고, **지정한 값이 바뀔 때**에도 호출됨

- `useEffect` 안에서 사용하는 상태나 props 는 `deps` 에 넣어주어야 함 **(규칙)**

  > 그렇지 않으면 `useEffect` 에 등록한 함수가 **최신 props 나 상태**를 가르키지 않음

```js
import React, { useEffect } from 'react'

function User({ user, onRemove, onToggle }) {
  useEffect(() => {
    console.log('컴포넌트가 화면에 나타남')
    console.log(user);
    // cleanup 함수 호출
    return () => {
      console.log('컴포넌트가 화면에서 사라짐')
      console.log(user);
    }
  }, [user])  // deps 값 지정
  return (
    (...)
  )
}

(...)

export default UserList
```

### 4-3. deps 파라미터 생략

> deps 파라미터를 생략하면, 컴포넌트가 리렌더링 될 때마다 호출됨

```js
import React, { useEffect } from 'react'

function User({ user, onRemove, onToggle }) {
  useEffect(() => {
    console.log(user);
  });  // deps 값 생략
  return (
    (...)
  )
}

(...)

export default UserList
```

<br>

## 5. 성능 최적화

> 변하지 않은 값이나 함수를 재사용하여 성능을 높이는 방법

- 컴포넌트의 성능을 **실제로 개선할 수 있는 상황**에서만 진행

### 5-1. `useMemo` 활용 (값 재사용)

> 연산된 값을 재사용

- 첫번째 파라미터 : 어떻게 연산할지 정의하는 함수
- 두번째 파라미터 : deps 배열

**App.js**

```js
function countActiveUsers(users) {
  console.log('활성 사용자 수를 세는중...')
  return users.filter(user => user.active).length
}

function App() {
  // users 의 내용이 바뀌지 않았다면 이전에 연산한 값 재사용
  const count = useMemo(() => countActiveUsers(users), [users])
  // const count = countActiveUsers(users) : 매번 값을 연산 (재사용 X)
  
(...)
 
export default App
```

### 5-2. `useCallback` 활용 (함수 재사용)

> 특정 함수를 새로 만들지 않고 재사용

- 함수 안에서 사용하는 상태 혹은 props 가 있다면 꼭, `deps` 배열안에 포함
- `React.memo` 를 통한 컴포넌트 **렌더링 최적화 작업**까지 해주어야 성능이 최적화됨

**App.js**

```js
(...)

function App() {
  const onChange = useCallback(
    e => {
      const { name, value } = e.target
      setInputs({
        ...inputs,
        [name]: value
      })
    },
    [inputs]  // deps 배열안에 상태나 props 포함
  )

  const nextId = useRef(4)
  const onCreate = useCallback(() => {
    const user = {
      id: nextId.current,
      username,
      email
    }
    setUsers(users.concat(user))

    setInputs({
      username: '',
      email: ''
    })
    nextId.current += 1;
  }, [users, username, email])

  const onRemove = useCallback(
    id => {
      setUsers(users.filter(user => user.id !== id))
    },
    [users]
  )
  
  const onToggle = useCallback(
    id => {
      setUsers(
        users.map(user =>
          user.id === id ? { ...user, active: !user.active } : user
        )
      )
    },
    [users]
  )
  
(...)
 
export default App
```

### 5-3. `React.memo` 활용 (리렌더링 방지)

> 컴포넌트의 props 가 바뀌지 않았을 경우, 리렌더링 방지

- **리렌더링**을 막을 컴포넌트에서 `React.memo` 적용

- `deps` 에 포함하는 대신 **함수형 업데이트**를 통해 함수 재생성 방지 (**최신값** 참조 가능)

**CreateUser.js**

```js
import React from 'react'

const CreateUser = ({ username, email, onChange, onCreate }) => {
  return (
    (...)
  )
}

export default React.memo(CreateUser)  // React.memo 적용
```

**UserList.js**

```js
import React from 'react'

// React.memo 적용
const User = React.memo(function User({ user, onRemove, onToggle }) {
  return (
    (...)
  )
})

function UserList({ users, onRemove, onToggle }) {
  return (
    (...)
  )
}

export default React.memo(UserList)  // React.memo 적용
```

**App.js**

```js
(...)

function App() {
  const onChange = useCallback(e => {
    const { name, value } = e.target
    setInputs(inputs => ({  // 함수형 업데이트
      ...inputs,
      [name]: value
    }))
  }, [])  // deps 배열에서 inputs 제외

  const nextId = useRef(4)
  const onCreate = useCallback(() => {
    const user = {
      id: nextId.current,
      username,
      email
    }
    setUsers(users => users.concat(user))  // 함수형 업데이트

    setInputs({
      username: '',
      email: ''
    })
    nextId.current += 1;
  }, [username, email])  // deps 배열에서 users 제외

  const onRemove = useCallback(id => {
    setUsers(users => users.filter(user => user.id !== id))  // 함수형 업데이트
  }, [])  // deps 배열에서 users 제외
  
  const onToggle = useCallback(id => {
    setUsers(users =>  // 함수형 업데이트
      users.map(user =>
        user.id === id ? { ...user, active: !user.active } : user
      )
    )
  }, [])  // deps 배열에서 users 제외
  
(...)
 
export default App
```

<br>

## 6. `useReducer` 활용

- 컴포넌트의 상태 업데이트 로직을 **컴포넌트에서 분리**할 수 있음 (**컴포넌트 바깥**이나 **다른 파일**에 작성 가능)

- `type` 값을 지닌 `action` 객체를 통해 상태를 변경 (`action` 객체의 형태는 자유)

  ```js
  // 카운터에 1을 더하는 액션
  {
    type: 'INCREMENT'
  }
  // input 값을 바꾸는 액션
  {
    type: 'CHANGE_INPUT',
    key: 'email',
    value: 'tester@react.com'
  }
  // 새 할 일을 등록하는 액션
  {
    type: 'ADD_TODO',
    todo: {
      id: 1,
      text: 'useReducer 배우기',
      done: false,
    }
  }
  ```

- **관리하는 값이 여러개**가 되어 구조가 복잡하거나, **setter** 를 한 함수에서 여러번 사용하는 경우 주로 활용

```js
import React, { useRef, useReducer, useMemo, useCallback } from 'react';
import UserList from './UserList';
import CreateUser from './CreateUser';

function countActiveUsers(users) {
  console.log('활성 사용자 수를 세는중...');
  return users.filter(user => user.active).length;
}

// 초기 상태를 컴포넌트 바깥에서 설정
const initialState = {
  inputs: {
    username: '',
    email: ''
  },
  users: [
    {
      id: 1,
      username: 'user1',
      email: 'user1@example.com',
      active: true
    },
    {
      id: 2,
      username: 'tester',
      email: 'user2@example.com',
      active: false
    },
    {
      id: 3,
      username: 'user3',
      email: 'user3@example.com',
      active: false
    }
  ]
};

function reducer(state, action) {
  // switch 를 통해 action 의 type 을 활용
  switch (action.type) {
    // state 의 불변성을 지켜주어야 함
    case 'CHANGE_INPUT':
      return {
        ...state,
        inputs: {
          ...state.inputs,
          [action.name]: action.value
        }
      };
    case 'CREATE_USER':
      return {
        inputs: initialState.inputs,
        users: state.users.concat(action.user)
      };
    case 'TOGGLE_USER':
      return {
        ...state,
        users: state.users.map(user =>
          user.id === action.id ? { ...user, active: !user.active } : user
        )
      };
    case 'REMOVE_USER':
      return {
        ...state,
        users: state.users.filter(user => user.id !== action.id)
      };
    default:
      return state;
  }
}

function App() {
  const [state, dispatch] = useReducer(reducer, initialState);
  const nextId = useRef(4);

  // state 에서 필요한 값들을 추출
  const { users } = state;
  const { username, email } = state.inputs;

  const onChange = useCallback(e => {
    const { name, value } = e.target;
    // action 객체를 dispatch
    dispatch({
      type: 'CHANGE_INPUT',
      name,
      value
    });
  }, []);

  const onCreate = useCallback(() => {
    dispatch({
      type: 'CREATE_USER',
      user: {
        id: nextId.current,
        username,
        email
      }
    });
    nextId.current += 1;
  }, [username, email]);

  const onToggle = useCallback(id => {
    dispatch({
      type: 'TOGGLE_USER',
      id
    });
  }, []);

  const onRemove = useCallback(id => {
    dispatch({
      type: 'REMOVE_USER',
      id
    });
  }, []);

  const count = useMemo(() => countActiveUsers(users), [users]);
  return (
    <>
      <CreateUser
        username={username}
        email={email}
        onChange={onChange}
        onCreate={onCreate}
      />
      <UserList users={users} onToggle={onToggle} onRemove={onRemove} />
      <div>활성사용자 수 : {count}</div>
    </>
  );
}

export default App;
```

<br>

## Reference

- [벨로퍼트와 함께하는 모던 리액트](https://react.vlpt.us/)
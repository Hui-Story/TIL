[TOC]

# 🔃 React Router v6, Redux-Saga 연동

## 1. `history` 대신 `useNavigate` 사용

> React Router v6 에서 ‘history’ 가 ‘useNavigate’ 로 대체되면서 변경사항을 Saga 에 적용

- Component 의 Container 에서 `navigate` 정의

  `containers/PostContainers.js`

  ```jsx
  import { useNavigate } from "react-router-dom";
  
  function PostContainer({ postId }) {
  	const navigate = useNavigate();
  	...
  
  	return (
  		<button onClick={() => dispatch(goToHome(navigate))}>홈으로 이동</button>
  		...
  	);
  }
  ```

- module 에서 `navigate` 파라미터 전달, Saga 에서 `navigate` 사용

  `modules/posts.js`

  ```jsx
  const GO_TO_HOME = "GO_TO_HOME";
  
  // 파라미터로 navigate 전달
  export const goToHome = (navigate) => ({
    type: GO_TO_HOME,
    navigate: navigate,
  });
  
  ...
  
  function* goToHomeSaga(action) {
  
  	// --- history 대신 navigate 사용 ---
    yield action.navigate("/");
  
  	// --- history 를 사용할 때 ---
    // const history = yield getContext("history");
    // history.push("/");
  
  }
  ```

- `navigate` 를 전역으로 관리하는 방법도 고민해볼 것

  - [참고자료](https://github.com/remix-run/react-router/issues/7135)
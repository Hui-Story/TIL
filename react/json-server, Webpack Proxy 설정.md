[TOC]

# :globe_with_meridians: json-server, Webpack Proxy 설정

<br>

## 💻 json-server 로 임시 API 서버 생성

### 1. 임시 API 서버 생성

- `data.json` 파일을 project 폴더에 생성

  ```json
  {
    "posts": [
      {
        "id": 1,
        "title": "리덕스 미들웨어를 배워봅시다",
        "body": "리덕스 미들웨어를 직접 만들어보면 이해하기 쉽죠."
      },
      {
        "id": 2,
        "title": "redux-thunk를 사용해봅시다",
        "body": "redux-thunk를 사용해서 비동기 작업을 처리해봅시다!"
      },
      {
        "id": 3,
        "title": "redux-saga도 사용해봅시다",
        "body": "나중엔 redux-saga를 사용해서 비동기 작업을 처리하는 방법도 배워볼 거예요."
      }
    ]
  }
  ```

- 파일을 기반으로 서버 실행

  ```bash
  $ npx json-server ./data.json --port 4000
  ```

- 터미널에 다음과 같은 결과물 생성

  ```bash
  	\\{^_^}/ hi!
  
    Loading ./data.json
    Done
  
    Resources
    <http://localhost:4000/posts>
  
    Home
    <http://localhost:4000>
  ```

- 다음과 같은 링크를 통해 API 서버 접근 가능

  - http://localhost:4000/posts
  - http://localhost:4000/posts/1

### 2. axios 를 사용하여 API 요청

- js 파일에 실제 API 요청을 위한 로직 작성

  ```jsx
  import axios from 'axios';
  
  export const getPosts = async () => {
    const response = await axios.get('<http://localhost:4000/posts>');
    return response.data;
  };
  
  export const getPostById = async id => {
    const response = await axios.get(`http://localhost:4000/posts/${id}`);
    return response.data;
  };
  ```

- 브라우저의 URL 요청을 통해 확인

  ![image](https://user-images.githubusercontent.com/87461594/183449349-a8e86b44-81bb-4393-bdaf-c6024f463276.png)

### 3. [참고문서](https://react.vlpt.us/redux-middleware/08-json-server.html)

## 📶 Proxy 설정을 통한 개발 환경 CORS 문제 해결

### 1. Proxy 설정하기 (선택)

> Webpack 개발 서버의 프록시를 사용하면, 개발 단계에서 CORS 설정 없이 API 를 요청 가능

![image](https://user-images.githubusercontent.com/87461594/183449394-34fe12de-8a72-4057-93b5-f1e6f114f9b5.png)

- `package.json` 수정 (`proxy` 추가)

  ```json
  (...),
    },
    "proxy": "<http://localhost:4000>"
  }
  ```

- `[<http://localhost:4000/posts>](<http://localhost:4000/posts>)` 대신에 `/posts` URL 로 요청을 하면 현재 개발 서버 (`localhost:3000`) 으로 요청하게 됨

  ```jsx
  import axios from 'axios';
  
  export const getPosts = async () => {
    const response = await axios.get('/posts');
    return response.data;
  };
  
  export const getPostById = async id => {
    const response = await axios.get(`/posts/${id}`);
    return response.data;
  };
  ```

  ![image](https://user-images.githubusercontent.com/87461594/183449423-98e7e488-0fea-4d94-a63b-f9622f350f54.png)

### 2. 개발과 배포 환경에 따라 baseURL 수정

> 프로젝트를 완성하고 배포하는 경우에 API 도메인과 서비스의 도메인이 다른 경우 (예: 서비스는 [velog.io](http://velog.io/), API 는 [api.velog.io](http://api.velog.io/)), axios 의 글로벌 `baseURL` 을 설정하면 됨

- `index.js` 에 다음과 같이 작성

```jsx
axios.defaults.baseURL = process.env.NODE_ENV === 'development' ? '/' : '<https://api.velog.io/>';
```

### 3. [참고문서](https://react.vlpt.us/redux-middleware/09-cors-and-proxy.html)
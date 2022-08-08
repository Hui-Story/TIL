# :book: React 프로젝트 생성

> React 프로젝트 생성 및 라이브러리 설치

### 0. [해당 문서](https://react.vlpt.us/)를 참고하여 진행

### 1. React 프로젝트 생성

- npx create-react-app <프로젝트 이름>

```bash
$ npx create-react-app docong
$ cd docong
$ npm start
or
$ yarn start
```

### 2. Immer 라이브러리 설치 (선택)

> 불변성 관리를 위한 라이브러리

```bash
$ npm install immer
or
$ yarn add immer
```

- [참고문서](https://react.vlpt.us/basic/23-immer.html)

### 3. Sentry 연동 (선택)

> error 목록을 수집하여 관리할 수 있는 서비스

- [Sentry 프로젝트 생성](https://sentry.io/)

```bash
$ npm install @sentry/react @sentry/tracing
or
$ yarn add @sentry/react @sentry/tracing
```

- [참고문서](https://react.vlpt.us/basic/26-componentDidCatch-and-sentry.html)

### 4. Prettier 연동 (선택)

> 자동으로 코드 스타일을 관리

- VSCode `Prettier - Code formatter` 익스텐션 설치

![image](https://user-images.githubusercontent.com/87461594/183420609-33772ac3-f075-4986-8363-bf09cb1c3048.png)

- 루트 디렉토리에 `.prettierrc`  파일 생성 후 다음과 같이 작성

```json
{
  "trailingComma": "es5",
  "tabWidth": 4,
  "semi": false,
  "singleQuote": true
}
```

- `Ctrl + ,`  환경설정에서 ‘Format On Save’ 설정 (저장할 때 자동으로 코드 변경)

![image](https://user-images.githubusercontent.com/87461594/183420658-e6d6792e-ab82-4e40-a0e8-c01bf30fbaf5.png)

- ‘Format On Save’ 가 적용되는 `defaultFormatter` 목록 추가

  - `Ctrl + P` 에서 `>settings.json` 검색

  ![image](https://user-images.githubusercontent.com/87461594/183420798-860b282e-c352-41c2-b801-f6c88120fdb4.png)

  - `settings.json` 의 아래에 다음처럼 코드 추가

  ```json
  		"editor.formatOnSave": true,
      "[javascript]": {
          "editor.defaultFormatter": "esbenp.prettier-vscode"
      },
      "[javascriptreact]": {
          "editor.defaultFormatter": "esbenp.prettier-vscode"
      },
      "[typescript]": {
          "editor.defaultFormatter": "esbenp.prettier-vscode"
      },
      "[typescriptreact]": {
          "editor.defaultFormatter": "esbenp.prettier-vscode"
      },
  ```

- [참고문서](https://prettier.io/docs/en/configuration.html)

### 5. ESLint 연동 (with Prettier) (선택)

> 코드 스타일에 적합하지 않은 경우 VSCode 에서 알려줌

- 기본적인 규칙은 `ESLint` 익스텐션 설치만으로 사용 가능 **(일반적인 경우에 사용)**

![image](https://user-images.githubusercontent.com/87461594/183420818-d1e6f9d2-1a64-40b8-b448-503f40e54b48.png)

- 까다로운 규칙 적용을 위해서는 프로젝트에 설정 필요 **(선택)**

  - 라이브러리 제공
    - [eslint-config-airbnb](https://www.npmjs.com/package/eslint-config-airbnb)
    - [eslint-config-google](https://www.npmjs.com/package/eslint-config-google)
    - [eslint-config-standard](https://www.npmjs.com/package/eslint-config-standard)
  - `eslint-config-airbnb` 적용

  ```bash
  $ npm install eslint-config-airbnb
  or
  $ yarn add eslint-config-airbnb
  ```

  - `package.json` 의 `eslintConfig` 부분 수정 **(airbnb 추가)**

  ```json
    "eslintConfig": {
      "extends": [
        "react-app",
        "airbnb"
      ]
    },
  ```

  - `Prettier` 에서 관리하는 스타일을 `ESLint` 에서 비활성화

  ```bash
  $ npm install eslint-config-prettier
  or
  $ yarn add eslint-config-prettier
  ```

### 6. node-sass 라이브러리 설치 (styled-components 과 혼용)

> Sass 를 CSS 로 변환해주는 역할

- `node-sass` 라이브러리 설치

```bash
$ npm install node-sass
or
$ yarn add node-sass
```

- `classnames` 라이브러리 설치

  > 동적으로 CSS 클래스를 부여하여, 조건부 스타일링에 도움

  ```bash
  $ npm install classnames
  or
  $ yarn add classnames
  ```

- [참고문서](https://react.vlpt.us/styling/01-sass.html)

### 7. react-icons 라이브러리 설치

> Font Awesome, Material Design Icons 등의 아이콘 컴포넌트 형태로 사용 가능

- `react-icons` 라이브러리 설치

```bash
$ npm install react-icons
or
$ yarn add react-icons
```

- [참고문서](https://react-icons.github.io/react-icons/#/)

### 8. styled-components 라이브러리 설치

> CSS in JS 를 구현할 수 있는 라이브러리

- `styled-components` 라이브러리 설치

```bash
$ npm install styled-components
or
$ yarn add styled-components
```

- VSCode `vscode-styled-components` 익스텐션 설치

  > 익스텐션을 설치해야 CSS in JS 코드의 색상을 구분할 수 있음

  ![image](https://user-images.githubusercontent.com/87461594/183421125-6220b6bd-ceeb-4ef5-8436-55ef2b3b7484.png)

- `polished` 라이브러리 설치

  > Sass 에서 사용되는 유틸 함수 사용 (`lighten`, `darken`등)

  ```bash
  $ npm install polished
  or
  $ yarn add polished
  ```

### 9. axios 라이브러리 설치

> API 호출하는 라이브러리

- `axios` 라이브러리 설치

```bash
$ npm install axios
or
$ yarn add axios
```

- `react-async` 라이브러리 설치

  > async 요청 상태 관리에 대한 다양한 기능 내장

  ```bash
  $ npm install react-async
  or
  $ yarn add react-async
  ```

- [참고문서](https://github.com/axios/axios)

### 10. react-router-dom 라이브러리 설치

> react 라우터 관리

- `react-router-dom` 라이브러리 설치

```bash
$ npm install react-router-dom
or
$ yarn add react-router-dom
```

- [참고문서](https://reactrouter.com/docs/en/v6/getting-started/overview)
- [v5 → v6 변경점](https://kyung-a.tistory.com/36)

### 11. redux 라이브러리 설치

> 컴포넌트들의 상태 관련 로직을 분리시켜서 관리

- `redux` 라이브러리 설치

```bash
$ npm install redux
or
$ yarn add redux
```

- [참고문서](https://react.vlpt.us/redux/03-prepare.html)

- `react-redux` 라이브러리 설치

  > react 프로젝트에 redux 적용

  ```bash
  $ npm install react-redux
  or
  $ yarn add react-redux
  ```

- `redux-devtools-extension` 라이브러리 설치

  > redux 개발자 도구를 사용하기 위한 라이브러리

  ```bash
  $ npm install redux-devtools-extension
  or
  $ yarn add redux-devtools-extension
  ```

  - [크롬 개발자 도구](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd) 설치

- `redux-logger` 미들웨어 설치

  > redux 의 log 를 출력

  ```bash
  $ npm install redux-logger
  or
  $ yarn add redux-logger
  ```

  - [참고문서](https://github.com/LogRocket/redux-logger)

- ~~`redux-thunk` 미들웨어 설치~~ (redux-thunk 와 redux-saga 중 선택) **[제외]**

  > action 객체가 아닌 함수를 dispatch 할 수 있음

  ```bash
  $ npm install redux-thunk
  or
  $ yarn add redux-thunk
  ```

  - [참고문서](https://github.com/reduxjs/redux-thunk)

- `redux-saga` 미들웨어 설치 (redux-thunk 와 redux-saga 중 선택) **[채택]**

  > action 을 모니터링 하다가, 특정 action 이 발생하면 특정 작업을 진행 redux-thunk 에서 못하는 다양한 작업을 처리할 수 있음 (but. 진입장벽이 비교적 높음)

  ```bash
  $ npm install redux-saga
  or
  $ yarn add redux-saga
  ```

  - [참고문서](https://github.com/redux-saga/redux-saga)

- `typesafe-actions` 라이브러리 설치

  > action 생성 함수와 reducer 를 쉽고 깔끔하게 작성

  ```bash
  $ npm install typesafe-actions
  or
  $ yarn add typesafe-actions
  ```

- `redux-persist` 라이브러리 설치

  > localStorage 에 store 데이터를 저장하여 새로고침 시 유지

  ```bash
  $ npm install redux-persist
  or
  $ yarn add redux-persist
  ```

### 12. TypeScript 설치

> 코드를 작성하는 단계에서 Type 체크할 수 있는 정적 프로그래밍 언어

- React 프로젝트를 생성하면서 `TypeScript` 설치

  ```bash
  $ npx create-react-app docong --template typescript
  ```

- 프로젝트가 이미 생성된 경우 `TypeScript` 설치

  ```bash
  $ npm install typescript @types/node @types/react @types/react-dom @types/jest
  or
  $ yarn add typescript @types/node @types/react @types/react-dom @types/jest
  ```

  - `js` 확장자를 `tsx` 으로 변경

- 공식적으로 TypeScript 를 지원하지 않는 라이브러리는 `@types/` 를 앞에 붙여서 추가 설치

  - `@types/react-redux` 설치

    ```bash
    $ npm install @types/react-redux
    or
    $ yarn add @types/react-redux
    ```

  - `@types/styled-components` 설치

    ```bash
    $ npm install @types/styled-components
    or
    $ yarn add @types/styled-components
    ```

  - `@types/date-fns` 설치

    ```bash
    $ npm install @types/date-fns
    or
    $ yarn add @types/date-fns
    ```

### 13. Material UI 프레임워크 설치 (styled-components 사용)

> React 의 다양한 UI Components 를 제공하는 UI Framework

```bash
$ npm install @mui/material @mui/styled-engine-sc ~~styled-components (위에서 설치)~~
or
$ yarn add @mui/material @mui/styled-engine-sc ~~styled-components (위에서 설치)~~
```

- `@mui/icons-material` 설치

  > SVG Material icons 사용

  ```bash
  $ npm install @mui/icons-material
  or
  $ yarn add @mui/icons-material
  ```

  - `package.json` 과 `tsconfig.json` 추가 설정 필요 ([참고문서](https://mui.com/guides/styled-engine/))

    ```json
    // package.json
    
    {
      "dependencies": {
    		...
      },
    + "resolutions": {
    +   "@mui/styled-engine": "npm:@mui/styled-engine-sc@latest"
    + },
    }
    ```

    ```json
    // tsconfig.json
    
    {
      "compilerOptions": {
    +   "paths": {
    +     "@mui/styled-engine": ["./node_modules/@mui/styled-engine-sc"]
    +   }
      },
    }
    ```

- `@mui/lab` 설치

  ```jsx
  $ npm install @mui/lab
  or
  $ yarn add @mui/lab
  ```

- `@date-io/date-fns` 설치

  ```jsx
  $ npm install @date-io/date-fns
  or
  $ yarn add @date-io/date-fns
  ```

- [참고문서](https://mui.com/)

### 14. react-google-login 라이브러리 설치

> 구글 로그인 구현

```bash
$ npm install react-google-login
or
$ yarn add react-google-login
```

### 15. react-apexcharts 설치

> 다양한 Chart 를 제공해주는 라이브러리

```bash
$ npm install react-apexcharts apexcharts
or
$ yarn add react-apexcharts apexcharts
```

- `types` 폴더 내의 `apexcharts.d.ts` 파일을 추가해야 함
- [참고문서](https://github.com/apexcharts/apexcharts.js)
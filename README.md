## 프로젝트 소개

<strong>나에게 맞는 금융 상품을 추천받자!😀</strong> 사용자 금융 정보와 HONEYMONEY의 모든 이용자의 데이터베이스를 통해 맞춤형 상품을 추천합니다.
|팀원|역할|
|------|---|
|박효진|Front-end 개발, UI/UX 디자인, Chatbot 프롬프트 엔지니어링|
|허세령|Back-end 개발, Chatbot, 환율 계산기, 추천 상품 페이지 Front-end 개발|

## Tech Stack

### Language

    python
    javascript

### Back-end

    Django
    Django-rest-framework
    dj-rest-auth
    pillow

### Front-end

    Vue3
    vuetify
    pinia
    axios
    chart.js

## 설계 기획 및 목업

#### 설계 아키텍처

![설계 아키텍처](README_IMG/설계아키텍처.png)

#### 디자인 목업

![디자인목업](README_IMG/디자인목업.png)

## ERD

![ERD](README_IMG/ERD.png)

## 금융 상품 추천 알고리즘

### 1. 나의 금융 정보와 비슷한 금융 정보를 가진 유저들이 가입한 상품 추천받기

😄사용자는 회원가입 시 연봉, 자산, 저축 성향, 저축 희망 기간을 입력합니다. 최소 10000명의 유저가 가입된 HONEYMONEY에서는 모든 사용자의 금융 정보를 기반으로 내 금융 정보 맞춤 상품 10개를 추천합니다.

### 2. 내 나이대의 사용자들이 가장 많이 가입한 상품 추천 받기

😄사용자가 회원가입 시 입력한 나이를 기반으로 상품을 추천합니다. HONEYMONEY 내 같은 나이 대의 유저들이 가장 많이 가입한 상품 10개를 추천합니다.

## 서비스 기능

- 예금, 자유 적금, 정기 적금 상품 모아보기

  - 금융 상품의 가입 기간 별 금리 비교
  - 모든 상품끼리의 금리 비교
  - 은행 별 상품 검색
  - 상품 리스트에서 나의 희망 적립 기간을 한 눈에 보기 쉽게!

- 주변 은행 검색하기

  - 도/시, 시/군/구 기준 원하는 은행 찾기
  - 은행 검색 시 은행이 가진 금융 상품 리스트 출력

- 환율 계산기
  - 송금 받을 때, 송금 보낼 때, 매매 기준율 기준으로 외화 -> 원화 계산
- 금융 상품 알고리즘 추천
  - 나와 비슷한 금융 정보를 가진 이용자들의 가입 상품
  - 내 나이대 이용자들의 가입 상품
- HONEYMONEY 커뮤니티 기능
  - 게시글 작성 및 댓글 작성
- 금융 상품 찜하기

  - 금융 상품 상세 페이지에서 상품 담기, 취소하기
  - HONEYMONEY 사용자 중 몇 명이 찜했는지 확인 가능
  - 기간 별 금리를 차트로 한 눈에 확인

- 유저의 프로필 페이지
  - 내 금융 정보 변경 가능
  - 회원 탈퇴 기능
  - 내가 담은 상품 목록 출력 (예금, 적금) 및 담기 취소
  - 내가 담은 상품 개수 확인 가능
- 금융 챗봇
  - 웹 사이트의 모든 화면에서 언제든지 챗봇과 대화하기 가능
  - 내 금융 정보를 기반으로 챗봇에게 금융 상품 추천받기

## 후기

### 박효진
시작부터 말하지 않아도 분업이 정해져서 신기했고, 믿을만한 팀원을 만나 마음껏 프론트에 집중할 수 있어서 너무 재밌었다. front에서 사용하기 위한 db를 모두 구축해둔 덕분에 막힘 없이 진행할 수 있었다..

앞선 기수분들이 사용했던 stack을 쓰겠다고 당차게 시작했지만, Vuetify의 벽은 너무 높았다. 물론 부트스트랩과 동일한 부분도 많았지만, 스피너나 다이얼로그 등이 영어 단어가 달라서 docs보는데 시간이 조금 걸렸다.

지금까지 배웠던 기술 및 스택 들을 사용해보는 과정이어서 더 재미있었고, 알고리즘까지 빠지지 않고 등장해서 반가웠다. 또한 front는 굉장히 주관적인 요소라 fix하는대까지 너무 긴 시간이 걸렸고, 표현 요소를 제대로 못할때마다 답답함이 많았다. 

빠르게 back을 끝내고 front를 도와준 페어에게 고맙고, 고마운 만큼 전반적인 디자인을 깔끔하게 했다고 개인적으론 생각한다. 굉장히 만족스러운 프로젝트였고, 포트폴리오로 쓰기에 흠집없는 결과물이라고 자부할 수 있다.

가장 재미있었던 것은 의외로 AI Chat Bot인데, css는 디자인 하는 것이라 질리는 감이 있었는데, 직접 Chat Bot을 훈련시켜 원하는 대답과 유저 정보를 미리 넘겨주어 사용자 UX를 향상시킬 수 있다는 점이 매력적이었다. 파인 튜닝을 진행하고 싶었으나 데이터를 모두 준비해둔 상태에서 시작하려니, 유료였다는 점에서 포기한게 아쉬웠다.. 다음 프로젝트에는 AI요소를 이용한 작은 프로젝트를 진행해보고 싶다.

### 허세령

개발자의 분업과 협업이 이런 것인가? 프로젝트를 진행하면서 역할 분담이 쉽지 않을 것이라 생각했지만, 서로 각자의 역할을 120% 해주면서 처음부터 끝까지 순조롭게 흘러갈 수 있게 해준 페어에게 고맙습니다! 코드 오류 찾는 게 힘들었지, 팀워크는 완벽했다!

한 학기 동안 배우면서 ‘이런 건 굳이 왜 쓰지?’ 라고 생각했던 것들이 이해되기도 하고, 새로운 라이브러리를 쓰면서 docs 보는 능력이 생긴 것 같다.

일주일동안 에이바우트에 살면서 앞이 안보일 정도로 피곤에 쩔었지만, 시간 가는 줄도 모르고 결과물 보면서 뿌듯해 했다. 재밌고 후회 없이 내 인생 첫 프로젝트를 완성할 수 있음에 감사하다!😄

# Gemini CLI (1) - CLI 명령어 기본 사용 방법 (Gemini CLI 기초 - gemini 기본 사용 방법)

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcOf384%2FbtsPwcpCZ6G%2FAAAAAAAAAAAAAAAAAAAAABUclUjCayHovqPyGM6nk7CoyfYiMRPh98i_8AXsXK19%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1756652399%26allow_ip%3D%26allow_referer%3D%26signature%3DuzohDJq3woPerFaMxOUgxYfLmas%253D)

## Metadata
- Author: [[갓대희]]
- Full Title: Gemini CLI (1) - CLI 명령어 기본 사용 방법 (Gemini CLI 기초 - gemini 기본 사용 방법)
- Category: #articles
- Document Tags:  #email 
- Summary: Gemini CLI는 터미널에서 자연어로 코드 작성, 테스트, Git 커밋까지 자동 처리하는 AI 도구입니다.  
무료 티어가 관대해 개인 개발자에게 부담이 적고 코드 탐색·버그 수정·기능 개발에 유용합니다.  
세션 기억이 제한되고 권한 확인이 잦으며 긴 컨텍스트에서 오류가 날 수 있지만 대형 파일 작업에서 효율적입니다.
- URL: https://goddaehee.tistory.com/374?category=798193

## Full Document
안녕하세요! 갓대희 입니다. :-)

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/cOf384/btsPwcpCZ6G/AAAAAAAAAAAAAAAAAAAAABUclUjCayHovqPyGM6nk7CoyfYiMRPh98i_8AXsXK19/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=uzohDJq3woPerFaMxOUgxYfLmas%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
오늘은 요즘 핫한 Gemini CLI 기초 사용 방법을 알아보려고 한다.

Claude Code, OpenAI Codex에 이어 Google에서도 드디어 터미널 기반 AI 코딩 도구를 출시했다.

실제로 며칠간 써보니 생각보다 꽤 쓸만하다고 생각은 든다.

특히 무료 티어가 관대해서 개인 개발자가 부담 없이 사용할 수 있다는 점이 역시나 장점이었다.

바로 바이브 코딩을 시작할 수도 있지만, CLI 방식인 만큼 전통적인 학습 방식으로 Gemini CLI의 기초 명령어부터 알아가고, 어떤 의도로 Gemini CLI를 출시하였고, 활용하면 좋을지 파악해보자.

혹여, Gemini CLI 설치와 관련해서는 좀더 자세한 내용은 하기 글을 참고 부탁 드립니다.

[2025.07.16 - [AI/Gemini] - Gemini CLI 사용방법(설치방법) - Gemini CLI 시작하기 (with Claude CLI)](https://goddaehee.tistory.com/371)

**Gemini CLI가 뭔가?**

터미널에서 바로 사용하는 Google의 agentic 코딩 도구, 자연어 명령만으로 코드 작성부터 디버깅까지 모든 개발 작업을 처리할 수 있는 CLI 기반 AI 도구이다.

Google에서 Gemini CLI라는 터미널 기반 AI 도구를 출시했다는 소식을 듣고 바로 써봤는데 결론적으로는 IDE에 벗어나 어디에서든 활용할 수 있다는 클로드의 컨셉과 유사하다고 느껴졌다.

이친구 또한 클로드 처럼 기존 도구나 워크플로우를 바꿀 필요 없이, 터미널에서 바로 AI와 협업할 수 있다는 게 핵심이다.

##### **Gemini CLI란?**

Gemini CLI는 Google이 **2025년 6월 25일(하필?)**에 출시한 터미널 기반 AI 코딩 도구다.

단순한 코드 자동완성 도구가 아니라, "에이전트(agent)" 역할을 하는 AI 개발자라고 볼 수도 있다.

자연어로 요청하면 알아서 계획을 세우고, 코드를 작성하고, 테스트하고, Git 커밋까지 가능 하다.

##### **Gemini CLI의 핵심 특징**

* **터미널 네이티브 :** 새로운 IDE나 확장프로그램 설치 불필요
* **전체 코드베이스 이해 :** 프로젝트 구조와 컨텍스트를 자동으로 파악
* **직접 액션 실행 :** 파일 편집, 명령어 실행, Git 작업까지 자동화
* **MCP 지원 :** Google Drive, Slack 등 외부 도구와 연동
* **Gemini 2.5 Pro 기반 :** 100만 토큰 컨텍스트 윈도우
* **관대한 무료 티어 :** 분당 60회, 하루 1000회 무료 사용

##### **빠른 시작 - 5분 만에 시작하기**

Gemini CLI 설치는 클로드 보다 쉽다. 처음부터 클로드는 과도기가 있어 wsl이 필요한 시점이 있었지만, Gemini CLI는 Windows를 지원하며, Node.js만 있으면 바로 시작할 수 있다.

###### 📄 필수 요구사항 확인

```
# Node.js 버전 확인 (18 이상 필요)
node --version

# npm 버전 확인  
npm --version
```

처음 실행하면 Google 계정 연동을 유도한다. 개인 Google 계정만 있어도 무료로 사용 가능하고, key를 발급 받아 사용도 가능하다.   

자세한 내용은 하기 글에 작성해 두었다. (참고)

[2025.07.16 - [AI/Gemini] - Gemini CLI 사용방법(설치방법) - Gemini CLI 시작하기 (with Claude CLI)](https://goddaehee.tistory.com/371)

- 이렇게 아직은 다양한 issue가 레포트 되어 개선사항, 변경 사항이 많을 수 있으니, 자주 버전을 올려 주면 좋을 것 같다.

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/mQKVJ/btsPwMRNkn2/AAAAAAAAAAAAAAAAAAAAAPPS6K3pZ0Yg2nyb8I9qfI_VWa46RKV_rh3y3PgIdCGU/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=lwi3%2FxnpBKTi5QcQNtkWX9diMYE%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
ex) 하기와 같이 업데이트 권고를 해주고 있다.

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/6DyUf/btsPwKmamGv/AAAAAAAAAAAAAAAAAAAAAHhNx7tMz9KoG2XvMzu_udD78FBwRA9fsuz_DdgI0hA1/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=1OLD8bDp968MeghYs%2BuxB7gSC2s%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
ex) update 완료

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/d7VC6K/btsPxCVlBuu/AAAAAAAAAAAAAAAAAAAAABoOZis1stQ3knnryah7T5VeD1yZdDML1G7P-UaWvQAR/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=XTCoerEiw6NH9Klewh2OB5AB%2Frk%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
##### **Gemini CLI 기본 사용법**

##### **1. 인증 및 초기 설정**

Gemini CLI를 실행하면 가장 먼저 어떤 인증 방법을 사용할지 선택할 수 있다.

| 인증 방법 | 특징 | 제한 | 주의 사항 |
| --- | --- | --- | --- |
| Google 로그인 | 무료, 간편함 | 60회/분, 1000회/일 | 입력 데이터가 **Google의 모델 개선에 사용될 수 있음** |
| API 키 | 사용량 기반 과금 | 과금에 따라 제한 | 데이터 보호 보장 (입력 $0.10/100만토큰, 출력 $0.40/100만토큰) |

유의 주의사항을 고려 하고, 처음 사용한다면 Google 로그인만 해도 사용가능하니 API키 발급 없이 써볼 수 있다.

무료 티어의 혜택이 꽤 관대하다.

##### **2. 기본 인터페이스**

Gemini CLI가 실행되면 다음과 같은 인터페이스가 나타난다:

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/cfZ8T7/btsPuRG2OlA/AAAAAAAAAAAAAAAAAAAAABw1bkBeVESztUuGZ4FNWp5QcgxMxdRRJC-oLIAavfKb/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=iuFX%2FYudonaUr2ybgPBo1fpPQVg%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
여기서 `Gemini >` 프롬프트에 자연어로 명령을 입력하거나 슬래시 명령어를 사용할 수 있다.

##### 3. 슬래시 명령어 vs 자연어

Gemini CLI는 두 가지 방식으로 명령을 내릴 수 있다.

**1) 자연어 명령 방식**

# 코딩 작업 관련 요청

```
# 파일 생성/수정
package.json에 새로운 의존성을 추가해줘

# 코드 분석
이 함수에서 성능 병목이 있는지 확인해줘

# 버그 수정
TypeError가 발생하는 이유를 찾아서 고쳐줘
```

**2) 슬래시 명령어**

**2-1) 기본 세션 관리**

```
/clear   # 화면과 대화 기록 초기화 (중요!)
/quit    # CLI 종료
/chat    # 대화 기록 관리 (list|save|resume) 
/compress # 컨텍스트를 요약으로 압축
```

- 여기서 chat은 매우 중요한 편인것 같아 조금 내용을 자세히 살펴 보자.

###### **대화 기록 관리**

`gemini chat` 세션 내에서는 `/chat` 명령어를 통해 대화 기록을 직접 관리할 수 있다. 이는 Claude CLI의 `/clear`나 `/compact`와 유사하게 세션 내에서 컨텍스트를 초기화하거나 관리하는 데 유용하지 않을까?

// 현재 저장된 대화 기록 목록 확인

```
/chat save my-project-feature
```

```
/chat resume my-project-feature
```

- Gemini는 기본적으로는 이전 대화 내용을 기억하고 있지 않다.

ex) 내가 별도의 조치를 취하지 않으면 새로운 세션 마다 내용이 초기화 되는것으로 보인다.

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/JarZc/btsPC4qKvLI/AAAAAAAAAAAAAAAAAAAAAMRZ0cFRC8cCQQsGUzR8J7KlNf2tlhJ0jVsZU1xmcSO9/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=r%2BxgFq9zqMUuwkQddRjFvKf5wPY%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
ex) 기억해줘

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/crYlFV/btsPBKfGoGr/AAAAAAAAAAAAAAAAAAAAAD-3bKcfXGx4m5hJu84DG_YoG2cDL9HL2RLTPEtB_btW/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=5q2%2BUa6Up%2BASc5qcZ6AI6k3b1hg%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
ex) memory.json 에 저장했다고 한다. /memory 라고 하는 영역에 저장된것은 아니다.

다만 아직 /슬래시 명령어가 있는것은 아니지만 의도적으로 몇가지 기억 시킬 수 있는 방법인 것 으로 보인다.

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/phGXn/btsPCj21eMF/AAAAAAAAAAAAAAAAAAAAADwZtniqZThbu2foLWVvQnHpm-xLJaQBBuc2z4ZPzXAJ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=AKsL4h8Zp55LKPdlbBcTf%2BOALJY%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/Fi32Z/btsPBKNxL1j/AAAAAAAAAAAAAAAAAAAAAPmKXRYjGwy9zFneVyuMQUovVM-vYfm-Ti2a7PFYbGJW/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=WSLzmXDXS7qE8SN%2Fxeg8WsyMEKE%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
- Gemini는 기본적으로는 이전 대화 내용을 기억하고 있지 않다.

ex) chat list를 통해 확인해도 내가 의도적으로 기억시킨 내용이 없다.

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/NlC85/btsPBEGy1Fp/AAAAAAAAAAAAAAAAAAAAAA_58Ty-4ez2nj_zwah72_jnzG1NFtO51su7jcWJf2t5/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=xF4M5Q1f9kockmYLQ%2Fdp89zBHNU%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
ex) 그럼 현재 대화 내용이 중요한 경우 저장해보도록 하자.

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/MvElJ/btsPBIa78Rx/AAAAAAAAAAAAAAAAAAAAAF24ii438diDY-z8J82LpzdabmCTH00waAOvYleHIR9V/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=uXdYcb%2B5s%2BjZeDOGhNp5ihB2YtY%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/2qSBk/btsPA0i1UWO/AAAAAAAAAAAAAAAAAAAAAEFmx8Hvr48KGrgVbqh9xC9aMtoa1aj0SV096APuYJl8/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=IqKdmv1PnnxslXz8t6yjzmHWSec%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
ex) 접속을 끊고 다시 gemini ~ 신규 세션 시작 후 물어보기

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/bAQ2GN/btsPBkBzuCt/AAAAAAAAAAAAAAAAAAAAAGGSnpcFduNagG3wf6bAATLrJtFIaUQwDRCCT9XanU8K/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=ugGTV7yB6%2FEAToL82ADnxlBJpII%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
ex) chat list 호출시 이전에 저장한 내용이 보인다. ( memoryjson 으로 저장 되어 버렸다. )

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/kPv0U/btsPBkn5lTg/AAAAAAAAAAAAAAAAAAAAAGECwZB5MRm4Y1QGaNxXjw8tOEAhdD74QcJyICn_UCCn/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=VQuTh9JJAnkH4g71pc5Zi1KRW4c%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
ex) /chat resume으로 이어가보자.

- 이전 대화 내용이 그대로 저장 되어 있다.

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/bkqm0c/btsPAxIroOK/AAAAAAAAAAAAAAAAAAAAABwNDvRJ-NPejc9_7yCX9moP9IM4A8EMq-9hFeKp0z3J/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=dEe99%2Bb%2FMwzy1oCfXevOXDfRq8c%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
ex) 이 테스트 했던 대화 내용은 필요 없으니 제거하고 싶은데, delete 같은 명령어는 또 없다...   

 - 사실 아직 클로드 코드에 비하면 제공되는 슬래시 명령어들이 약한건 사실 이다ㅠ

**삽질 경험: `load`와 `delete` 명령어의 부재**  

다른 CLI 도구에서 흔히 볼 수 있는 `load`나 `delete` 명령어를 `gemini chat` 내에서 찾으려 했지만, 존재하지 않아 당황했다. 특히 저장된 대화 기록을 삭제하는 방법은 없어, 다음 버전 릴리즈를 기다리는 상황이다.   

( 현재 0.1.14 version )

- delete 는 없다는 소리 ㅠ

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/DMM42/btsPBkuQTe6/AAAAAAAAAAAAAAAAAAAAAGZuHaFnqVGp3utdO7LT1hTutjgGwx8OA4T0G2ug5knG/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=uUDSjguUtzMHZTpt90dDbHn2dGo%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
**2-2) 정보 및 도움말**

```
/help     # Gemini CLI 도움말 보기
/docs     # 브라우저에서 전체 문서 열기
/about    # 버전 정보 표시
/stats    # 세션 통계 확인 (/stats model 또는 /stats tools)
/privacy  # 개인정보 처리 방침 표시
```

**2-3) 설정 및 환경**

```
/auth     # 인증 방법 변경
/theme    # 테마 변경
/editor   # 외부 에디터 설정
```

ex) /editor - Gemini CLI가 파일을 수정할 때 터미널 내에서 처리하지 않고, 설정한 외부 에디터로 파일을 열어서 작업할 수 있다.

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/bNIjuz/btsPwCaRdFd/AAAAAAAAAAAAAAAAAAAAALrdaNpyKEr-L4qHDvJMLVShP40ASnS96uozWvts7hyc/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=7veaK3OMD4R8RADKxleKLly9IDQ%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
- 나의 경우에는 동작 하지 않아서 확인해보니 cursor에서 버그가 존재 하는것 같다. 하기링크 참고)

<https://github.com/google-gemini/gemini-cli/issues/2255>

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/k4mzW/btsPwylZQpi/AAAAAAAAAAAAAAAAAAAAALBDeYMJd9p0tHh6cJvGuEPzKZUSyUMXtW4dKcbwC7lG/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=IQS6ugMp0sycphzAq%2Bluy%2Fjjlgs%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
**2-4) 개발 도구**

```
/tools       # 사용 가능한 Gemini CLI 도구 목록
/mcp         # 설정된 MCP 서버와 도구 목록
/extensions  # 활성화된 확장 프로그램 목록
/bug         # 버그 리포트 제출
```

**2-5) 메모리 및 컨텍스트 관리**

```
/memory show     # 현재 메모리 내용 표시
/memory add      # 메모리에 내용 추가
/memory refresh  # 소스에서 메모리 새로고침
/compress        # 컨텍스트를 요약으로 압축
```

**2-6) 키보드 단축키**

```
Enter           # 메시지 전송
Ctrl+J          # 새 줄
Up/Down         # 프롬프트 히스토리 탐색
Alt+Left/Right  # 입력창에서 단어 단위 이동
Shift+Tab       # 자동 승인 편집 토글
Ctrl+Y          # YOLO 모드 토글 (자동 실행) >>>> 생산성을 위해 키고 사용해보자.
Esc             # 작업 취소
Ctrl+C          # 애플리케이션 종료
```

그리고 기본 사용법에서 중요한 것들

```
# @ 기호로 파일/폴더 컨텍스트 추가
@src/myFile.ts

# ! 기호로 쉘 명령어 실행  
!npm run start

# 자연어로 서버 시작
start server
```

**💡 중요한 팁**  

• `/clear`는 정말 중요하다! 컨텍스트가 길어지면 응답 품질이 떨어지니 새 작업 시작할 때마다 사용하자  

• `/compress`로 긴 대화를 요약해서 토큰을 절약할 수 있다  

• `Shift+Tab`으로 자동 승인 모드를 켜면 매번 확인 없이 파일 수정이 가능하다 (상남자 모드!)

**etc)**

클로드에 있는 /model 설정 기능이 없다.

Gemini CLI는 기본적으로 최신 및 프로 모델 "gemini-2.5-pro" 등으로 고정된 상태에서 동작하며,   

내부에서 자동으로 필요 시 다른 모델(예: gemini-2.5-flash)으로 전환 가능하나 CLI 사용자에게   

/model 명령어로 직접 변경 권한을 주는 방식은 현재 공식적으로 지원 안 함이 표준 으로 보인다.

아마 Google이 모델 권한과 비용 관리를 중앙 집중화하는 정책과 관련 있지 않을까?

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/bvKVoK/btsPwJmPQKK/AAAAAAAAAAAAAAAAAAAAAMU8TucxIMw0tdhXWoLUEhgOEc1jcPYgD4jx4TTSU--J/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=tRZj%2BkkAk%2Bb0y5B8cqoPD4eXcmI%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
`/help` 를 통해 가능한 명령어들을 살펴보자. 아마 계속 업데이트가 될 것으로 보인다.

ex) 0.1.13 버전의 /help

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/HL9tO/btsPwE0HDp1/AAAAAAAAAAAAAAAAAAAAACmpv-IH6aJ4dgP6NWNG72WT3UETAbwt_fiuoE_6YSzP/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=aGmZUanDJtnKYb1BntVuPWOg7XA%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
##### **비대화형 프롬프트 전달 방법 : `gemini --prompt`**

단일 질문에 대한 답변을 빠르게 얻고 싶거나, 스크립트에서 Gemini AI를 활용하고 싶을 때 `gemini --prompt` 옵션을 사할 수 있다.  

이 옵션은 프롬프트를 직접 전달하고, AI의 응답만 출력한 뒤 CLI가 종료된다.

이 방식은 `gemini generate`라는 별도의 서브커맨드 없이도 텍스트 생성 기능을 수행하며, 코드 스니펫을 빠르게 얻거나, 간단한 문서 초안을 마련할 때 매우 효율적일 수 있다.

ex) 사실 웹 브라우저 환경이 아닌 개발자들도 많다. 웹 브라우저는 킬 수 없지만, gemini cli가 허용 되어 있다면??(물론 이렇게 잘 허용해주진 않겠지만) 이런식으로도 마치 챗 gpt 처럼 활용 가능하다.

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/zykJH/btsPB2N0NJq/AAAAAAAAAAAAAAAAAAAAAKe2XlzchXdCClE6fa05k0yZIOI49gjUbGYcbgwK6Xev/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=UCeoy%2BgYy%2Fsn58eoAzFQ7I%2BsL40%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
##### **내장 도구들 활용하기**

GEMINI.md 파일은 Gemini CLI가 프로젝트를 이해하는 데 사용하는 "메모리" 역할을 한다.

```
이 프로젝트에 대한 정보를 GEMINI.md 파일로 만들어줘:
- 기술 스택
- 프로젝트 구조  
- 코딩 컨벤션
- 중요한 설정들
```

프로젝트 루트에 GEMINI.md가 있으면 매번 컨텍스트를 설명할 필요가 없다. 팀원들과 공유해서 모든 사람이 같은 컨텍스트로 Gemini CLI를 사용할 수 있다.

Gemini CLI의 진짜 힘은 내장된 도구들에 있다. 이 도구들을 사용하면 파일 읽기, 편집, 검색, 심지어 쉘 명령어 실행까지 자연어로 처리할 수 있다.

| 도구명 | 기능 | 사용 예시 |
| --- | --- | --- |
| `ReadFolder` | 디렉토리 내용 조회 (ls) | 프로젝트 구조 파악 |
| `ReadFile` | 파일 내용 읽기 | 코드 분석, 설정 확인 |
| `ReadManyFiles` | 여러 파일 동시 읽기 | 글로브 패턴 매칭 |
| `FindFiles` | 파일 패턴 검색 (glob) | config.json 찾기 |
| `SearchText` | 텍스트 검색 (grep) | TODO 찾기, 함수 검색 |
| `Edit` | 파일 편집 (diff 적용) | 버그 수정, 기능 추가 |
| `WriteFile` | 새 파일 생성 | README.md 생성 |
| `Shell` | 쉘 명령어 실행 | !npm test 실행 |
| `WebFetch` | 웹 콘텐츠 가져오기 | API 문서 확인 |

##### **파일 참조 방법**

매우 중요한 기능이 아닐까??

Gemini CLI에서 파일이나 추가 정보를 참조하는 다양한 방법들

```
@src/components/UserList.jsx에서 로딩 상태를 추가해줘

# # 기호로 프로젝트 컨텍스트 실시간 추가  
# 이 프로젝트는 React 18 + TypeScript를 사용합니다

# URL로 웹 컨텐츠 참조
https://docs.react.dev/learn 이 문서를 참고해서 Hook을 설명해줘

# 여러 파일 동시 참조
@package.json과 @tsconfig.json을 보고 TypeScript 설정을 최적화해줘

# 디렉토리 전체 참조
@src/utils/ 폴더의 모든 함수에 JSDoc 주석을 추가해줘
```

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/bW4lUi/btsPwyM1Cnw/AAAAAAAAAAAAAAAAAAAAAFtu97huNmuB_wVWPr7REEGecRhkumxBugXYzcFzftM1/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=%2Fi8DifjWZ2TV0Y23bgYRCBizB%2Fk%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
ex) 간단한 명령어로 Gemini CLI가 제대로 동작하는지 확인해보자.

```
# 프로젝트 구조 파악
이 프로젝트의 구조를 설명해줘

# 간단한 파일 생성
Hello World를 출력하는 index.js 파일을 만들어줘
```

![현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)](https://blog.kakaocdn.net/dna/kZ8Rz/btsPvFlU23D/AAAAAAAAAAAAAAAAAAAAAL63MNcr72LKG06P-_teipZzXbSsSPVEhBqS2eDofBik/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1756652399&allow_ip=&allow_referer=&signature=iq92qJkQlNQkzg265ipYQ985rzE%3D)현재 나는 특별하게 변경한게 없으니 2.5 pro 모델로 선택되어 있다. 추윽 하단에는 남은 사용량 표기 (98%)
##### **활용 예시**

##### **코드베이스 탐색하기**

새로운 프로젝트나 팀 코드를 파악할 때 예시

##### **새 기능 개발하기**

기능 요구사항을 자연어로 설명하면 알아서 구현한다.

##### **버그 수정하기**

에러 메시지를 복사해서 붙여넣기만 하면 끝.

###### 🐛 디버깅 예시

```
# 에러 메시지 직접 붙여넣기
TypeError: Cannot read property 'map' of undefined
at UserList.jsx:15:23
이 에러 고쳐줘

# 증상 설명으로 디버깅
API 호출 후 데이터가 렌더링되지 않는 문제가 있어.
네트워크 탭에서는 200 응답이 오는데 화면에 안 뜨네
```

**ex) 활용 예시**  

회사 프로젝트에서 React 컴포넌트의 성능 이슈를 분석할 때, 전체 컴포넌트 구조를 파악하고 리렌더링 문제를 찾아내는 데 10분 정도밖에 걸리지 않았다. 평소라면 코드를 하나하나 읽으면서 30분은 걸렸을 작업이었다.

##### **응용? 활용 버전!**

##### **MCP 서버 연동**

Model Context Protocol(MCP)를 통해 다양한 외부 도구와 연동할 수 있다.

mcp는 너무 중요하니 별도로 진행하고 간단히 예시만 확인.

##### 지원하는 MCP 서버들

* **Google Drive:** 설계 문서나 요구사항 읽기
* **Slack:** 팀 커뮤니케이션 자동화
* **Jira:** 이슈 생성/업데이트
* **Figma:** 디자인 스펙 확인
* **Sentry:** 에러 트래킹

```
{
  "mcpServers": {
    "google-drive": {
      "command": "npx",
      "args": ["@google-drive/mcp-server"],
      "env": {"GOOGLE_APPLICATION_CREDENTIALS": "./credentials.json"}
    },
    "slack": {
      "command": "npx", 
      "args": ["@slack/mcp-server"],
      "env": {"SLACK_BOT_TOKEN": "xoxb-your-token"}
    }
  }
}
```

##### **실시간 로그 모니터링**

Unix 파이프라인과 연동해서 실시간 로그 모니터링도 가능하다.

```
tail -f /var/log/app.log | gemini -p "에러나 warn이 나오면 슬랙으로 알려줘"

# 성능 지표 모니터링
kubectl logs -f deployment/my-app | gemini -p "응답시간이 1초 넘으면 알려줘"

# 배포 로그 분석
docker logs -f container_name | gemini -p "배포 관련 이슈가 있으면 정리해서 알려줘"
```

##### **자주 겪는 문제들과 해결법**

며칠 사용하면서 몇 가지 문제점들을 겪었는데, 대부분 간단하게 해결할 수 있었다.

**🚨 문제 상황: 모델이 자동으로 gemini-2.5-flash로 변경됨**  

무료 티어 사용 중에 할당량 문제로 더 낮은 모델로 자동 전환되는 경우가 있다.

**✅ 해결 방법**  

잠시 기다렸다가 다시 시도하거나, API 키를 설정해서 더 안정적인 서비스를 이용하는 것이 좋다. 디버그 메시지에서 모델 전환을 확인할 수 있다.

**🚨 문제 상황: CLI 시작 시 인증 에러**  

가끔 CLI 실행 시 인증 관련 에러가 발생할 때가 있다.

**✅ 해결 방법**  

`/auth` 명령어로 다시 인증하거나, 브라우저에서 Google 계정 로그아웃 후 재로그인하면 대부분 해결된다.

**🤯 아쉬운 점**  

가끔 API 호출로 인한 지연이 있어서 응답이 느릴 때가 있다. 특히 무료 티어를 사용할 때는 모델이 gemini-2.5-flash로 자동 조정되는 경우가 있어서 답변 품질이 살짝 아쉬울 때도 있었다.

#### **활용 예시 및 주의사항 ⚠️**

##### 터미널 사용 팁

| 키보드 단축키 | 기능 | 설명 |
| --- | --- | --- |
| `Escape` | 작업 중단 | Ctrl+C가 아니다 |

##### 성능 최적화

| 상황 | 권장사항 | 이유 |
| --- | --- | --- |
| 새 작업 시작 | 새 세션 시작 | 컨텍스트 정리, 토큰 절약 |
| 복잡한 작업 | 구체적 요청 | 더 나은 결과 |

18,000줄짜리 React 컴포넌트도 Gemini CLI는 문제없이 수정한다. Cursor 같은 다른 도구들이 헤맬 때도 Gemini CLI는 안정적으로 동작한다. 큰 파일이나 복잡한 작업일수록 Gemini CLI의 장점이 드러난다.

#### **실제 사용 후기와 교훈 💭**

* **워크플로우 변화:** 처음엔 IDE 사이드바로 쓰던 AI가 이제는 메인 인터페이스가 되었다. 코드를 직접 보는 것보다 Gemini에게 먼저 묻게 된다. (한때는 ChatGPT부터 켰지만, 이젠 Gemini부터 키게 된다.)
* **안정성:** Cursor처럼 중간에 멈추거나 patch 해결을 못하는 경우가 거의 없다. 특히 큰 파일 수정할 때 차이가 확실히 난다.
* **러닝 커브:** 터미널 인터페이스라 처음엔 어색했지만, 이 또한 사용할만 하다. 거부감을 갖지 말자! 익숙해진다면 최고의 조력자가 아닐까?
* **무료 티어의 힘:** 분당 60회, 하루 1000회는 개인 개발자에게 충분히 관대하다. 생산성 향상을 고려하면 충분히 가치있다.

권한 확인이 너무 자주 뜬다. 매번 "파일 수정해도 될까요?" 물어본다. 그리고 가끔 컨텍스트가 너무 길어지면 응답이 이상해질 때가 있다. 하지만 발전할 것이다.

#### **자주 묻는 질문 ❓**

A: 개인 개발자나 소규모 프로젝트라면 무료 티어로도 충분합니다. 하루 1000회 요청은 꽤 관대한 편이고, 100만 토큰 컨텍스트도 대부분의 프로젝트를 커버할 수 있습니다.

A: VS Code의 Gemini Code Assist와 동일한 엔진을 사용하지만, 터미널에서 직접 사용할 수 있어서 IDE를 벗어난 작업에도 활용할 수 있습니다. 특히 서버 관리나 스크립트 작업에 유용합니다.

A: Claude Code는 유료 구독이 필요하지만 Gemini CLI는 관대한 무료 티어를 제공합니다. 기능적으로는 비슷하지만 Google 생태계와의 연동성이 장점입니다.

A: Gemini 모델 자체가 다양한 언어를 지원하므로 Python, JavaScript, Java, Go, Rust 등 대부분의 주요 언어를 사용할 수 있습니다. 특히 웹 개발 관련 작업에서 뛰어난 성능을 보입니다.

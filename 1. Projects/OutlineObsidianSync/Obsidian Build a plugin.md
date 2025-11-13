## 1단계: 샘플 플러그인 다운로드

Obsidian이 플러그인을 인식할 수 있도록 `.obsidian/plugins` 디렉터리에 샘플 플러그인을 다운로드합니다.

1. 터미널에서 `plugins` 디렉터리로 이동

```bash
cd path/to/vault
mkdir -p .obsidian/plugins
cd .obsidian/plugins
```

2. Git을 사용하여 샘플 플러그인 클론

```bash
git clone https://github.com/obsidianmd/obsidian-sample-plugin.git
```

📌 **참고:** 해당 저장소는 GitHub 템플릿 저장소입니다. 개인 저장소를 만들고 싶다면, [GitHub 문서](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template)를 참고하세요.

---

## 2단계: 플러그인 빌드

Obsidian이 플러그인을 로드할 수 있도록 소스 코드를 컴파일합니다.

1. 플러그인 디렉터리로 이동

```bash
cd obsidian-sample-plugin
```

2. 필요한 패키지 설치

```bash
npm install
```

3. 소스 코드 컴파일

```bash
npm run dev
```

🔹 이 명령어는 터미널에서 실행된 상태로 유지되며, 코드 수정 시 자동으로 다시 빌드됩니다.

---

## 3단계: 플러그인 활성화

Obsidian에서 플러그인을 사용하려면 설정에서 활성화해야 합니다.

1. Obsidian에서 **설정(Settings)** 을 엽니다.
2. 사이드 메뉴에서 **커뮤니티 플러그인(Community plugins)** 을 선택합니다.
3. **커뮤니티 플러그인 활성화(Turn on community plugins)** 를 선택합니다.
4. **설치된 플러그인(Installed plugins)** 목록에서 **Sample Plugin** 을 활성화합니다.

✅ 이제 플러그인을 사용할 준비가 되었습니다.

---

## 4단계: 플러그인 정보 업데이트

플러그인의 이름을 변경하려면 `manifest.json` 파일을 수정해야 합니다.

1. `manifest.json` 파일을 코드 편집기로 엽니다.
2. `id` 값을 `"hello-world"` 로 변경합니다.
3. `name` 값을 `"Hello world"` 로 변경합니다.
4. 플러그인 폴더 이름을 `id` 값과 동일하게 변경합니다.
5. Obsidian을 재시작 하여 변경 사항을 반영합니다.

✅ **설치된 플러그인 목록에서 새로운 이름으로 업데이트된 것을 확인할 수 있습니다.**  
📌 `manifest.json`을 수정한 후에는 반드시 **Obsidian을 재시작해야 변경사항이 반영됩니다.**

---

## 5단계: 플러그인 코드 수정

플러그인에 **리본 아이콘을 추가하고 클릭하면 인사 메시지를 출력하도록 수정**합니다.

1. `main.ts` 파일을 엽니다.
2. 클래스 이름을 `MyPlugin`에서 `HelloWorldPlugin`으로 변경합니다.
3. `obsidian` 패키지에서 `Notice`를 가져옵니다.

```ts
import { Notice, Plugin } from 'obsidian';
```

4. `onload()` 메서드에 다음 코드를 추가합니다.

```ts
this.addRibbonIcon('dice', 'Greet', () => {
  new Notice('Hello, world!');
});
```

5. **Obsidian을 새로고침하여 플러그인 변경사항을 반영합니다.**
    
- 방법 1: 커맨드 팔레트에서 Reload app without saving 실행
- 방법 2: 커뮤니티 플러그인 패널에서 플러그인을 비활성화 후 다시 활성화

✅ 이제 Obsidian의 왼쪽 리본에 🎲 (주사위) 아이콘이 생성되며, 클릭하면 "Hello, world!" 메시지가 표시됩니다.

📌 **Hot Reload 기능**을 원하면, [Hot-Reload 플러그인](https://github.com/pjeby/hot-reload)을 설치하면 플러그인 변경 사항을 자동으로 반영할 수 있습니다.

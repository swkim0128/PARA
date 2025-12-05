## 1. Obsidian 플러그인 개요

Obsidian은 JavaScript 및 TypeScript로 작성된 플러그인을 지원하며, 플러그인을 통해 다양한 기능을 확장할 수 있습니다. 플러그인은 `manifest.json`, `main.js`(또는 `main.ts`), 그리고 선택적으로 `styles.css`로 구성됩니다.

---
## Obsidian 플러그인 개발환경 설정

## 2. 플러그인 기본 구조

### 2.1 프로젝트 폴더 구조

```plaintext
obsidian-plugin/
 ├── .gitignore
 ├── manifest.json
 ├── main.js (또는 main.ts)
 ├── styles.css (선택 사항)
 ├── package.json
 ├── tsconfig.json (TypeScript 사용 시)
 ├── src/
 │   ├── main.ts
 │   ├── settings.ts (설정 UI 추가 시)
 │   ├── api.ts (API 연동 시)
```

### 2.2 `manifest.json` 파일 구성

```json
{
  "id": "outline-sync",
  "name": "Outline Sync",
  "version": "1.0.0",
  "author": "Your Name",
  "minAppVersion": "0.12.0",
  "description": "Outline과 Obsidian을 동기화하는 플러그인",
  "isDesktopOnly": false
}
```

### 2.3 `main.ts` 파일 기본 구성

```typescript
import { Plugin } from 'obsidian';

export default class OutlineSyncPlugin extends Plugin {
  async onload() {
    console.log('Outline Sync Plugin Loaded');
    // 추가 기능 로드
  }

  onunload() {
    console.log('Outline Sync Plugin Unloaded');
  }
}
```

---

## 3. Obsidian 플러그인 개발 주요 기능

### 3.1 설정 UI 추가하기

```typescript
import { App, PluginSettingTab, Setting } from 'obsidian';

interface OutlineSyncSettings {
  apiUrl: string;
  personalToken: string;
}

const DEFAULT_SETTINGS: OutlineSyncSettings = {
  apiUrl: '',
  personalToken: ''
};

export default class OutlineSyncPlugin extends Plugin {
  settings: OutlineSyncSettings;

  async onload() {
    await this.loadSettings();
    this.addSettingTab(new OutlineSyncSettingTab(this.app, this));
  }

  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }

  async saveSettings() {
    await this.saveData(this.settings);
  }
}

class OutlineSyncSettingTab extends PluginSettingTab {
  plugin: OutlineSyncPlugin;

  constructor(app: App, plugin: OutlineSyncPlugin) {
    super(app, plugin);
    this.plugin = plugin;
  }

  display(): void {
    let { containerEl } = this;
    containerEl.empty();

    new Setting(containerEl)
      .setName('API URL')
      .setDesc('Outline API의 URL을 입력하세요')
      .addText(text => text
        .setValue(this.plugin.settings.apiUrl)
        .onChange(async (value) => {
          this.plugin.settings.apiUrl = value;
          await this.plugin.saveSettings();
        }));
  }
}
```

### 3.2 파일 저장 이벤트 감지 및 처리

```typescript
this.registerEvent(
  this.app.vault.on('modify', (file) => {
    console.log(`${file.path} was modified.`);
    // Outline API 업데이트 로직 추가
  })
);
```

### 3.3 API 호출 예제 (Outline 연동)

```typescript
async function fetchOutlineDocuments(apiUrl: string, token: string) {
  const response = await fetch(`${apiUrl}/documents.list`, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  });
  return response.json();
}
```

---

## 4. Obsidian 플러그인 개발 및 배포

### 4.1 개발 환경 설정

```bash
npm init -y
npm install obsidian
npm install typescript --save-dev
```

### 4.2 빌드 및 실행

```bash
tsc
cp manifest.json dist/
cp main.js dist/
```

### 4.3 플러그인 설치 및 테스트

1. `dist/` 폴더를 Obsidian 플러그인 폴더 (`.obsidian/plugins/outline-sync/`)에 복사합니다.
2. Obsidian에서 플러그인을 활성화합니다.

### 4.4 GitHub 배포 및 Obsidian 커뮤니티 등록

1. GitHub에 저장소를 생성하고 코드를 업로드합니다.
2. Obsidian 공식 플러그인 저장소에 등록을 요청합니다.

---

## 5. 향후 개선 사항

- UI 개선 및 사용자 경험 최적화
- 동기화 충돌 관리 로직 추가
- 다중 계정 지원 기능 고려

이 문서는 Obsidian 플러그인 개발을 위한 기본적인 가이드를 제공하며, Outline과의 동기화를 중심으로 기능을 확장할 수 있도록 구성되었습니다.

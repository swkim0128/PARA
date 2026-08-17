## **🔗 Notion 연동**

> ⚠️ **2026-08-17 방향 전환** — 옛 "Notion → PARA 단방향, 직접 편집 금지" 규약은 폐기됐다. 이제 **볼트가 실질 SoT**이고 노션은 상태 인덱스이며, 이 문서는 직접 편집한다. 규칙 정본 → `02.Areas/07.개인관리/05.프로젝트.md`
> 자동 동기화는 2026-05-19 이후 정지 상태 — 아래 값은 수동 갱신한다.

- **Notion ID**: [PRO-73](https://www.notion.so/83e67ee556a44be9b257fea9b3fd9ffa) (노션 페이지명: `법안 git graph (legigraph)` ↔ 볼트 폴더: `01.Projects/02.legigraph/`)
- **Status**: Paused
- **Priority**: 중간
- **Tags**: 개인, 사이드 프로젝트
- **Start Date**: 2024-12-23
- **End Date**: _(미정)_
- **연결된 Tasks**: 11건 (노션 페이지에서 확인)

## **📌 프로젝트 개요**

LegiGraph는 대한민국 국회의 법안 변화를 Git Graph 형식으로 시각화하는 웹 애플리케이션입니다. 사용자는 특정 법안의 발의 내역, 버전 히스토리, 입법 절차 등을 시각적으로 탐색할 수 있으며, 각 버전 간의 차이도 비교할 수 있습니다.

---

## **🧱 기술 스택**

- **프레임워크**: Next.js 15 (App Router 기반, SSR)
- **스타일링**: Tailwind CSS
- **빌드 도구**: Vite
- **컴포넌트 문서화**: Storybook
- **형상 관리**: Git, GitHub
- **디자인 시스템**: Atomic Design Pattern 적용
- **디자인 툴**: Figma (AI 기반 프로토타이핑)

---

## **🛠 초기 개발 세팅**

### **1. 프로젝트 디렉터리 구성**

```
legigraph/
├── frontend/
│   ├── app/
│   ├── components/
│   │   ├── atoms/
│   │   ├── molecules/
│   │   └── organisms/
│   ├── public/
│   ├── styles/
│   ├── .storybook/
│   └── tsconfig.json
```

### **2. 주요 패키지 설치**

```
# 필수 패키지
npm install next react react-dom

# 타입스크립트 및 타입 정의
npm install -D typescript @types/react @types/node

# Tailwind CSS 설정
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Vite 설정
npm install -D vite @vitejs/plugin-react vite-tsconfig-paths

# Storybook 설정
npm install -D storybook @storybook/react @storybook/addon-essentials @storybook/experimental-nextjs-vite
```

### **3. Tailwind 설정**

**tailwind.config.ts**

```
export default {
  content: ["./app/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

**postcss.config.mjs**

```
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

### **4. Storybook 설정**

**.storybook/main.ts**

```
import type { StorybookConfig } from "storybook";
const config: StorybookConfig = {
  framework: {
    name: "@storybook/experimental-nextjs-vite",
    options: {},
  },
  stories: ["../components/**/*.stories.@(ts|tsx)"],
  addons: ["@storybook/addon-essentials"],
};
export default config;
```

**.storybook/preview.ts**

```
import "../styles/globals.css";
export const parameters = {
  actions: { argTypesRegex: "^on[A-Z].*" },
  controls: {
    matchers: {
      color: /(background|color)$/i,
      date: /Date$/,
    },
  },
};
```

---

## **⚙️ 컴포넌트 설계 (Atomic Design 기반)**

### **Atoms**

- Button, Input, Checkbox, Radio, Select, Textarea
- Label, Icon (Lucide 기반), Badge
- Image, Avatar, Tooltip, Divider, Spinner, Skeleton, Text, Link

### **Molecules**

- FormField, AvatarWithText, ImageCard
- CheckboxGroup, RadioGroup
- TooltipWrapper, SpinnerOverlay

### **Organisms**

- 공통 UI: Header, Footer, Sidebar
- 그래프 관련 UI: GraphCanvas, GraphNodeDetailPanel, VersionComparisonPanel
- 리스트 및 정보: BillList, VersionTimeline, ProcessTracker, LegislatorProfile
- 상호작용 요소: SearchBar, FilterPanel, TabSwitcher
- 기타 유틸리티: NotificationToast, Modal

---

## **📚 Storybook 구조**

- 각 컴포넌트는 *.stories.tsx로 별도 디렉토리(stories/atoms, stories/molecules, stories/organisms)에 분리하여 관리
- useArgs 대신 상태를 Storybook에서 직접 props로 제어하거나 useState 활용 가능
- 컴포넌트 props는 interface로 통일, 기본적으로 BaseComponentProps를 상속하여 testId, className 제공

---

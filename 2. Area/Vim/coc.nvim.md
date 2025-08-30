
언어 지원을 추가하는 방법은 아주 간단합니다. Vim의 명령 모드에서 `:CocInstall` 다음에 설치하고 싶은 확장 프로그램 이름을 입력하면 됩니다.  
예를 들어, TypeScript와 JavaScript 지원을 설치하고 싶다면 아래와 같이 입력합니다.

Vim Script

```
:CocInstall coc-tsserver
```

---

## 주요 프로그래밍 언어별 `coc.nvim` 확장 목록

개발에 많이 사용되는 언어들을 중심으로 추천 확장 목록을 정리해 드릴게요. 필요한 언어를 찾아 설치해 보세요!

### 🌐 웹 개발 (JavaScript, TypeScript, HTML, CSS, JSON)

**JavaScript/TypeScript**: `coc-tsserver` (가장 기본적인 웹 개발 확장입니다)

```
:CocInstall coc-tsserver
```

**HTML**: `coc-html`

```
:CocInstall coc-html
```

**CSS/SCSS/Less**: `coc-css`

```
:CocInstall coc-css
```

**JSON**: `coc-json` (기본적으로 내장되어 있거나, 추천 확장으로 쉽게 설치 가능)

```
:CocInstall coc-json
```

**Prettier (코드 포맷터)**: `coc-prettier` (코드 정리를 위해 강력 추천합니다)

```
:CocInstall coc-prettier
```

**ESLint (코드 린터)**: `coc-eslint`

```
:CocInstall coc-eslint
```

### 🐍 Python

**Pyright**: `coc-pyright` (Microsoft에서 개발한 빠르고 안정적인 타입 체커 및 언어 서버)

```
:CocInstall coc-pyright
```

_참고: 과거에는 `coc-python`도 많이 사용되었지만, 현재는 `coc-pyright`가 더 나은 성능으로 인해 널리 추천됩니다._

### ⚙️ C / C++ / Objective-C

**Clangd**: `coc-clangd` (LLVM 프로젝트의 공식 언어 서버로, 가장 강력한 기능을 제공)

```
:CocInstall coc-clangd
```

_설치 후 `:CocCommand clangd.install` 명령어로 clangd 바이너리를 설치해야 할 수도 있습니다._

### ☕ Java

**Java**: `coc-java` (Eclipse JDTLS 기반의 언어 서버)

```
:CocInstall coc-java
```

### 🐹 Go

**Go**: `coc-go` (공식 Go 언어 서버인 `gopls`를 사용)

```
:CocInstall coc-go
```

### 🦀 Rust

**Rust Analyzer**: `coc-rust-analyzer` (Rust 공식 언어 서버)

```
:CocInstall coc-rust-analyzer
```

### 🐘 PHP

**PHP**: `coc-phpls`

```
:CocInstall coc-phpls
```

### 💎 Ruby

**Ruby**: `coc-solargraph`

```
:CocInstall coc-solargraph
```

### 📜 셸 스크립트 (Shell Script)

**Bash**: `coc-sh`

```
:CocInstall coc-sh
```

### 🔧 기타 유용한 확장

**YAML**: `coc-yaml`

```
:CocInstall coc-yaml
```

**Docker**: `coc-docker`

```
:CocInstall coc-docker
```

**Terraform**: `coc-terraform`

```
:CocInstall coc-terraform
```

**SQL**: `coc-sql`

```
:CocInstall coc-sql
```

---

## 확장 프로그램 직접 검색하기

더 많은 언어나 도구를 찾고 싶으시다면 `coc-marketplace`를 사용해 보세요.

1. **Marketplace 설치**:

```
:CocInstall coc-marketplace
```

2. **Marketplace 실행**:

```
:CocList marketplace
```

이 명령을 실행하면 설치 가능한 모든 확장 프로그램의 목록이 나타납니다. 여기서 원하는 확장을 검색하고 바로 설치할 수 있습니다.

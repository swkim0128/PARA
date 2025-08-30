## macOS Vim 설정 가이드

### 1. Vim 설치

macOS에는 기본 Vim이 있지만, 최신 버전 사용을 권장합니다.

```bash
vim --version
brew install vim
```

### 2. 설정 파일 위치

Vim 설정은 홈 디렉토리의 `.vimrc` 파일에 저장됩니다.

```bash
touch ~/.vimrc
```

### 3. 기본 설정 예시 (`~/.vimrc`)

```vim
" 기본 인코딩
set encoding=utf-8

" 줄 번호 표시
set number

" 탭 설정
set tabstop=4
set shiftwidth=4
set expandtab

" 검색 시 실시간 하이라이트
set hlsearch
set incsearch
set ignorecase
set smartcase

" 줄 바꿈 시 보기 좋게
set wrap
set linebreak

" 상태줄에 파일 정보 표시
set ruler
set showcmd

" 괄호 짝 자동 표시
set showmatch

" 백업, 스왑파일 생성 방지
set noswapfile
set nobackup

" 클립보드 연동 (macOS)
set clipboard=unnamed

" 컬러 스킴
syntax on
colorscheme desert
```

### 4. 플러그인 매니저 설치: vim-plug

```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
     https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

### 5. 플러그인 설정 예시

```vim
call plug#begin('~/.vim/plugged')

Plug 'preservim/nerdtree'
Plug 'junegunn/fzf.vim'
Plug 'tpope/vim-commentary'
Plug 'vim-airline/vim-airline'
Plug 'morhetz/gruvbox'

call plug#end()
```

Vim 실행 후 다음 명령어 입력:

```vim
:PlugInstall
```

### 6. 테마 설정

```vim
syntax on
colorscheme gruvbox
```

### 7. 주요 사용 명령

- 파일 트리 열기: `:NERDTreeToggle`
- 주석 토글: Visual 모드에서 `gcc` (vim-commentary 필요)
- 파일 검색: `:Files` (fzf 필요)

### 8. 설정 파일 경로 정리

| 항목                            | 경로                                      |
| ----------------------------- | --------------------------------------- |
| Vim 설정 파일                     | `~/.vimrc`                              |
| 플러그인 디렉토리                     | `~/.vim/plugged`                        |
| vim-plug 설치 경로                | `~/.vim/autoload/plug.vim`              |

### 9. 설정 iCloud에 동기화하기

1. iCloud Drive에 dotfiles 폴더 생성

```bash
mkdir -p ~/Library/Mobile\ Documents/com~apple~CloudDocs/dotfiles
mv ~/.vimrc ~/Library/Mobile\ Documents/com~apple~CloudDocs/dotfiles/
ln -s ~/Library/Mobile\ Documents/com~apple~CloudDocs/dotfiles/.vimrc ~/.vimrc
```

2. 다른 Mac에서 같은 경로에 심볼릭 링크만 만들면 설정이 자동 적용됨

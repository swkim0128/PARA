전체적인 과정은 다음과 같습니다.

1. **vim-plug 설치하기**: 플러그인을 쉽게 설치하고 관리할 수 있게 해주는 도구입니다.
2. **.vimrc 설정 파일 작성하기**: Vim의 모든 설정을 관리하는 파일입니다. 여기에 기본 설정과 플러그인 목록을 추가할 겁니다.
3. **플러그인 설치하기**: 설정 파일에 명시된 플러그인들을 Vim 내에서 간단한 명령어로 설치합니다.

---

## vim-plug 설치하기

먼저, 터미널을 열고 아래 명령어를 실행하여 `vim-plug`를 설치해 주세요. 운영체제에 맞는 명령어를 사용하시면 됩니다.

### macOS 또는 Linux

Bash

```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

### Windows (PowerShell):

PowerShell

```bash
iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |`
    ni $HOME/vimfiles/autoload/plug.vim -Force
```

---

## .vimrc 설정 파일 작성하기

```plain text
" =============================================================================
" # 플러그인 목록 (vim-plug)
" =============================================================================
call plug#begin('~/.vim/plugged')

" 테마 및 외형
Plug 'dracula/vim', { 'as': 'dracula' } " Dracula 테마
Plug 'ryanoasis/vim-devicons' " 파일 탐색기 아이콘
Plug 'vim-airline/vim-airline' " 상태 표시줄
Plug 'vim-airline/vim-airline-themes' " 상태 표시줄 테마

" 파일 탐색기
Plug 'preservim/nerdtree' " 파일 트리 탐색기
Plug 'Xuyuanp/nerdtree-git-plugin' " NERDTree Git 상태 표시

" 코드 자동 완성 및 문법 검사
Plug 'neoclide/coc.nvim', {'branch': 'release'} " 자동 완성 엔진

" 생산성 및 유틸리티
Plug 'tpope/vim-fugitive' " Git 연동
Plug 'tpope/vim-commentary' " 주석 처리
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } } " 파일 퍼지 파인더
Plug 'junegunn/fzf.vim' " fzf Vim 연동
Plug 'preservim/tagbar' " 코드 구조(함수, 클래스 등) 표시
Plug 'jiangmiao/auto-pairs' " 괄호 자동 쌍 맞춤

call plug#end()


" =============================================================================
" # 기본 설정
" =============================================================================
" 인코딩 설정
set encoding=utf-8

" 줄 번호 표시
set number

" 절대 줄 번호와 상대 줄 번호 함께 사용
set relativenumber

" 구문 강조 사용
syntax on

" 검색 시 대소문자 무시 (단, 대문자가 포함되면 구분)
set ignorecase
set smartcase

" 들여쓰기 설정
set tabstop=4       " 탭 크기 4칸
set shiftwidth=4    " 자동 들여쓰기 4칸
set expandtab       " 탭을 공백으로 변환
set autoindent      " 자동 들여쓰기

" 화면 분할 시 아래쪽, 오른쪽에 새 창 생성
set splitbelow
set splitright

" 마우스 사용 허용
set mouse=a

" 입력 중 검색 결과 바로 보여주기
set incsearch

" 항상 상태 표시줄 표시
set laststatus=2

" 명령어 입력 줄 높이
set cmdheight=1

" 숨김 버퍼 사용 (저장하지 않은 채로 다른 파일로 이동 가능)
set hidden

" 백업 파일 및 스왑 파일 생성 안 함
set nobackup
set noswapfile


" =============================================================================
" # 플러그인 설정
" =============================================================================
" Dracula 테마 설정
if (has("termguicolors"))
 set termguicolors
endif
colorscheme dracula

" NERDTree (파일 탐색기)
" F2 키로 NERDTree 토글
nnoremap <F2> :NERDTreeToggle<CR>
" Vim 시작 시 파일이 없으면 NERDTree 자동 실행
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" CoC (자동 완성)
" Tab으로 자동 완성 항목 선택
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" fzf (퍼지 파인더)
" Ctrl+P로 파일 검색
nnoremap <C-p> :Files<CR>
" Ctrl+B로 버퍼 검색
nnoremap <C-b> :Buffers<CR>

" Tagbar (코드 구조 보기)
" F3 키로 Tagbar 토글
nnoremap <F3> :TagbarToggle<CR>

" vim-airline (상태 표시줄)
let g:airline_powerline_fonts = 1 " 파워라인 폰트 사용
let g:airline#extensions#tabline#enabled = 1 " 탭 라인 확장
let g:airline_theme = 'dracula' " Dracula 테마 적용
```

---

## 플러그인 설치 및 적용

1. 위에서 수정한 `.vimrc` 파일을 저장하고 Vim을 다시 시작하세요.
2. Vim을 시작하면 `vim-plug`가 설치되지 않은 플러그인이 있다는 메시지를 보여줄 수 있습니다.
3. Vim 명령 모드에서 아래 명령어를 입력하고 실행하세요.

Vim Script
```
:PlugInstall
```

4. 새로운 창이 열리면서 `.vimrc`에 명시된 플러그인들이 자동으로 설치됩니다.
5. 설치가 완료되면 Vim을 다시 시작하면 모든 설정과 플러그인이 적용됩니다.

---

## 주요 기능 및 단축키 요약

- **테마**: 어두운 배경의 **Dracula** 테마가 적용됩니다.
- **파일 탐색기 (NERDTree)**: `<F2>` 키를 눌러 파일 탐색기를 열고 닫을 수 있습니다.
- **코드 구조 보기 (Tagbar)**: `<F3>` 키를 눌러 현재 파일의 함수나 클래스 목록을 볼 수 있습니다.
- **빠른 파일 검색 (fzf)**: `<Ctrl-P>`로 프로젝트 내 파일을 빠르게 검색하여 열 수 있습니다.
- **Git 연동 (vim-fugitive)**: `:Git` 또는 `:G`로 시작하는 다양한 Git 명령어를 Vim 내에서 바로 사용할 수 있습니다. (예: `:G blame`, `:G status`)
- **자동 완성 (coc.nvim)**: 코드를 작성하면 자동으로 완성 목록이 나타납니다. `Tab` 키로 항목을 선택할 수 있습니다.
    - **추가 설정**: `coc.nvim`은 더 강력한 기능을 위해 언어 서버를 설치해야 합니다. 예를 들어, JavaScript/TypeScript 개발을 한다면 Vim에서 다음 명령어를 실행하세요.
	
```
:CocInstall coc-tsserver
```

다른 언어는 [CoC 마켓플레이스](https://www.google.com/search?q=https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions%23implemented-coc-extensions)를 참고하여 필요한 `coc-*` 확장을 설치하시면 됩니다.
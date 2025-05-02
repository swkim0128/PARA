# Git의 새로운 기본 Merge 전략 Ort

![rw-book-cover](http://blog.outsider.ne.kr/skin/blog/anti_verbose/images/title-image.jpg)

## Metadata
- Author: [[Textcube]]
- Full Title: Git의 새로운 기본 Merge 전략 Ort
- Category: #articles
- Document Tags:  #git 
- Summary: Git 2.34부터 새로운 기본 Merge 전략인 ort가 도입되었다. 이 전략은 기존의 resolve 전략과 recursive 전략을 대체하고, 더 빠르고 효율적인 머지를 가능하게 한다. ort는 파일 이름 변경을 탐지하고 처리할 수 있으며, 이름이 변경된 파일을 찾아내는 작업을 최적화하여 더 빠른 머지를 가능하게 한다. 새로운 전략에는 몇 가지 제약사항이 있지만, 이를 대부분 해결할 수 있도록 최적화 작업이 이루어졌다. 이로써 ort는 Git의 기본 머지 전략으로 사용되고 있으며, 이전의 recursive 전략에 비해 더욱 효율적이고 안정적인 머지를 가능하게 한다.

## Full Document
[[Full Document Contents/Git의 새로운 기본 Merge 전략 Ort.md|See full document content →]]

## Highlights
- `resolve` 전략
  Git이 2개의 브랜치를 머지할 때 변경 사항을 합치기 위해 여러 가지 전략 중 하나를 선택한다. 원래의 전략은 [3-way merge](https://en.wikipedia.org/wiki/Merge_(version_control)#Three-way_merge) 알고리즘을 사용하는 `resolve` 전략을 사용했다.
  3-way merge는 A 파일과 B 파일의 차이점을 분석한 후 두 파일의 공통 조상인 C 까지 고려해서 합칠 변경 사항을 구성하고 A, B, C 셋 다 다른 경우는 충돌(Conflict)로 표시해서 사용자가 해결하도록 한다. ([View Highlight](https://read.readwise.io/read/01hq2hc7sqpwbf9b34qevad3er))
    - Note: 3-way merge 전략
- `recursive` 전략
  Git이 만들어진 초기인 2005년에 `resolve` 전략은 `recursive`라는 전략으로 [교체](https://github.com/git/git/commit/fbf8ac212caa74fc506434da83f8e9630b09ed12)된다. 이렇게 `recursive`로 바꾼 주요 이유는 머지할 두 브랜치가 공통된 조상이 없는 경우에도 각 브랜치에서 그 이름대로 재귀적으로 머지할 수 있어서 `resolve` 전략에서 충돌하는 경우에도 머지할 수 있고 한 브랜치에서는 파일이 수정되고 다른 브랜치에서는 파일명이 변경된 경우에도 이를 감지할 수 있기 때문이다. ([View Highlight](https://read.readwise.io/read/01hq2hdfj5m2bdqeetz94wkbeh))
    - Note: resolve 전략에서 recursive 전략으로 깃 머지 전략이 바뀜
      2005년 이후 쭉 사용
- `ort` 전략
  `ort`는 재귀(recursion)와 파일이름 변경 탐지를 하는 `recursive`와 같은 컨셉을 가지고 처음부터 새로 작성된 전략이다. 그래서 ort라는 이름도 Ostensibly Recursive’s Twin의 약자로 표면적으로는 Recursive의 쌍둥이라는 의미이고 이전에 비해 [훨씬 빨라졌다](https://lore.kernel.org/git/4a0f088f3669a95c7f75e885d06c0a3bdaf31f42.1628055482.git.gitgitgadget@gmail.com/). ([View Highlight](https://read.readwise.io/read/01hq2hfe7ftjs3x0bxxwqy1tv0))
    - Note: recursive 전략에서 새롭게 생긴 git merge 전략

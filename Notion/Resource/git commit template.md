---
type: Git
archive: false
---
### git commit template

```Bash
$ git config --global commit.template ~/git_commit_template.txt

or

# .gitconfig
[commit]
template=~/git_commit_template.txt

# 레포지토리별
# repository/.git/config
[commit]
template=repository/git_commit_template.txt
```

  

- 내가 사용하는 commit template

```Plain
# Header <Type>:<Title>

# -- Type -- 
# ENG  : 개선하거나 신기능 추가 (Engancement)
# BUG  : 버그
# DOC  : 문서화 관련된 작업 (Document)
# TST  : 새로운 유닛테스트를 추가하거나 기존 테스트를 수정 (Test)
# BLD  : 빌드 프로세스 관련 코드 혹은 스크립트를 수정 (Build)
# PERF : 계산 속도의 개선과 관련된 작업 (Performance)
# CLN  : 코드를 정리하거나 리팩토링한 작업 (Cleanup)
# ---

# Text

# Footer

# Commit Message rule
# 1. 제목 줄은 50자 내로 작성.
# 2. 제목 첫 글자를 대문자로
# 3. 제목은 명령문으로
# 4. 제목 끝에 마침표(.) 금지
# 5. 본문은 한 줄 당 72자 내로 작성한다.
# 6. 본문 내용은 양에 구애받지 않고 최대한 상세히 작성한다.
# 7. 본문은 "어떻게" 보다 "무엇을", "왜"를 설명한다.
# 8. 꼬리말에는 이슈 트래커를 작성한다.
# 9. 꼬리말은 "유형:#이슈번호" 형식으로 작성한다.
```
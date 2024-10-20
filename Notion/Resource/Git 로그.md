---
type: Git
archive: false
---
## Git Log

### 주요 옵션

  

### log Format

```Bash
# git log 명령어
git log --graph --all --pretty="%C(auto)%h%Creset -%C(auto)%d%Creset %s %C(bold blue)<%an>%Creset %Cgreen(%cr)”
```

```Bash
# git alias 등록
git config --global alias.lg 'log --graph --all --pretty="%C(auto)%h%Creset -%C(auto)%d%Creset %s %C(bold blue)<%an>%Creset %Cgreen(%cr)"'
```
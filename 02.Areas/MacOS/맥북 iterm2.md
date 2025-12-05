## 📦 iTerm2 설정을 iCloud로 동기화하는 방법

### ✅ 1. iCloud Drive 경로 확인

iCloud Drive는 일반적으로 다음 위치에 있습니다:

```
~/Library/Mobile Documents/com~apple~CloudDocs
```

혹은 Finder에서 iCloud Drive > 원하는 폴더에 접근해도 됩니다.

예: ~/Library/Mobile Documents/com~apple~CloudDocs/iTerm2Prefs

### ✅ 2. 기존 맥북에서 설정 동기화 설정

1. iTerm2 실행
2. 메뉴에서 iTerm2 > Settings (또는 Preferences) 클릭
3. General > Preferences 탭으로 이동
4. 아래 항목 설정:
    - **✔ Load preferences from a custom folder or URL** 체크
    - 폴더 위치를 다음 중 하나로 설정:

```
~/Library/Mobile Documents/com~apple~CloudDocs/iTerm2Prefs
```

또는 Finder에서 iCloud Drive에 적절한 폴더 생성 후 경로 지정

- Save changes to folder when iTerm2 quits 체크

5. iTerm2를 종료 후 다시 실행

이제 설정 파일들이 iCloud Drive에 저장되며, 다른 장비에서도 불러올 수 있습니다.

### ✅ 3. 새 맥북에서 설정 적용

1. iTerm2 설치 및 실행
2. iTerm2 > Preferences > General > Preferences 탭으로 이동
3. ✔ Load preferences from a custom folder or URL 체크
4. 동일한 iCloud Drive 경로 지정:

```
~/Library/Mobile Documents/com~apple~CloudDocs/iTerm2Prefs
```

5. iTerm2 재시작

모든 설정이 자동으로 불러와집니다.

---

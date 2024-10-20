---
type: Django
archive: false
---
## 프로젝트 및 앱의 구조와 설정

### pyenv와 가상환경

### Django 설치

### Django 프로젝트 및 앱 구조

**기본 디렉토리 및 파일 구조**

---

```Bash
# 해당 project 디렉터리에서 명령어를 입력하여 생성한다.
django-admin startproject config .
```

```Plain
project
├── config
│		├── __init__.py
│		├── asgi.py
│		├── settings.py
│		├── urls.py
│		└── wsgi.py
├── userapp
```

**settings.py**

django core에서 사용할 수 있는 전역 설정 목록과 기본값이 설정된 파일

**urls.py**

urlpatterns 리스트의 항목(엔드포인트, 대상)에 따라 request를 라우팅 한다.  
위 항목에서는 엔드포인트가 admin/인 request에 대해서는 장고 기본 admin urls을,  
엔드포인트가 없는 request에 대해서는 users라는 앱의 urls를 라우팅한다.  

  

**Django 앱 구조**

---

```Bash
# 위 프로젝트에서 users 패키지에 해당하는 앱
python manage.py startapp accounts
```

```Plain
project
├── UserDefinedApp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py

Django 버전 1.9부터 애플리케이션의 설정 클래스를 정의하는 apps.py 파일이 추가되었다.
```

장고는 MVC(Model-View-Controller)를 기반으로 한 프레임워크다.  
하지만 장고에서는 같은 개념을 MTV(Model - Template - View)라고 부른다.  

**models.py**

앱에서 사용하기 위한 데이터 베이스 테이블을 ORM문법에 의거하여 작성하는 파일  
클래스는 DB에서 테이블과, 각 멤버 객체들은 column에 대응한다.  

**templates**

사용자에게 보여주는 부분.

**views.py**

request가 최종적으로 라우팅되어 동작시킬 로직이 정의된 파일

**admin.py**

adminpage에서 GUI를 통해 관리할 모델을 선언하는 페이지  
python manage.py createsuperuser 명령어를 통해 만든 관리자 ID, 비밀번호로 접근한다.  

  

**공통 모듈 구조**

---

```Plain
bookmark/
    __init__.py
    admin.py
    apps.py
    migrations/
    models.py
    tests.py
    views.py
    urls.py         # 앱의 URL 패턴 선언
    forms.py        # 입력 폼 선언
    behaviors.py    # 모델 믹스인 위치에 대한 옵션
    constants.py    # 앱에 쓰이는 상수 선언
    decorators.py   # 데코레이터
    db/             # 여러 프로젝트에서 용되는 커스텀 모델이나 컴포넌트
    fields.py       # 폼 필드
    factories.py    # 테스트 데이터 팩토리 파일
    helpers.py      # 뷰와 모델 파일을 가볍게 하기 위해 유틸리티 함수 선언
    managers.py     # models.py가 너무 커질 경우 커스텀 모델 매니저가 위치
    signals.py      # 커스텀 시그널
    viewmixins.py   # 뷰 모듈과 패키지를 더 가볍게하기 위해 뷰 믹스인을 이 모듈로 이전
```

### Django 프로젝트 설정

Django 기본 설정 옵션은 [`setting.py`](http://setting.py) 모듈 파일 하나로 설정. 그러나 실무적으로는 패키지로 만들어 설정을 나누어 관리.

  

**설정 기본**

---

`settings.py` 파일의 내용은 크게 다음 부분으로 나눌 수 있다.

- 데이터베이스 설정
    
    ```Python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ```
    
- 템플릿 설정
    
    ```Python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```
    
- 지역 시각 및 다국어 설정
    
    ```Python
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    
    # 프로젝트 기본 설정값은 위와 같으며 아래와 같이 수정한다.
    
    LANGUAGE_CODE = 'ko-kr'
    TIME_ZONE = 'Asia/Seoul'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    ```
    
- 애플리케이션의 등록
    
    ```Python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'bookmark.apps.BookmarkConfig',
    ]
    
    # 단순히 bookmark 모듈 이름으로 등록할 수도 있지만 
    # bookmark.apps.BookmarkConfig 설정 클래스 이름으로 등록하는 것이 보다 정확한 방법이다.
    ```
    
- 정적 파일 설정
    
    ```Python
    # 프로젝트 기본 설정값은 없으며 파일 업로드 기능 구현을 위해 다음 설정을 추가한다.
    
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
    # runserver 테스트 서버 구동 시에 /media 경로를 올바로 찾지 못하는 문제가 발생한다.
    # 따라서 URL 패턴 매칭을 해주는 다음 코드가 필요하다.
    
    from django.conf.urls.static import static
    
    urlpatterns = [
        ....
    ]
    
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
    
- 미디어 파일 설정
    
    ```Python
    STATIC_URL = '/static/'
    
    # 프로젝트 기본 설정값은 위와 같으며 STATIC_URL 변수를 추가한다.
    
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    ```
    

  

**설정 실무**

---

**settings 패키지로 구현**

```Plain
프로젝트_이름/
    repo/
        app1/
        app2/
        conf/
            __init__.py
            settings/
                base.py
                local.py
                production.py
                test.py
            urls.py
            wsgi.py
        manage.py            
        README.md
        requirements.txt
        .gitignore
    venv/
    # 배포 후 소켓 파일 및 연동 설정 파일이 위치하는 디렉토리
    run/
        uwsgi.ini
        uwsgi.sock
        gunicorn.sock
    # 로그 디렉토리
    logs/
    # SSL 키 파일 디렉토리
    ssl/
```

**설정 데이터의 분류**

1. 환경마다 다른 공개적인 설정
    - `local.py`, `test.py`, `production.py` 등으로 파일을 나누고 저장소에서 관리한다.
2. 모든 환경에서 동일한 공개적인 설정
    - `base.py` 파일을 만들고 이를 구체적인 `local.py`, `test,py`, `production.py` 등에서 임포트한다.
3. 환경마다 다른 비공개적인 설정
    - `local.py`, `test.py`, `production.py` 등으로 파일을 나누고 설정값은 환경변수로 로드한다.
4. 모든 환경에서 동일한 비공개적인 설정
    - `base.py` 파일을 만들고 설정값은 환경변수에서 로드하며 구체적인 `local.py`, `test.py`, `production.py` 등에서 임포트한다.

**여기서 중요한 것은 공개적인 설정은 저장소에서 코드로 저장되어 관리되지만 비공개 설정은 저장소에 절대 커밋되어서는 안 된다.**

  

### Database 연동

**PostgreSQL**

---

**패키지 설치**

```Bash
pip install psycopg2
```

**데이터베이스 및 사용자 추가**

```Bash
sudo su - postgres
psql
psql (9.5.4)
Type "help" for help.
```

```SQL
# 아래와 같이 django_test 데이터베이스와 시스템 계정이 아닌 
# 데이터베이스 사용자 django_user를 추가한다.

CREATE DATABASE django_test;
CREATE USER django_user WITH PASSWORD 'django_pass';
ALTER ROLE django_user SET client_encoding TO 'utf8';
ALTER ROLE django_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE django_test TO django_user;

\q
```
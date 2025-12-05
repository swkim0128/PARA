---
type: Django
archive: false
---
## 모델과 ORM

### 모델의 선언

```Python
# models.py

from django.db import models


class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 모음'
        ordering = ['title', ]

    def __str__(self):
        return self.title

# admin.py

from django.contrib import admin
from bookmark.models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Bookmark, BookmarkAdmin)
```

**Meta 내부 클래스 옵션**

---

**verbose_name**

사용자가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에서 표시된다. 영어를 기준으로 단수형이다.  
  
`verbose_name` 옵션을 지정하지 않으면 `CamelCase` 클래스 이름을 기준으로 `camel case` 이와 같이 모두 소문자로 변경한다.

**verbose_name_plural**

사용자가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에서 표시되는 것은 동일하나 영어를 기준으로 복수형이다.  
한국어에서는 굳이 단수와 복수를 구별해 사용하지 않으므로   
`verbose_name`과 동일하게 쓸 수 있다.  
  
`verbose_name_plural` 옵션을 지정하지 않으면 `verbose_name`에 `s`를 붙인다.

**ordering**

모델의 정렬 순서를 지정하며 여러 개를 지정할 경우 필드 이름을 리스트로 나열한다. 기본값은 오름차순으로 정렬하고 `-`를 붙이면 내림차순으로 정렬한다.  
다음 예시는   
`pub_date` 필드 기준 내림차순으로 정렬하고 다시 `author` 필드를 기준으로 오름차순 정렬한다.

```Python
ordering = ['-pub_date', 'author']
```

**db_table**

**abstract**

  

### 모델 매니저

**디폴트 모델 매니저**

---

모델 매니저는 데이터베이스 쿼리와 연동되는 인터페이스이다.  
각 모델은 애플리케이션에서 최소 하나의 매니저를 가진다. 디폴트 모델 매니저의 이름은   
`objects`이다.

  

**커스텀 모델 매니저**

---

커스텀 모델 매니저를 구현하는 방법은 크게 두 가지이다.

- 모델 매니저를 매번 추가해서 특정 모델 매니저 인스턴스를 이용하는 방식
- 디폴트 모델 매니저를 변경 후 메소드 체인으로 호출하는 방식

  

**모델 매니저를 추가하는 방식**

```Python
# blog/models.py 파일에 추가

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

# blog/models.py 파일 수정

class Post(models.Model):
    objects = models.Manager()
    published = PublishedManager()

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    publish = models.DateTimeField(default=timezone.now)

    ... 생략 ...

# 커스텀 모델 매니저의 메소드 호출 예시

>>> from blog.models import Post
>>> Post.objects.count()
2
>>> Post.published.count()
1
```

  

**모델 매니저를 메소드 체인으로 지정하는 방식**

```Python
# 커스템 모델 매니저를 정의
# blog/models.py 파일에 추가

class PublishedManager(models.Manager):
    use_for_related_fields = True
    # use_for_related_fields = True 옵션은 기본 매니저로 이 매니저를 정의한 모델이 있을 때
    # 이 모델을 가리키는 모든 관계 참조에서 모델 매니저를 사용할 수 있도록 한다.

    def published(self, **kwargs):
        return self.filter(status='published', **kwargs)

# 모델의 기본 매니저를 커스텀 메소드로 변경한다.
# blog/models.py 파일 수정

class Post(models.Model):
    objects = PublishedManager()

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    publish = models.DateTimeField(default=timezone.now)

    ... 생략 ...
```

  

### 모델 상속

### 모델의 관계 매핑
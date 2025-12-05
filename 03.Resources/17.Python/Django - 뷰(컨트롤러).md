---
type: Django
archive: false
---
## 뷰(컨트롤러)

### url 패턴

---

**url 정의**

```Python
urlpatterns = [
    path(정규식, 뷰, kwargs=None, name=None, prefix=''),
]
```

- 정규식: URL을 정규식으로 표현
- 뷰: URL 매칭이 되면 불러올 뷰 (CBV 또는 FBV)
- kwargs: 정규식 인자에서 추출한 파라미터 외에 추가적인 인자를 파이썬 사전 타입의 키워드 인자로 뷰 함수에 전달 가능
- name: URL 별로 별명을 두어 템플릿 파일에서 사용
- prefix: 뷰 함수에 대한 접두사 문자열

  

**클래스형 뷰와 함수형 뷰 호출**

- 클래스형 뷰 호출

```Python
urlpatterns = [
    path(r'^$', Home.as_view(), name='home'),
]
```

- 함수형 뷰 호출

```Python
urlpatterns = [
    path(r'^$', views.home, name='home'),
]
```

  

**파일 인클루드**

```Python
urlpatterns = [
    path(r'^polls/', include('polls.urls', namespace='polls')),
]
```

  

### 클래스형 뷰(CBV)

**CBV의 장점**

---

- GET, POST 등 HTTP 메소드에 따른 처리 코드를 작성할 때 if 함수 대신에 메소드 명으로 코드의 구조가 깔끔하다.
- 다중상속 같은 객체지향 기법을 활용해 제너릭 뷰, 믹스인 클래스 등을 사용해 코드의 재사용과 개발 생산성을 높여준다.

  

**제너릭 뷰와 상속**

---

제너릭 뷰의 4가지 분류

- 기반 뷰(Base View): 뷰 클래스를 생성하고 다른, 제너릭 뷰의 부모 클래스가 되는 기본 제너릭 뷰
- 제너릭 보기 뷰(Generic Display View): 객체의 목록 또는 하나의 객체 상세 정보를 보여주는 뷰
- 제너릭 수정 뷰(Generic Edit View): 폼을 통해 객체를 생성, 수정, 삭제하는 기능을 제공하는 뷰
- 제너릭 날짜 뷰(Generic Date View): 날짜 기반 객체의 연/월/일 페이지로 구분해 보여주는 뷰

  

**주요 제너릭 뷰 목록**

---

**기반 뷰(Base View)**

- View: 최상위 부모 제너릭 뷰 클래스
- TemplateView: 주어진 템플릿으로 렌더링
- RedirectView: 주어진 URL로 리다이렉트

**제너릭 보기 뷰(Generic Display View)**

- DetailView: 조건에 맞는 하나의 객체 출력
- ListView: 조건에 맞는 객체 목록 출력

**제너릭 수정 뷰(Generic Edit View)**

- FormView: 폼이 주어지면 해당 폼을 출력
- CreateView: 객체를 생성하는 폼 출력
- UpdateView: 기존 객체를 수정하는 폼을 출력
- DeleteView: 기존 객체를 삭제하는 폼을 출력

**제너릭 날짜 뷰(Generic Date View)**

- YearArchiveView: 주어진 연도에 해당하는 객체 출력
- MonthArchiveView: 주어진 월에 해당하는 객체 출력
- DayArchiveView: 주어진 날짜에 해당하는 객체 출력
- TodayArchiveView: 오늘 날짜에 해당하는 객체 출력
- DateDetailView: 주어진 연, 월, 일 PK(또는 슬러그)에 해당하는 객체 출력

  

**제너릭 뷰 오버라이딩**

---

**속성 변수 오버라이딩**

**`model`**

기본 뷰(View, Template, RedirectView) 3개를 제외하고 모든 제너릭 뷰에서 사용한다.

**`queryset`**

기본 뷰(View, Template, RedirectView) 3개를 제외하고 모든 제너릭 뷰에서 사용한다. `queryset`을 사용하면 `model` 속성은 무시된다.

**`template_name`**

TemplateView를 포함한 모든 제너릭 뷰에서 사용한다. 템플릿 파일명을 문자열로 지정한다.

**`context_object_name`**

뷰에서 템플릿 파일에 전달하는 컨텍스트 변수명을 지정한다.

**`paginate_by`**

ListView와 날짜 기반 뷰(예, YearArchiveView)에서 사용한다. 페이징 기능이 활성화 된 경우 페이지당 출력 항목 수를 정수로 지정한다.

**`date_field`**

날짜 기반 뷰(예, YearArchiveView)에서 사용한다. 이 필드의 타입은 DateField 또는 DateTimeField이다.

**`form_class`**

FormView, CreateView, UpdateView에서 폼을 만드는데 사용할 클래스를 지정한다.

**`success_url`**

FormView, CreateView, UpdateView, DeleteView에서 폼에 대한 처리가 성공한 후 리디이렉트할 URL 주소이다.

**메소드 오버라이딩**

**`def get_queryset()`**

기본 뷰(View, Template, RedirectView) 3개를 제외하고 모든 제너릭 뷰에서 사용한다. 디폴트는 `queryset` 속성을 반환한다. `queryset` 속성이 지정되지 않은 경우 모델 매니저 클래스의 all() 메소드를 호출해 QuerySet 객체를 생성해 반환한다.

**`def get_context_data(**kwargs)`**

뷰에서 템플릿 파일에 넘겨주는 컨텍스트 데이터를 추가하거나 변경하는 목적으로 오버라이딩한다.

**`def form_valid(form)`**

**모델을 지정하는 방법 3가지**

1. model 속성 변수 지정
2. queryset 속성 변수 지정
3. `def get_queryset()` 메소드 오버라이딩

  

**예제 코드**

---

```Python
from django.views.generic import ListView, DetailView
from .models import Question


class IndexView(ListView):
    template_name = 'cbvpolls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(DetailView):
    model = Question
    template_name = 'cbvpolls/detail.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'cbvpolls/results.html'
```

  

### 함수형 뷰(FBV)

**예제 코드**

---

```Python
from django.shortcutsimport render, get_object_or_404
from django.core.urlresolversimport reverse
from .modelsimport Question


defindex(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
return render(request, 'polls/index.html', context)


defdetail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
return render(request, 'polls/detail.html', {'question': question})


defresults(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
return render(request, 'polls/results.html', {'question': question})
```
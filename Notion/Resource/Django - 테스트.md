---
type: Django
archive: false
---
## 테스트

### 단위 테스트

---

테스트 구조

```Plain
catalog/
  /tests/
    __init__.py
    test_models.py
    test_forms.py
    test_views.py
```

  

test_models.py

```Python
from django.test import TestCase

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
```

- `setUpTestData()` 는 클래스 전체에서 사용되는 설정을 위해서 테스트 시작 때 딱 한 번만 실행됩니다. 테스트 메쏘드가 실행되면서 수정되거나 변경되지 않을 객체들을 이곳에서 생성할 수 있습니다.
- `setUp()` 은 각각의 테스트 메쏘드가 실행될 때마다 실행됩니다. 테스트 중 내용이 변경될 수 있는 객체를 이곳에서 생성할 수 있습니다 (모든 테스트 메쏘드는 방금 막 생성된 ("fresh") 오브젝트를 입력받게 됩니다).
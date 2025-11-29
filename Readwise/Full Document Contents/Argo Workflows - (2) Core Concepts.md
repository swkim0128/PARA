# Argo Workflows - (2) Core Concepts

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FetfqBH%2Fbtq8HdytOy6%2FAAAAAAAAAAAAAAAAAAAAAPpSE2sgOPdSLt9SHyCYMs-LzVrD0zBPppSyhIpwSHSk%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1764514799%26allow_ip%3D%26allow_referer%3D%26signature%3DezCji5Yy5SCWnD50ela9Yi3ZxgA%253D)

## Metadata
- Author: [[Operation CWAL]]
- Full Title: Argo Workflows - (2) Core Concepts
- Category: #articles
- Document Tags:  #argocd  #kubernetes 
- Summary: Argo Workflows uses a Workflow CRD defined in YAML to run tasks as reusable templates. Templates can be container, script, resource, or invoker types (steps or DAG) to run tasks serially or in parallel. You can add features like suspend/delay, and later use parameters, artifacts, loops, and conditions.
- URL: https://cwal.tistory.com/68

## Full Document
#### Core Concepts

이번 시간엔 Argo Workflows의 기본 개념과 Workflow에 대해서 알아보자. 가장 먼저 Argo Workflows 공식 홈페이지에서 제공하는 간단한 'Hello world' 예제부터 시작한다.

##### 'Hello world' Workflow

아래와 같이 'wf-hello-world.yaml'을 작성한다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: hello-world-  # Name of this Workflow
spec:
  entrypoint: whalesay        # Defines "whalesay" as the "main" template
  templates:
  - name: whalesay            # Defining the "whalesay" template
    container:
      image: docker/whalesay
      command: [cowsay]
      args: ["hello world"]   # This template runs "cowsay" in the "whalesay" image with arguments "hello world"
```

'Workflow'는 Argo Workflows에서 사용하는 CRD(Custom Resource Definition)이며, 당장은 위 YAML이 뭘 의미하는지 이해가 잘 안가도 'whalesay' 컨테이너를 통해 'hello world'를 출력하지 않을까라는 느낌이 든다. 아래 명령어로 Workflow를 생성해보자.

```
kubectl -n argo create -f wf-hello-world.yaml
```

![](https://blog.kakaocdn.net/dna/etfqBH/btq8HdytOy6/AAAAAAAAAAAAAAAAAAAAAPpSE2sgOPdSLt9SHyCYMs-LzVrD0zBPppSyhIpwSHSk/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=ezCji5Yy5SCWnD50ela9Yi3ZxgA%3D)
Argo Workflows 대시보드에서 'hello-world' workflow를 확인할 차례다.

![](https://blog.kakaocdn.net/dna/bKRojn/btq8PwiIvRX/AAAAAAAAAAAAAAAAAAAAAD9NwsGTkP-DFpLTsNw_ybmE_WBebunNIUyjIf02W7Sh/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=Zc9Y1oEzxIvSysTfMhhiOaYTlNk%3D)
SUMMARY 메뉴에서 MAIN LOGS 버튼을 선택하면 컨테이너 로그 조회가 가능하며, 'hello world' 메시지가 출력된 것을 확인할 수 있다.

![](https://blog.kakaocdn.net/dna/rgE6H/btq8Jttxxiv/AAAAAAAAAAAAAAAAAAAAAFrqcMsFvlxrx5dPiI9aCOFSmwOcKzgo2hGdcyJvrHQL/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=6%2FSphigQcNgGs9DTicreJneWYYc%3D)
'workflow' CRD의 Manifest는 YAML 또는 JSON 형식으로 작성하며, K8s의 기본 Workload(ex: Deployment, Pod)와 같이 크게 4개의 파트로 구성된다.

* apiVersion: 해당 Manifest의 API Version을 의미하며, 'argoproj.io/v1alpha1'를 사용한다.
* kind: K8s에 생성할 Resource 타입으로, 'Workflow'를 사용한다.
* metadata: Workflow의 이름(name) 또는 접두어(generateName), 그리고 namespace를 설정한다.
* spec
	+ entrypoint: 맨처음 시작할 template을 선택한다.
	+ templates: Workflow에 포함할 template들을 정의한다.

##### Template

Template은 Workflow 안에서 실제 작업을 수행하는 최소 단위로, 사용자에 의해 정의되고 재사용이 가능하다. 현재 Argo Workflows에선 총 4개의 Template 형식이 존재한다.

###### Container Template

Container Template은 Pod spec에서 container를 정의하는 것과 동일하다. container 생성시 사용할 image, 그리고 command 또는 args 필드를 설정한다. 다음은 container template을 사용한 workflow이며, 'hello-world' 예제와 구성이 크게 다르지 않다. 대부분의 경우, 많이 사용하는 방식이다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: wf-container-template-
spec:
  entrypoint: container-template
  templates:
  - name: container-template
    container:
      image: python:3.8-slim
      command: [echo, "The container template was executed successfully."]
```

```
kubectl -n argo create -f wf-container-template.yaml
```

![](https://blog.kakaocdn.net/dna/NyLSO/btq8OkixYyC/AAAAAAAAAAAAAAAAAAAAANaY6MqvidZiqPS5SS0Mdhp_v7oMTTMIs4FaOpjS4dyJ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=4KiK9noGKkTIm87YlPb369s0vrM%3D)
컨테이너에서 사용할 스크립트를 직접 Manifest 안에 정의한다는 점에서 Container Template과는 큰 차이가 있다. 다음은 간단한 script template 예제로, source 필드 안에 정의한 Python 스크립트를 컨테이너 안에서 실행한다. 따로 Image를 생성하지 않고도, 간단한 스크립트를 추가할 수 있다는 점에서 꽤 유용하다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: wf-script-template-
spec:
  entrypoint: script-template
  templates:
  - name: script-template
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        print("The script template was executed successfully.")
```

```
kubectl -n argo create -f wf-script-template.yaml
```

![](https://blog.kakaocdn.net/dna/b8CvL6/btq8Jkj1pV2/AAAAAAAAAAAAAAAAAAAAAHc7rlofgFjkmIQEGY-xBb0kMYmIr6b1EybjTpwh28Zp/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=oxncyYUu%2BeuuuDLS0zgdlpWkZy0%3D)
###### Resource Template

Workflow 실행시 다른 K8s 리소스를 생성할 수 있는 Template으로, Manifest 내용을 확인하면 상당히 재밌는 개념이다.

아래는 resource template 내부에서 'wf-test'라는 이름의 workflow 리소스를 생성하는 예제이다. workflow 안에 workflow를 정의한 것을 볼 수 있다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: wf-resource-template-
spec:
  entrypoint: resource-template
  templates:
  - name: resource-template
    resource:
      action: create
      manifest: |
        apiVersion: argoproj.io/v1alpha1
        kind: Workflow
        metadata:
          name: wf-test
        spec:
          entrypoint: test-template
          templates:
          - name: test-template
            script:
              image: python:3.8-slim
              command: [python]
              source: |
                print("Workflow wf-test created with resource template.")
```

```
kubectl -n argo create -f wf-resource-template.yaml
```

로그를 확인하면 해당 template으로부터 'wf-test' workflow가 생성되었다고 한다.

![](https://blog.kakaocdn.net/dna/4lJR4/btq8MHx43YT/AAAAAAAAAAAAAAAAAAAAAFy5j9-6ll-6JArbVYpLlIW4IiCn_mvUtvSKAktLAcfY/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=kCZplYm0c%2Fv5nGfandNE2WK0Fx8%3D)
실제로 'wf-test' workflow가 존재하며, 로그로부터 Manifest 작성시 정의한 메시지가 출력된 것을 알 수 있다.

![](https://blog.kakaocdn.net/dna/vfrFa/btq8Pu6kLZ7/AAAAAAAAAAAAAAAAAAAAAHo5Fc-gal-OOsGh42qLxKeGb5IqqvahrOMsyOJaisi5/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=qoq0A%2BG8ybLWHHZ7DJhVp%2FmyeDI%3D)
실행시 정해진 시간 동안 일시정지(suspend) 상태로 존재하는 template으로, 작업 간의 동기화 또는 대기 시간이 필요한 경우에 사용할 수 있다. 사용 방법은 Template Invocator를 먼저 소개한 후 알아보자.

##### Template Invocator

Template Invocator는 위에서 설명한 template(ex: container template, script template)을 호출할 수 있는 template으로, 여러 template들의 순차 또는 병렬 실행을 가능케 한다. 단일 template으로 구성된 workflow가 아니라면 반드시 필요한 template이다. 사용자가 직접 순서를 정의하는 Steps Template과 의존성을 통해 순서가 결정되는 DAG Template으로 구분된다.

steps 필드 내 정의 순서에 따라 어떤 step이 먼저 실행될지 결정되며, 아래 Manifest의 경우 step1 -> step2 -> step3 순으로 실행된다. 후순위의 step은 앞서 실행중인 step이 성공하기 전엔 실행되지 않는다. 실제 작업을 수행할 template인 'task-template은 script template으로 정의하였으며, 각 step에 의해 호출되는 것을 알 수 있다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: wf-steps-templates-serial
spec:
  entrypoint: steps-template-serial
  templates:
  - name: steps-template-serial
    steps:
    - - name: step1
        template: task-template
    - - name: step2
        template: task-template
    - - name: step3
        template: task-template
  - name: task-template
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        print("Task executed.")
```

```
kubectl -n argo create -f wf-step-template-serial.yaml
```

![](https://blog.kakaocdn.net/dna/cu4mUi/btq8KRuVddg/AAAAAAAAAAAAAAAAAAAAACgfAc1J5uelB9WQbWVsjqhDnuuQSYaFqohkgNb5gF9b/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=q%2F2eiStI0YkVS%2BeISbQo7ZQFZTI%3D)
###### Step Template - Parallel

steps 필드 안에서 동일 레벨에 '-'가 존재할 경우, 병렬 실행된다. 아래 workflow를 생성할 경우, step2와 step3가 동시에 실행되는 것을 확인할 수 있다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: wf-steps-templates-parallel
spec:
  entrypoint: steps-template-parallel
  templates:
  - name: steps-template-parallel
    steps:
    - - name: step1
        template: task-template
    - - name: step2
        template: task-template
      - name: step3
        template: task-template
    - - name: step4
        template: task-template
  - name: task-template
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        print("Task executed.")
```

```
kubectl -n argo create -f wf-step-template-parallel.yaml
```

![](https://blog.kakaocdn.net/dna/R1A7c/btq8MG61Wgi/AAAAAAAAAAAAAAAAAAAAAGiV5nxUF5d7-jfMhtWLuSAopiqknTIXUn7yCba3uvHf/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=4mj3%2Bn2BTplNrsHOUzKgwjBGDa0%3D)
steps template과는 달리, 명시적으로 순서를 정의하지 않는 대신 template 호출 단위인 'task' 간의 의존성(dependencies)을 기술함으로써, 자동으로 실행 순서가 결정된다. 의존성이 존재하지 않는 task의 경우, 대기없이 바로 실행된다. 다음은 DAG를 사용한 간단한 Workflow 예시이다. task1은 아무런 의존성이 없으므로 바로 실행되며, task2, task3는 모두 task1에 의존성이 있으므로 task1 완료 이후 실행되며, task4는 task2와 task3가 모두 끝난 뒤에 실행된다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: wf-dag-templates
spec:
  entrypoint: dag-template
  templates:
  - name: dag-template
    dag:
      tasks:
      - name: task1
        template: task-template
      - name: task2
        template: task-template
        dependencies: [task1]
      - name: task3
        template: task-template
        dependencies: [task1]
      - name: task4
        template: task-template
        dependencies: [task2, task3]

  - name: task-template
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        print("Task executed.")
```

```
kubectl -n argo create -f wf-dag-template.yaml
```

![](https://blog.kakaocdn.net/dna/bpxkFk/btq8KSm7rJ5/AAAAAAAAAAAAAAAAAAAAAAd37IR4MhxfyLrJDMzfg0HLqGd11bbqsAb67d1QtctF/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=W38EC8RxZyWvemG1ZZOr8t9urqc%3D)
위에서 언급했던 Suspend Template을 Parallel Steps template에 적용해보자. 다음은 template 호출시 10초간 일시정지가 발생하도록 구성한 Workflow이다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: wf-suspend-template
spec:
  entrypoint: steps-template-parallel
  templates:
  - name: steps-template-parallel
    steps:
    - - name: step1
        template: task-template
    - - name: step2
        template: task-template
      - name: step3
        template: task-template
    - - name: delay
        template: delay-template
    - - name: step4
        template: task-template
  - name: task-template
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        print("Task executed.")
  - name: delay-template
    suspend:
      duration: "10s"
```

```
kubectl -n argo create -f wf-suspend-template.yaml
```

![](https://blog.kakaocdn.net/dna/c2MWlk/btq8KXOJjV6/AAAAAAAAAAAAAAAAAAAAADChhp0punJEaED5gHl-tRzaQFpTzKOwCsJafSaE6Vi_/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=3zZbKisd25IKG8H58RXJs8wIVA4%3D)
'delay' step의 SUMMARY 메뉴를 확인하면 duration이 10s인 것을 알 수 있다.

![](https://blog.kakaocdn.net/dna/brvrzg/btq8KXVt1MN/AAAAAAAAAAAAAAAAAAAAAGGdPVVZLGiphvAxZjzUgr2qoWxc1nV1ZSTFtNYXs_Et/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=xjS88sSmnflkbZ7%2B3eb7d4sbSSE%3D)
#### What comes next?

다음 시간엔 보다 정교한 Workflow 및 Template 정의에 필요한 기능인 Input/Output Parameter, Artifact, Loop, Condition 등에 대해서 공부해보자.

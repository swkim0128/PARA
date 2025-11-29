# Argo Workflows - (3) Parameter, Artifact

![rw-book-cover](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fbb44Vf%2Fbtq80zs3113%2FAAAAAAAAAAAAAAAAAAAAAO9iZCWi_IJwjNVzMGtkY50aXFrDpGR84Vo-P2PbceEL%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1764514799%26allow_ip%3D%26allow_referer%3D%26signature%3Dr6DvX22sqmTyIvjoggBf06GP1bs%253D)

## Metadata
- Author: [[Operation CWAL]]
- Full Title: Argo Workflows - (3) Parameter, Artifact
- Category: #articles
- Document Tags:  #argocd  #kubernetes 
- Summary: Argo Workflows lets you define Parameters to pass values into templates when you run workflows. Output Parameters capture a template's stdout or files so other templates can use those results. You can pass parameters from the CLI, a file, or link task outputs/artifacts to later tasks.
- URL: https://cwal.tistory.com/69

## Full Document
#### Parameters

Workflow를 정의할 때, template에서 사용할 변수를 정의하고 해당 template 호출시 값을 전달해 줄 수 있는 이를 Parameter라고 한다. Argo Workflows에는 Input과 Output 두가지 타입의 Parameter가 존재한다.

##### Input

Input Parameter의 값을 달리 하여, Template 실행시 다른 동작을 하도록 구성할 수 있다. 이전에 작성했던 wf-dag-template.yaml을 수정하여, 다음과 같은 Workflow manifest를 작성해보자.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: wf-input-parameter-templates
spec:
  entrypoint: dag-template
  arguments:
    parameters:
    - name: message1
      value: Task 1 is executed
    - name: message2
      value: Task2 is executed
    - name: message3
      value: Task3 is executed
    - name: message4
      value: That's it with task 4
  templates:
  - name: dag-template
    inputs:
      parameters:
      - name: message1
      - name: message2
      - name: message3
      - name: message4
    dag:
      tasks:
      - name: task1
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message1}}"}]
        template: task-template
      - name: task2
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message2}}"}]
        template: task-template
        dependencies: [task1]
      - name: task3
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message3}}"}]
        template: task-template
        dependencies: [task1]
      - name: task4
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message4}}"}]
        template: task-template
        dependencies: [task2, task3]

  - name: task-template
    inputs:
      parameters:
      - name: text
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        param = "{{inputs.parameters.text}}"
        print(param)
```

* spec.arguments.parameters: Workflow에서 사용할 Parameter의 이름과 값을 설정하는 곳으로, message1부터 message4까지 각각의 문자열 값을 준비한 것을 볼 수 있다.
* spec.templates[\*].inputs.parameters: 해당 template에서 input으로 사용할 parameter를 정의한다. template 안에서 특정 input parameter를 호출하기 위해선 '{{inputs.parameters.<parameter명>}}' 형식(Jinja2 templating)을 사용한다.
* dag-template은 task-template 호출시, 해당 template의 input parameter 'text'에 message1부터 message4까지 각각 할당하는 것을 볼 수 있다.
* task-template은 python으로 작성된 Script template으로, 변수 param은 해당 template의 input parameter 'text'의 값이 할당되며, 이를 stdout으로 출력한다.

위 Workflow를 실행하면 다음과 같은 결과를 확인할 수 있다. 이번 시간부터는 kubectl 대신 argo cli 명령어를 사용한다.

```
argo -n argo submit wf-input-parameter-dag.yaml
```

![](https://blog.kakaocdn.net/dna/bb44Vf/btq80zs3113/AAAAAAAAAAAAAAAAAAAAAO9iZCWi_IJwjNVzMGtkY50aXFrDpGR84Vo-P2PbceEL/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=r6DvX22sqmTyIvjoggBf06GP1bs%3D)
![](https://blog.kakaocdn.net/dna/bwW3Im/btq8W7YMWwA/AAAAAAAAAAAAAAAAAAAAAAIaVMQvHPG6wjNqzdt5XIJSUqDc8TNMFaR3eH_DC_Yb/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=06KwHGdAmSHienz8weKdggMADpA%3D)
![](https://blog.kakaocdn.net/dna/2WbRw/btq8ZH584C3/AAAAAAAAAAAAAAAAAAAAAOrMitSMHNPww4_Eswb7PiE5VQBAue16iLZF6EzQxo_l/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=a94xhoqtuc1qq65Bf0p5vE45q2U%3D)
다음 명령어로 기존 Workflow를 삭제할 수 있다.

```
argo -n argo delete wf-input-parameter-templates
```

![](https://blog.kakaocdn.net/dna/duXJk5/btq8VFaoQ5h/AAAAAAAAAAAAAAAAAAAAAPVFSNpWXRSQtD-VbvYNKmPdxQ52lWSR0EgbtC_es0vY/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=cXBNdc%2FKq9tRZ1zGiqLD5fuy5A0%3D)
Parameter 값을 CLI를 통해 외부에서 제공하는 방법도 존재한다. 다음은 message1의 값을 CLI에서 지정하는 명령어 예시이다.

```
argo -n argo submit wf-input-parameter-dag.yaml -p message1="Parameter used from terminal"
```

![](https://blog.kakaocdn.net/dna/dS37y5/btq8YW3NYmw/AAAAAAAAAAAAAAAAAAAAAMhYzOLEgg2PtcgliHdwIeJ-lcDuVTxkANfgu7S3mwbQ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=h3EmAhc9W0wK6PId2AC04W1bu3g%3D)
![](https://blog.kakaocdn.net/dna/dMRS1S/btq8ZqQ6PSE/AAAAAAAAAAAAAAAAAAAAAIFkaKWhW-HAFKFVsZaPrC4vWnH0KNJoWfsXvQ0QvjLZ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=D3NBDQD1tvJ%2FFiOFLcuoUDyW5t4%3D)
그리고 Parameter 값을 별도의 파일에 작성하고, 이를 workflow 실행시 불러올 수도 있다. 먼저 아래와 같은 'params.yaml'이라는 파일을 준비한다. 기존 Workflow는 삭제하자.

```
message1: Parameter 1 from param file
message3: Parameter 3 from param file
```

다음 명령어로 params.yaml 파일로부터 Parameter 값을 읽은 후, Workflow를 생성할 수 있다.

```
argo -n argo submit wf-input-parameter-dag.yaml --parameter-file params.yaml
```

![](https://blog.kakaocdn.net/dna/Focsb/btq8TPxzlUt/AAAAAAAAAAAAAAAAAAAAAJwLXOklJ6v_OCEz9-F6VBTe3qMlQzJdOHCIpJczdzDo/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=ecR%2BWTV3APjDQOgzyt7wbPrVtU8%3D)
##### Ouput

Argo Workflows는 Template 실행 결과(output)에 별도의 이름을 붙임으로써, 이를 Parameter로 관리할 수 있는 기능을 제공한다. 어떤 template의 stdout으로 출력된 메시지나 파일을 다른 template의 input parameter로 전달하는 등의 동작이 가능하다.

task의 표준출력(stdout) 메시지를 그대로 가져와서 input parameter로 사용할 수 있다. 우선 wf-input-parameter-dag.yaml 파일을 수정하여 다음과 같은 Workflow를 작성한다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: wf-script-result
spec:
  entrypoint: dag-template
  arguments:
    parameters:
    - name: message1
      value: Task 1 is executed
    - name: message2
      value: Task2 is executed
  templates:
  - name: dag-template
    inputs:
      parameters:
      - name: message1
      - name: message2
    dag:
      tasks:
      - name: task1
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message1}}"}]
        template: task-template
      - name: task2
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message2}}"}]
        template: task-template
        dependencies: [task1]
      - name: task3
        template: task-output
        dependencies: [task1]
      - name: task4
        arguments:
          parameters: [{name: text, value: "{{tasks.task3.outputs.result}}"}]
        template: task-template
        dependencies: [task2, task3]

  - name: task-template
    inputs:
      parameters:
      - name: text
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        param = "{{inputs.parameters.text}}"
        print(param)
  
  - name: task-output
    script:
      image: node:9.1-alpine
      command: [node]
      source: |
        var out = "Print result";
        console.log(out);
```

'task-output' 템플릿은 node.js로 작성된 스크립트로 stdout에 "Print Result"라는 메시지를 출력한다. dag-template의 task3은 task-output을 단순히 호출하는 task이며, task4는 task3의 출력을 "{{tasks.task3.outputs.result}}"라는 이름으로 가져와서 task-template에 input parameter로 전달한다. {{tasks.<task명>.outputs.result}} 는 Argo Workflows에서 미리 reserve되어있는 변수명으로 해당 task의 표준출력 메시지를 output parameter로 지정한다. task4는 input parameter 'text'를 그대로 출력한다.

다음은 workflow를 실행 후 task3과 task4의 로그를 확인한 결과이다. task3의 출력이 task4의 입력으로 전달된 것을 볼 수 있다.

![](https://blog.kakaocdn.net/dna/bMtRxW/btq839hqvHp/AAAAAAAAAAAAAAAAAAAAAA15UCRBtNG_TJF26Aj07w1h0EtHidMQGK2AnvcDUtC9/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=1K9m93nJuRO4mdHn84A7%2F1%2FMF%2FY%3D)task3 출력 
![](https://blog.kakaocdn.net/dna/buuhwD/btq810eqccT/AAAAAAAAAAAAAAAAAAAAAADuddFHVFtdhKUbbJUvyXd3M-pbAuKJ-Rxr3OwdAw2g/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=%2B0mGVN%2FN2NDZS9ECRuy9%2BeCOYmA%3D)task4 출력 
사용자가 직접 Output Parameter를 추가할 수도 있다. 우선 wf-script-result workflow를 수정하여 다음과 같은 Manifest를 작성한다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: wf-output-parameter
spec:
  entrypoint: dag-template
  arguments:
    parameters:
    - name: message1
      value: Task 1 is executed
    - name: message2
      value: Task2 is executed
  templates:
  - name: dag-template
    inputs:
      parameters:
      - name: message1
      - name: message2
    dag:
      tasks:
      - name: task1
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message1}}"}]
        template: task-template
      - name: task2
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message2}}"}]
        template: task-template
        dependencies: [task1]
      - name: task3
        template: task-output
        dependencies: [task1]
      - name: task4
        arguments:
          parameters: [{name: text, value: "{{tasks.task3.outputs.parameters.task-param}}"}]
        template: task-template
        dependencies: [task2, task3]

  - name: task-template
    inputs:
      parameters:
      - name: text
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        param = "{{inputs.parameters.text}}"
        print(param)
  
  - name: task-output
    script:
      image: node:9.1-alpine
      command: [node]
      source: |
        var out = "Print result";
        console.log(out);
    outputs:
      parameters:
      - name: task-param
        value: "task-output-parameter"
```

task-output 템플릿에 outputs 필드를 추가하여 'task-param'이라는 이름을 가진 output parameter에 "task-output-parameter"라는 문자열 값을 할당한 것을 볼 수 있다. 기존과 동일하게 task3은 task-output 템플릿을 호출하지만, task4는 task3의 output parameter 중 task-param을 task-template의 input parameter로 전달한다. 결과적으로 task4의 로그는 "task-output-parameter"가 될 것이다.

![](https://blog.kakaocdn.net/dna/bF49jJ/btq85eP4jQX/AAAAAAAAAAAAAAAAAAAAALY0ZgbDFWrD681PhSdqsfpI1wFUl2mj1r3sjeWfw3p7/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=5CMqv7Wg8BOs%2F5Qn6ytv%2Fe%2BC0KA%3D)
###### File Output Parameter

특정 파일을 템플릿의 Output Parameter로 지정하는 기능도 존재한다. wf-output-parameter를 수정하여 아래와 같은 wf-output-parameter-file이라는 workflow를 정의하였다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: wf-output-parameter-file
spec:
  entrypoint: dag-template
  arguments:
    parameters:
    - name: message1
      value: Task 1 is executed
    - name: message2
      value: Task2 is executed
  templates:
  - name: dag-template
    inputs:
      parameters:
      - name: message1
      - name: message2
    dag:
      tasks:
      - name: task1
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message1}}"}]
        template: task-template
      - name: task2
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message2}}"}]
        template: task-template
        dependencies: [task1]
      - name: task3
        template: task-output
        dependencies: [task1]
      - name: task4
        arguments:
          parameters: [{name: text, value: "{{tasks.task3.outputs.parameters.task-param}}"}]
        template: task-template
        dependencies: [task2, task3]

  - name: task-template
    inputs:
      parameters:
      - name: text
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        param = "{{inputs.parameters.text}}"
        print(param)
  
  - name: task-output
    script:
      image: node:9.1-alpine
      command: [node]
      source: |
        var param = "Whatever parameters are written to the file.";
        const fs = require('fs');
        fs.writeFile("/tmp/output-params.txt", param)
    outputs:
      parameters:
      - name: task-param
        valueFrom:
          path: /tmp/output-params.txt
```

task-output 템플릿 실행시 "/tmp/output-params.txt"라는 파일에 메시지를 출력한다. 그리고 output parameter 'task-param'에 해당 파일로부터 값을 읽어오도록 설정하였다. 위 Workflow를 실행하면 task4의 로그는 다음과 같다.

![](https://blog.kakaocdn.net/dna/m1z1b/btq81d58GFb/AAAAAAAAAAAAAAAAAAAAAG9vC7SdmMMhrCBdP0cclrHQuB3mnT2Zipwy6YjyRySc/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=xOHQr%2FcGQA7KBEPtSM9dpzL3M28%3D)
#### Artifacts

Artifact는 File output parameter와 비슷하지만, 파일로부터 값을 읽어오는 것이 아닌 파일 그 자체를 input/output parameter로 사용 가능하다는 점에서 큰 차이를 보인다. 다음은 Artifact 기능을 통해 task 간에 파일을 전달하는 Workflow 예시이다.

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: wf-artifact
spec:
  entrypoint: dag-template
  arguments:
    parameters:
    - name: message1
      value: Task 1 is executed
    - name: message2
      value: Task2 is executed
  templates:
  - name: dag-template
    inputs:
      parameters:
      - name: message1
      - name: message2
    dag:
      tasks:
      - name: task1
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message1}}"}]
        template: task-template
      - name: task2
        arguments:
          parameters: [{name: text, value: "{{inputs.parameters.message2}}"}]
        template: task-template
        dependencies: [task1]
      - name: task3
        template: task-output-artifact
        dependencies: [task1]
      - name: task4
        arguments:
          artifacts: [{name: text, from: "{{tasks.task3.outputs.artifacts.artifact-out}}"}]
        template: task-input-artifact
        dependencies: [task2, task3]

  - name: task-template
    inputs:
      parameters:
      - name: text
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        param = "{{inputs.parameters.text}}"
        print(param)
  
  - name: task-output-artifact
    script:
      image: node:9.1-alpine
      command: [node]
      source: |
        var param = "Whatever parameters are written to the file.";
        const fs = require('fs');
        fs.writeFile("/tmp/output-params.txt", param)
    outputs:
      artifacts:
      - name: artifact-out
        path: /tmp/output-params.txt
  
  - name: task-input-artifact
    inputs:
      artifacts:
      - name: text
        path: /tmp/text
    script:
      image: python:3.8-slim
      command: [python]
      source: |
        with open("/tmp/text", "r") as f:
          lines = f.read()
          print(lines)
```

task-output-artifact 템플릿은 "/tmp/output-params.txt" 파일을 "artifact-out"이라는 이름의 Ouput Artifact로 정의하였으며, task-input-artifact 템플릿은 "/tmp/txt" 파일을 "text"라는 이름의 Input Artifact로 정의하였다. 그리고 dag-template의 task4는 task3의 output artifact를 task-input-artifact 템플릿 호출시 input artifact로 전달하는 것을 볼 수 있다. 결과적으로 task4 실행시, "Whatever parameters are written to the file." 로그가 출력된다.

![](https://blog.kakaocdn.net/dna/3YPqy/btq80z2CMjU/AAAAAAAAAAAAAAAAAAAAAOfNTZcX6ywn4Iq7uCijEcnXlXGuQMgREHtHlh-n4OHR/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=Lqim59emZHh4gNIstS1j6FE97Vw%3D)

---
tags:
  - kotlin
---

코틀린(Kotlin)으로 개발하기 위해 필요한 도구와 환경을 설정하는 방법을 설명합니다.

---

### 1. JDK 설치

코틀린은 JVM(Java Virtual Machine) 위에서 실행되므로 JDK(Java Development Kit)가 필요합니다.

**JDK 설치 방법**

1. [OpenJDK](https://openjdk.org/) 또는 [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html) 중 하나를 다운로드하여 설치합니다.
2. 설치 후 JDK 버전을 확인합니다:

```bash
   java -version
```

출력 결과에 JDK 버전이 표시되면 성공적으로 설치된 것입니다.

### 2. 코틀린 컴파일러 설치

코틀린 공식 컴파일러를 설치하여 CLI(Command Line Interface)에서 코드를 실행할 수 있습니다.

**설치 방법**

1. 코틀린 공식 웹사이트에서 최신 버전의 컴파일러를 다운로드합니다: [Kotlin Releases](https://github.com/JetBrains/kotlin/releases)
2. 다운로드한 파일을 압축 해제 후, 실행 가능한 kotlinc 파일이 있는 디렉토리를 환경 변수(PATH)에 추가합니다.
3. 설치 확인:

``` bash
kotlinc -version
```

### 3. IDE 설치

JetBrains에서 제공하는 **IntelliJ IDEA**는 코틀린 개발에 가장 적합한 IDE입니다.

**IntelliJ IDEA 설치**

1. [IntelliJ IDEA 공식 웹사이트](https://www.jetbrains.com/idea/)에서 Community 또는 Ultimate 버전을 다운로드하여 설치합니다.
2. 설치 후 코틀린 플러그인은 기본적으로 포함되어 있으며, 별도 설치가 필요하지 않습니다.

### 4. IntelliJ IDEA에서 코틀린 프로젝트 생성

1. IntelliJ IDEA를 실행합니다.
2. **New Project**를 선택합니다.
3. **Kotlin** > **JVM**을 선택한 후 프로젝트 설정을 완료합니다.
4. 생성된 프로젝트에 기본 코틀린 파일을 추가하여 코드를 작성할 수 있습니다:

- 파일 확장자는 .kt입니다.
- 예제:

``` kotlin
fun main() {
    println("Hello, Kotlin!")
}
```

### 5. Gradle 또는 Maven 설정

Gradle이나 Maven을 사용하면 코틀린 프로젝트의 빌드 및 의존성 관리를 쉽게 할 수 있습니다.

**Gradle 설정**

1. build.gradle 파일에 코틀린 플러그인을 추가합니다:

``` gradle
plugins {
    id 'org.jetbrains.kotlin.jvm' version '1.9.0'
}

repositories {
    mavenCentral()
}

dependencies {
    implementation "org.jetbrains.kotlin:kotlin-stdlib"
}
```

2. 프로젝트 디렉토리에서 Gradle 빌드 실행:

``` bash
./gradlew build
```

**Maven 설정**

1. pom.xml 파일에 코틀린 의존성을 추가합니다:

``` xml
<dependency>
    <groupId>org.jetbrains.kotlin</groupId>
    <artifactId>kotlin-stdlib</artifactId>
    <version>1.9.0</version>
</dependency>
```

2. Maven 빌드 실행:

``` bash
mvn clean install
```

### 6. VS Code를 이용한 코틀린 개발 (옵션)

VS Code에서도 코틀린 개발이 가능합니다.

**설정 방법**

1. [Visual Studio Code](https://code.visualstudio.com/)를 설치합니다.
2. VS Code의 **Extensions**에서 “Kotlin Language” 플러그인을 설치합니다.
3. 필요한 경우, **Code Runner** 플러그인을 추가로 설치하여 실행 환경을 설정합니다.

### 7. 첫 코틀린 프로그램 실행

**CLI에서 실행**

1. example.kt 파일을 생성하고 아래 코드를 작성합니다:

``` kotlin
fun main() {
    println("Hello, Kotlin!")
}
```

2. CLI에서 컴파일 및 실행:

``` bash
kotlinc example.kt -include-runtime -d example.jar
java -jar example.jar
```

**IntelliJ IDEA에서 실행**

1. 코드를 작성한 후, **Run** 버튼을 클릭하여 프로그램을 실행합니다.

이 가이드를 따라 코틀린 개발 환경을 설정하면, 다양한 플랫폼에서 코틀린을 사용하여 효율적으로 개발할 수 있습니다.

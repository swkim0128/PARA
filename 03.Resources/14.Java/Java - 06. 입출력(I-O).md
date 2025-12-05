---
type: Java
archive: false
---
## 자바에서의 입출력

### 입출력이란?

---

간단히 입출력, 컴퓨터 내부 또는 외부의 장치와 프로그램간의 데이터를 주고받는 것을 말함.

  

### 스트림(stream)

---

자바에서 어느 한쪽에서 다른 쪽으로 데이터를 전달하려면, 두 대상을 연결하고 데이터를 전송할 수 있는 무언가가 필요한데 이것을 스트림(stream)이라고 정의했다.

> 스트림이란 데이터를 운반하는데 사용되는 연결통로이다.

스트림은 단방향 통신만 가능하기 때문에 하나의 스트림으로 입력과 출력을 동시에 처리할 수 없다.  
그래서 입력과 출력을 동시에 수행하려면 입력을 위한 입력스트림(input stream)과 출력을 위한 출력스트림(output stream), 모두 2개의 스트림이 필요하다.  

  

### 바이트기반 스트림 - InputStream, OutputStream

---

스트림은 바이트단위로 데이터를 전송하며입출력 대상에 따라 다음과 같은 입출력스트림이 있다.

FileInputStream

ByteArrayInputStream

PipedInputStream

AudioInputStream

FileOutputStream

ByteArrayOutputStream

PipedOutputStream

AudioOutputStream

파일

메모리(byte배열)

프로세스(프로세스간의 토신)

오디오장치

이들은 모두 inputStream 또는 OutputStream의 자손들이며, 각각 일고 쓰는데 필요한 추상메서드를 자신에 맞게 구현해 놓았다.

  

InputStream

abstract int read()

int read(byte[] b)

int read(byte[] b, int off, int len)

OutputStream

abstract void write(int b)

void write(byte[] b)

void write(byte[] b, int off, int len)

  

### 보조스트림

---

언급한 스트림 외에도 스트림의 기능을 보완하기 위한 보조스트림이 제공된다. 보조스트림은 실제 데이터를 주고받는 스트림이 아니기 때문에 데이터를 입출력할 수 있는 기능은 없지만, 스트림의 기능을 향상시키거나 새로운 기능을 추가할 수 있다. 보조스트림만으로는 입출력을 처리할 수 없고, 스트림을 먼저 생성한 다음에 이를 이용해서 보조스트림을 생성해야한다.

입력

FilterInputStream

BufferedInputStream

  
DataInputStream  
  

SequenceInputStream

LineNumberInputStream

  
ObjectInputStream  
  

  
없음  
  

PushbackInputStream

출력

FilterOutputStream

BufferedOutputStream

  
DataOutputStream  
  

SequenceOutputStream

없음

  
ObjectOutputStream  
  

  
PinrtStream  
  

없음

설명

필터를 이용한 입출력 처리

버퍼를 이용한 입출력 성능향상

int, float와 같은 기본형 단위(primitive type)로 데이터를 처리하기는 기능

두 개의 스트림을 하나로 연결

읽어온 데이터의 라인 번호를 카운드

데이털를 객체단위로 읽고 쓴느데 사용. 주로 파일을 이용하며 객체 직렬화와 관련 있음.

버퍼를 이용하며, 추가적인 print관련 기능(print, printf, println메서드)

버퍼를 이용해서 읽어 온 데이터를 다시 되돌리는 기능(unread, push back to buffer)

  

### 문자기반 스트림 - Reader, Writer

---

지금까지 알아본 스트림은 모두 바이트기반의 스트림이었다. 바이트기반이라 함은 입출력의 단위가 1 byte라는 뜻이다. 이미 알고 있는 것과 같이 C언어와 달리 Java에서는 한 문자를 의미하는 char형이 1 byte가 아니라 2byte이기 때문에 바이트기반의 스트림으로 2 byte인 문자를 처리하는 데 어려움이 있다.  
이 점을 보완하기 위해서 문자기반의 스트림이 제공된다. 문자데이터를 입출력할 때는 바이트기반 스트림 대신 문자기반 스트림을 사용  

> InputStream → Reader  
> OutputStream → Writer  

**바이트기반 스트림**

FileInputStream  
FileOutputStream  

ByteArrayInputStream  
ByteArrayOutputStream  

PipedInputStream  
PipedOutputStream  

StringBufferInputStream(deprecated)  
StringBufferOutputStream(deprecated)  

**문자기반 스트림**

FileReader  
FileWriter  

CharArrayReader  
CharArrayWriter  

PipedReader  
PIpedWriter  

StringReader  
StringWriter  

  

**InputStream**

abstract int read()  
int read(byte[] b)  
int read(byte[], int off, int len)  

**OutputStream**

  
abstract void write(int b)  
void write(byte[] b)  
void write(byte[] b, int off, int lne)  

**Reader**

int read()  
int read(char[] cbuf)  
abstract int read(char[] cbuf, int off, int len)  

**Writer**

void write(int c)  
void write(char[] cbuf)  
abstract void write(char[] cbuf, int off, int len)  
void write(String str)  
void write(String str, int off, int len)  

  

보조스트림 역시 다음과 같은 문자기반 보조스트림이 존재하며 사용목적과 방식은 바이트기반 보조스트림과 다르지 않다.

**바이트기반 보조스트림**

BufferedInputStream  
BufferedOutputStream  

FilterInputStream  
FilterOutputStream  

LineNumberInputStream(deprecated)

PrintStream

PushbackInputStream

**문자기반 보조스트림**

BufferedReader  
BufferedWriter  

FilterReader  
FilterWriter  

LineNumberReader

PrintWriter

PushbackReader

  

## 바이트기반 스트림

### InputStream과 OutputStream

---

**메서드명**

int available()

void close()

void mark(int readlimit)  
  

  
boolean markSupported()  
  

  
abstract int read()  
  

int read(byte[] b)  
  

int read(byte[] b, int off, int len)

void reset()

long skip(long n)

**설 명**

스트림으로부터 읽어 올 수 있는 데이터의 크기를 반환한다.

스트림을 닫음으로써 사용하고 있던 자원을 반환한다.

현재위치를 표시해 놓는다. 후에 reset()에 의해서 표시해 놓은 위치로 다시 돌아갈 수 있다. readlimit은 되돌아갈 수 있는 byte의 수이다.

mark()와 reset()을 지원하는지 알려 준다. mark()와 reset()기능을 지원하는 것은 선택적이므로, mark()와 reset()을 사용하기 전에 markSupported()를 호출해서 지원여부를 확인해야 한다.

1 byte을 읽어 온다.(0~255사이의 값). 더 이상 읽어 올 데이터가 없으면 -1을 반환한다. abstract메서드라서 InputStream의 자손들은 자신의 상황에 알맞게 구현해야 한다.

배열 b의 크기만큼 읽어서 배열을 채우고 읽어 온 데이터의 수를 반환한다. 반환하는 값은 항상 배열의 크기보다 작거나 같다.

최대 len개의 byte를 읽어서, 배열 b의 지정된 위치(off)부터 저장한다. 실제로 읽어 올 수 있는 데이터가 len개보다 적을 수 있다.

스트림에서의 위치를 마지막으로 mark()이 호출되었던 위치로 되돌린다.

스트림에서 주어진 길이(n)만큼을 건너뛴다.

  

### ByteArrayInputStream과 ByteArrayOutputStream

---

메모리, 즉 바이트배열에 데이터를 입출력 하는데 사용되는 스트림이다. 주로 다른 곳에 입출력하기 전에 데이터를 임시로 바이트배열에 담아서 변환 등의 작업을 하는데 사용된다.  
자주 사용되지 않지만 스트림을 이용한 입출력방법으 ㄹ보여 준느 예제를 작성하기에는 적합.  

  

### FileInputStream과 FileOutputStream

---

파일에 입출력을 하기 위한 스트림이다. 실제 프로그래밍에서 많이 사용되는 스트림 중의 하나이다.

  

생성자

FileInputStream(String name)  
  

FileInputStream(File file)  
  

FileOutputStream(String name)  
  

  
FileOutputStream(String name, boolean append)  
  

FileOutputStream(File file)

설 명

지정된 파일이름(name)을 가진 실제 파일과 연결된 FileInputStream을 생성한다.

파일의 이름이 String이 아닌 File인스턴스로 지정해주어야 하는 점을 제외하고 FileInputStream(String name)와 같다.

지정된 파일이름(name)을 가진 실제 파일과의 연결된 FileOutputStream을 생성한다.

지정된 파일이름(name)을 가진 실제 파일과 연결된 FileOutputStream을 생성한다. 두번째 인자인 append를 true로 하면, 출력 시 기존의 파일내용의 마지막에 덧붙인다. false면, 기존의 파일내용을 덮어쓰게 된다.

파일의 이름을 String이 아닌 File인스턴스로 지정해주어야 하는 점을 제외하고 FileOutputStream(String name)과 같다.

  

## 바이트기반의 보조스트림

### FilterInputStream과 FilterOutputStream

---

InputStream/OutputStream의 자손이면서 모든 보조스트림의 조상이다. 보조 스트림은 자체적으로 입출력을 수행할 수 없기 때문에 기반스트림을 필요로 한다.

  

### BufferedInputStream과 BufferedOutputStream

---

스트림의 입출력 효율을 높이기 위해 버퍼를 사용하는 보조스트림이다. 한 바이트씩 입출력하는 것 보다는 버퍼(바이트배열)를 이용해서 한 번에 여러 바이트를 입출력하는 것이 빠르기 때문에 대부분의 입출력 작업에 사용된다.

  

**메서드 / 생성자**

BufferedInputStream(InputStream in, int size)  
  

  
BufferedInputSream(InputStream in)  

**설명**

주어진 InputStream인스턴스를 입력소스(input source)로 하며 지정된 크기(byte단위)의 버퍼를 갖는 bufferedInputStream인스턴스를 생성한다.

주어진 InputStream인스턴스를 입력소스(input source)로 하며 버퍼의 크기를 지정해주지 않으므로 기본적으로 8192byte크기의 버퍼를 갖게 된다.

  

BufferedInputStream의 버퍼크기는 입력소스로부터 한 번에 가져올 수 있는 데이터의 크기로 지정하면 좋다. 보통 입력소스가 파일인 경우 보통 작게는 1024부터 2048 또는 4096 정도의 크기로 하는 것이 보통이며, 버퍼의 크기를 변경해가면서 테스트하면 최적의 버퍼크기를 알아낼 수 있다.  
프로그램에서 입력소스로부터 데이터를 읽기 위해 처음으로 Read메서드를 호출하면, BufferedInputStrea은 입력소스로 부터 버퍼 크기만큼의 데이터를 읽어다 자신의 내무 버퍼에 저장한다. 이제 프로그램에서는 BufferedInputStream의 버퍼에 저장된 데이터를 읽으면 되는 것이다. 외부의 입력소스로부터 읽는 것보다 내부의 버퍼로부터 읽는 것이 훨씬 빠르기 때문에 그만큼 작업 효율이 높아진다.  

  

메서드/ 생성자

BufferedOutputStream(OutputStream out, int size)  
  

BufferedOutputStream(OutputStream out)  
  

flush()  
  

close()

설명

주어진 OutputStream인스턴스를 출력소스(output source)로하며 지정된 크기(단위byte)의 버퍼를 갖는 BufferedOutputStream인스턴스를 생성한다.

주어진 OutputStream인스턴스를 출력소스(output source)로하며 버퍼의 크기를 지정해주지 않으므로 기본적으로 8192 byte크기의 버퍼를 갖게 된다.

버퍼의 모든 내용을 출력소스에 출력한 다음, 버퍼를 비운다.

flush()를 호출해서 버퍼의 모든 내용을 출력소스에 출력하고, BufferedOutputStream인스턴스가 사용하던 모든 자원을 반환한다.

  

BufferedOutputStream역시 버퍼를 이용해서 출력소스와 작업을 하게 되는데, 입력소스로부터 데이터를 읽을 때와는 반대로 , 프로그램에서 write메서드를 이용한 출력이 BufferedOutputStream의 버퍼에 저장된다. 버퍼가 가득 차면, 그 때 버퍼의 모든 내용을 출력소스에 출력한다. 그리고는 버퍼를 비우고 다시 프로그램으로부터의 출력을 저장할 준비를 한다.

버퍼가 가득 찼을 때만 출력소스에 출력을 하기 때문에, 마지막 출력부분이 출력소스에 쓰여지지 못하고 BufferedOutputStream의 버퍼에 남아있는 채로 프로그램이 종료될 수 있다는 점을 주의해야한다.

  

### DataInputStream과 DataOutputStream

---

각각 FilterInputStream/FilterOutputStream의 자손이며 DataInputStream은 DataInput인터페이스를 DataOutputStream은 DataOutput인터페이스를 각각 구현하였기 때문에, 데이터를 읽고 쓰는데 있어서 byte단위가 아닌, 8가지 기본 자료형의 단위로 읽고 쓸 수 있다는 장점이 있다.

  

**메서드 / 생성자**

DataInputStream(InputStream in)  
  

boolena readBoolean()  
byte readByte()  
char readChar()  
short readShort()  
int readInt()  
long readLong()  
float readFloat()  
double readDouble()  

String readUTF()  
  

int skipBytes(int n)

**설 명**

주어진 InputStream인스턴스를 기반스트림으로 하는 DataInputStream인스턴스를 생성한다.

  
  
  
각 자료형에 알맞은 값들을 읽어 온다.  
더 이상 읽을 값이 없으면 EOFException을 발생시킨다.  
  
  
  

UTF형식으로 쓰여진 문자를 읽는다.  
더 이상 읽을 값이 없으면 EOFException을 발생시킨다.  

현재 읽고 있는 위치에서 지정된 숫자(n) 만큼을 건너뛴다.

  

**메서드 / 생성자**

DataOutputStream(OutputStream out)  
  

void writeBoolean(Boolean b)  
void writeByte(int b)  
void writeChar(int c)  
void writeShort(int s)  
void writeInt(int i)  
void writeLong(long l)  
void writeFloat(float f)  
void writeDouble(double d)  

void writeUTF(String s)

void writeChars(String s)  
  

int size()

**설 명**

주어진 OutputStream인스턴스를 기반스트림으로 하는 DataOutputStream인스턴스를 생성한다.

  
  
  
  
각 자료형에 알맞은 값들을 출력한다.  
  
  
  

UTF형식으로 문자를 출력한다.

주어진 문자열을 출력한다. writeChar(int c)메서드를 여러 번 호출한 결과와 같다.

지금까지 DataOutputStream에 쓰여진 Byte의 수를 알려준다.

  

### SequenceInputStream

---

여러 개의 입력스트림을 연속적으로 연결해서 하나의 스트림으로부터 데이터를 읽는 것과 같이 처리할 수 있도록 도와준다.

  

메서드 / 생성자

SequenceInputStream(Enumeration e)  
  

SequenceInputStream(InputStream s1, InputStream s2)

설 명

Enumeration에 저장된 순서대로 입력스트림을 하나의 스트림으로 연결한다.

두 개의 입력스트림을 하나로 연결한다.

  

### PrintStream

---

데이터를 기반스트림에 다양한 형태로 출력할 수 있는 print, println, printf와 같은 메서드를 오버로딩하여 제공한다.

PrintStream은 데이터를 적절한 문자로 출력하는 것이기 때문에 문자기반 스트림의 역할을 수행한다. JDK1.1에서부터 PrintStream보다 향상된 기능의 문자기반 스트림인 PrintWriter가 추가되엇으나 그 동안 매우 빈번히 사용되던 System.out이 PrintStream이다 보니 둘 다 사용할 수 밖에 없게 되었다.

PrintStream과 PrintWriter는 거의 같은 기능을 가지고 있지만 PrintWriter가 PrintStream에 비해 다양한 언어의 문자를 처리하는데 적합하기 때문에 가능하면 PrintWriter를 사용하는 것이 좋다.

  

생성자 / 메서드

PrintStream(File file)  
PrintStream(File file, String csn)  
PrintStream(OutputStream out)  
PrintStream(OutputStream out, boolean autoFlush)  
PrintStream(OutputStream out, boolean autoFlush, String encoding)  
PrintStream(String fileName)  
PrintStream(String fileName, String csn)  

boolean checkError()

void print(...)  
void println(...)  
  

void println()  
  

PrintStream printf(String format, Object... args)

protected void setError()

설명

  
  
  
지정된 출력스트림을 기반으로 하는 PrintStream인스턴스를 생성한다. autoFlush의 값을 true로 하면 println메서드가 호출되거나 개행문자가 출력될 때 자동으로 flush된다 .기본값은 false이다.  
  
  

스트림을 flush하고 에러가 발생했는지를 알려 준다.

인자로 주어진 값을 출력소스에 문자로 출력한다.  
println메서드는 출력 후 줄바꿈을 하고, print메서드는 줄을 바꾸지 않는다.  

줄바꿈 문자(line separator)를 출력함으로써 줄을 바꾼다.

정형화된(formatted) 출력을 가능하게 한다.  
  

작업 중에 오류가 발생했음을 알린다.  
(setError()를 호출한 후에, checkError()를 호출하면 true를 반환한다.)  

  

## 문자기반 스트림

문자데이터를 다루는데 사용된 다는 것을 제외하고는 바이트기반 스트림과 문자기반 스트림의 사용방법은 거의 같다.

  

### Reader와 Writer

---

바이트기반 스트림의 조상이 InputStream/OutputStream인 것과 같이 문자기반의 스트림에서는 Reader/Writer가 가와 같은 역할을 한다.

문자기반 스트림이라는 것이 단순이 2byte로 스트림을 처리하는 것만을 의미하지는 앟는 다는 것이다. 문자 데이터를 다루는데 필요한 또 하나의 정보는 인코딩(encoding)이다.

  

**메서드**

abstract void close()

void mark(int readlimit)  
  

boolean markSupported()

  
int read()  
  

int read(char[] c)  
  

abstract int read(char[] c, int off, int len)  
  

boolean ready()

void reset()  
  

long skip(long n)

**설 명**

입력스트림을 닫음으로써 사용하고 있던 자원을 반환한다.

현재위치를 표시해놓는다. 후에 reset()에 의해서 표시해 높은 위치로 다시 돌아갈 수 있다.

mark()와 reset()을 지원하는지를 알려 준다.

입력소스로부터 하나의 문자를 읽어 온다. char의 범위인 0~65535범위의 정수를 반환하며, 입력스트림의 마지막 데이터에 도달하면, -1을 반환한다.

입력소스로부터 매개변수로 주어진 배열 c의 크기만큼 읽어서 배열 c에 저장한다. 읽어 온 데이터의 개수 또는 -1을 반환한다.

입력소스로부터 최대 len개의 문자를 읽어서, 배열 c의 지정된 위치(off)부터 읽은 만큼 저장한다. 읽어 온 데이터의 개수 또는 -1을 반환한다.

입력소스로부터 데이터를 읽을 준비가 되어있는지 알려 준다.

입력소스에서의 위치를 마지막으로 mark()가 호출되었던 위치로 되돌린다.

현재 위치에서 주어진 문자 수(n)만큼을 건너뛴다.

  

**메서드**

abstract void close()

abstract void flush()  
  

void write(int b)

void write(char[] c)

abstract void write(char[] c, int off, int len)

void write(String str)

void write(String str, int off, int len)

**설 명**

출력스트림을 닫음으로써 사용하고 있던 자원을 반환한다.

스트림의 버퍼에 있는 모든 내용을 출력소스에 쓴다.(버퍼가 있는 스트림에만 해당됨)

주어진 값을 출력소스에 쓴다.

주어진 배열 c에 저장된 모든 내용을 출력소스에 쓴다.

주어진 배열 c에 저장된 내용 중에서 off번째부터 len길이만큼만 출력소스에 쓴다.

주어진 문자열(str)을 출력소스에 쓴다.

주어진 문자열(str)의 일부를 출력소스에 쓴다.(off번째 문자부터 len개 만큼의 문자열)

  

### FileReader와 FileWriter

---

파일로부터 텍스트데이터를 읽고, 파일에 쓰는데 사용된다.

  

### PipedReader와 PipedWriter

---

쓰레드 간에 데이터를 주고받을 때 사용된다. 다른 스트림과는 달리 입력과 출력스트림을 하나의 스트림으로 연결(connect)해서 데이터를 주고받는다는 특징이 있다.

스트림을 생성한 다음에 어느 한쪽 쓰레드에서 connect()를 호출해서 입력스트림과 출력스트림을 연결한다. 입출력을 마친 후에는 어느 한쪽 스트림만 닫아도 나머지 스트림은 자동으로 닫힌다.

  

### StringReader와 StringWriter

---

CharArrayReader/CharArrayWriter와 같이 입출력 대상이 메모리인 스트림이다.

StringWriter에 출력되는 데이터는 내부의 StringBuffer에 저장되며 StringWriter의 다음과 같은 메서드를 이용해서 저장된 데이터를 얻을 수 있다.

> StringBuffer getBuffer() : StringWriter에 출력한 데이터가 저장된 StringBuffer를 반환한다.  
> String toString() : StringWriter에 출력된(StringBuffer에 저장된) 문자열을 반환한다.  

  

## 문자기반의 보조스트림

### BufferedReader와 BufferedWriter

---

버퍼를 이용해서 입출력의 효율을 높일 수 있도록 해주는 역할을 한다. 버퍼를 이용하면 입출력의 효율이 비교할 수 없을 정도로 좋아지기 때문에 사용하는 것이 좋다.

BufferedReader의 readLine()을 사용하면 데이터를 라인단위로 읽어 올 수 있다는 장점이 있다.

  

### InputStreamReader와 OutputStreamWriter

---

이름에서 알 수 있는 것과 같이 바이트기반 스트림을 문자기반 스트림으로 연결시켜주는 역할을 한다. 그리고 바이트기반 스트림의 데이터를 지정된 인코딩의 문자데이터로 변환하는 작업을 수행한다.

  

**생성자 / 메서드**

InputStreamReader(InputStream in)  
  

InputStreamReader(InputStream in, String encoding)

String getEncoding()

**설 명**

OS에서 사용하는 기본 인코딩의 문자로 변환하는 InputStreamReader를 생성한다.

지정된 인코딩을 사용하는 InputStreamReader를 생성한다.

InputStreamReader의 인코딩을 알려 준다.

  

**생성자 / 메서드**

OutputStreamWriter(OutputStream in)  
  

OutputStreamWirter(OutputStream in, String encoding)

String getEncoding()

**설 명**

OS에서 사용하는 기본 인코딩의 문자로 변환하는 OutputStreamWriter를 생성한다.

지정된 인코딩을 사용하는 OutputStreamWriter를 생성한다.

OutputStreamWriter의 인코딩을 알려 준다.

  

한글윈도우에서 중국어로 작성된 파일을 읽을 때 InputStreamReader(InputStream in, String encoding)를 이용해서 인코딩이 중국어로 되어 있다는 것을 지정해주어야 파일의 내용이 깨지지 않고 올바르게 보일 것이다. 인코딩을 지정해 주지 않는다면 OS에서 사용하는 인코딩을 사용해서 파일을 해석해서 보여 주기 때문에 원래 작성된 데로 볼 수 없을 것이다.  
이와 마찬가지로 OutputStreamWriter를 이용해서 파일에 텍스트데이터를 저장할 때 생성자 OutputStreamWriter(OutputStream in, String encoding)를 이용해서 인코딩을 지정하지 않으면 OS에서 사용하는 인코딩으로 데이터를 저장할 것이다.  

  

## 표준입출력과 File

### 표준입출력 - System.in, Syste.out, System.err

---

표준입출력은 콘솔(console, 도스창)을 통한 데이터 입력과 콘솔로의 데이터 출력을 의미한다.

> [System.in](http://system.in) - 콘솔로부터 데이터를 입력받는데 사용  
> System.out - 콘솔로 데이터를 출력하는데 사용  
> System.err - 콘솔로 데이터를 출력하는데 사용  

Ssytem큰ㄴ래스의 소스에서 알 수 있듯이 in, out, err은 System클래스에 선언된 클래스변수(static변수)이다. 선언부분만을 봐서는 out, err, in의 타입은 inputStream과 PrintStream이지만 실제로는 버퍼를 이용하는 BufferedInputStream, BufferedOutputStream의 인스턴스를 사용한다.

  

### 표준입출력의 대상변경 - setOut(), setErr(), setIn()

---

초기에는 System.in, System.out, System.err의 입출력대상이 콘솔화면이지만, setIn(), setOut(), setErr()를 사용하면 입출력을 콘솔 이외에 다른 입출력 대상으로 변견하는 것이 가능하다.

```Java
import java.io.*;

class StandardIOEx3 {
	public static void main(String[] args) {
		PinrtStream ps = null;
		FileOutputStream fos = null;

		try {
			fos = new FileOutputStream("test.txt");
			ps = new PrintStream(fos);
			System.setOut(ps);
		}
		catch (FileNotFoundException e) {
			System.out.println("File not found");
		}

		System.out.println("Hello by System.out");
		System.err.println("Hello by System.err");
	}
}
```

System.out의 출력 소스를 test.txt파일로 변경하였기 때문에 System.out을 이용한 출력은 모두 test.txt파일에 저장된다. 그래서 실행결과에는 Ssytem.err를 이용한 출력만 나타낸다.

  

### RansdomAccessFile

---

자바에서는 입력과 출력이 각각 분리되어 별도로 작업을 하도록 설계되어 있는데, RandomAccessFile만은 하나의 클래스로 파일에 대한 입력과 출력을 모두 할 수 있도록 되어 있다.

DataInput인터페이스의 dataOutput인터페이스를 모두 구현했기 때문에 읽기와 쓰기가 모두 가능하다. 따라서 RandomAccessFile클래스도 DataInputStream과 DataOutputStream처럼, 기본 자료형 단위로 데이터를 읽고 쓸 수 있다.

RnadomAccessFile클래스의 가장 큰 장범은 파일의 어느 위치에나 읽기/쓰기가 가능하다는 것이다. 다른 입출력 클래스들은 입출력소스에 순차적으로 읽기/쓰기를 하기 때문에 읽기와 쓰기가 제한적인데 반해서 RandomAccessFile클래스는 파일에 읽고 쓰는위치에 제한이 없다.

  

이것을 가능하게 하귀 위해서 내부적으로 파일 포인터를 사용하는데, 입출력 시에 작업이 수행되는 곳이 바로 파일 포인터가 위치한 곳이 된다.  
파일 포인터의 위치는 파일의 제일 첫 부분(0부터 시작)이며, 읽기 또는 쓰기를 수행할 때 마다 작업이 수행된 다음 위치로 이동하게 된다. 순차적으로 읽기나 쓰기를 한다면, 파일 포인터를 이동시키기 위해 별도의 작업이 필요하지 않지만, 파일의 임의의 위치에 있는 내용에 대해서 작업하고자 한다면, 먼저 파일 포인터를 원하는 위치로 옮긴다음 작업을 해야 한다.  

현재 작업 중인 팡리에서 파일 포인터의 위치를 알고 싶을 때는 getFilePointer()를 사용하면 되고, 파일 포인터의 위치를 옮기기 위해서는 seek(long pos)나 skipByte(int n)를 사용하면 된다.

  

### File

---

파일은 기본적적이면서도 가장 많이 사용되는 입출력 대상이기 때문에 중요하다.

자바에서는 File클래스를 통해서 파일과 디렉토리를 다룰 수 있도록 하고 있다. 그래서 File인스턴스는 파일 일 수도 있고 디렉토리 일 수도 있다.

생성자 / 메서드

  
  
File(String fileName)  
  
  

File(String pathName, String fileName)  
File(File pathName, String fileName)  
  

String getName()

String getPath()

StringgetAbsolutePath()  
File getAbsoluteFile()  

String getParent()  
File getParentFile()  

String getCanonicalPath()  
File getCanonicalFile()  

설명

주어진 문자열(fileName)을 이름으로 갖는 파일을 위한 File인스턴스를 생성한다. 파일 뿐만 아니라 디렉토리도 같은 방법으로 다룬다. 여기서 fileName은 주로 경로(path)를 포함해서 지정해주지만, 파일 이름만 사용해도 되는 데 이 경우 프로그램이 실행되는 위치가 경로(paht)로 간주된다.

파일의 경로와 이름을 따로 분리해서 지정할 수 있도록 한 생성자. 이 중 두 번째 것은 경로를 문자열이 아닌 File인스턴스인 경우를 위해서 제공된 것이다.

파일 이름을 Stirng으로 반횐된다.

파일의 경로(path)를 String으로 반환한다.

파일의 절대경로를 String으로 반환한다.  
파일의 절대경로를 File로 반환한다.  

파일의 조상 디렉토리를 String으로 반환한다.  
파일의 조상 디렉토리를 File로 반환한다.  

파일의 정규경로를 String으로 반환한다.  
파일의 정규경로를 File로 반환한다.  

  

멤버변수

static String ptathSeparator

static char pathSeparatorChar  
  

static String separator

static char separatorChar

설명

OS에서 사용하는 경로(path) 구분자. 윈도우":", 유닉스 ":"

OS에서 사용하는 경로(path) 구분자.  
윈도우에서는 ':', 유닉스 ':'  

OS에서 사용하는 이름 구분자. 윈도우 "₩", 유닉스 "/"

OS에서 사용하는 이름 구분자. 윈도우 '₩', 유닉스 '/'

  

File인스턴스를 생성했다고 해서 파일이나 디렉토리가 생성되는 것은 아니라는 것이다. 파일명이나 디렉토리명으로 지정된 문자열이 유효하지 않더라도 컴파일 에러나 예외를 발생시키지 않는다.  
새로운 파일을 싱성하기 위해서는 File인스턴스를 생성한 다음, 출력스트림을 생성하거나 createNewFile()를 호출해야한다.  

> 1. 이미 존재하는 파일을 참조할 때 :  
> File f = new File("c:...", "FileEx1.java");  
>   
> 2. 기존에는 없는 파일을 새로 생성할 때 :  
> File f = new File("c:...", "NewFile.java");  
> f.createNewFile(); // 새로운 파일이 생성된다.  

  

메서드

boolean cnaRead()

boolean canWrite()

boolean exists()

boolean isAbsolute()

boolean isDirectory()

boolean isFile()

boolean isHidden()  
  

  
int compareTo(File pathname)  
  

  
  
boolean createNewFile()  
  

static File createTempFile(String prefix, String suffix)  
  

static File createTempFile(String prefix, String suffix, File directory)

boolean delete()

void deleteOnExit()  
  

  
boolean equals(Object obj)  
  

long length()

String[] list()

String[] list(FilenameFilter filter)  
  

File[] listFiles()

static File[] listRoots()

설 명

읽을 수 있는 파일인지 검사한다.

쓸 수 있는 파일인지 검사한다.

파일이 존재하는지 검사한다.

파일 또는 디렉토리가 절대경로명으로 지정되었는지 확인한다.

디렉토리인지 확인한다.

파일인지 확인한다.

파일의 속성이 '숨김(hidden)'인지 확인한다.  
또한 파일이 존재하지 않으면 false를 반환한다.  

주어진 파일 또는 디렉토리를 비교한다. 같으면 0을 반환하며, 다르면 1 또는 -1을 반환한다. (Unix 시스템에서는 대소문자를 구별하며, Windows에서는 구별하지 않는다.)

아무런 내용이 ㅇ벗는 새로운 파일을 생성한다. (단, 생성하려는 파일이 이미 존재하면 생성되지 않는다.)  
File f = new Fiel("c:...java");  
f.createNewFile();  

임시파일을 시스템의 임시 디렉토리에 생성한다.  
System.out.println(File.createTempFile("work", ".tmp"));  
결과 : c:...work14247.tmp  

  
임시파일을 시스템의 지정된 디렉토리에 생성한다.  

파일을 삭제한다.

응용 프로그램 종료시 파일을 삭제한다. 주로 실행 시 작업에 사용된 임시파일을 삭제하는데 사용된다.

주어진 객체(주로 File인스턴스)가 같은 파일인지 비교한다.  
(Unix시스템에서는 대소문자를 구별하며, Windows에서는 구별하지 않는다.)  

파일의 크기를 반환한다.

디렉토리의 파일목록(디렉토리 포함)을 String배열로 반환한다.

FilenameFilter인스턴스에 구현된 조건에 맞는 파일을 String배열로 반환한다.

디렉토리의 파일목록(디렉토리 포함)을 File배열로 반환한다.

컴퓨터의 파일시스템의 root의 목록(floppy, CD-ROM, HDD drive)을 반환한다.(ex: A:, C:)

  

## 직렬화(Serialization)

### 직렬화란?

---

직렬화(serialization)란 객체를 데이터 스트림으로 만드는 것을 뜻한다. 다시 얘기하면 객체에 저장된 데이터를 스트림에 쓰기(wirte)위해 연속적인(serial) 데이터로 변환하는 것을 말한다.  
반대로 스트림으로부터 데이터를 읽어서 객체를 만다는 것을 역직렬화(deserialization)라고 한다.  

  

✲ 객체를 저장한다는 것은 무엇을 의미하는가에 대해서 다시 한 번 정리.

객체는 클래스에 정의된 인스턴스 변수의 집합이다. 객체에는 클래스변수나 메서드가 포함되지 않는다. 객체는 오직 인스턴스변수들로만 구성되어 있다.  
사실 객체에는 메서드가 포함되지 않는다. 인스턴스변수는 인스턴스마다 다른 값을 가질 수 있어야하기 때문에 별도의 메모리공간이 필요하지만 메서드는 변하는 것이 아니라서 메모리를 낭비해 가면서 인스턴스마다 같은 내요의 코드(메서드)를 포함시킬 이유가 없다.  

객체를 저장한다는 것은 바로 객체의 모든 인스턴스변수의 값을 저장한다는 것과 같은 의미이다. 어떤 객체를 저장하고자 한다면, 현재 객체의 모든 인스턴스변수의 값을 저장하기만 하면 된다. 그리고 저장했던 객체를 다시 생성하려면 객체를 생성한 후에 저장했던 값을 읽어서 생성한 객체의 인스턴스변수에 저장하면 되는 것이다.

  

### ObjectInputStream, ObjectOutputStream

---

직렬화(스트림에 객체를 출력)에는 ObjectOutputStream을 사용하고 역직렬화(스트림으로부터 객체를 입력)에는 ObjectInputStream)을 사용한다.  
각각 inputStream과 OutputStream을 직접 상속받지만 기반 스트림을 필요로 하는 보조스트림이다. 그래서 객체를 생성할 때 입출력(직렬화/역직렬화)할 스트림을 지정해주어야 한다.  

> ObjectInputStream(InputStream in)  
> ObjectOutputStream(OutputStream out)  

  

만일 파일에 객체를 저장(직렬화)하고 싶다면 다음과 같이 하면 된다.

> FileOutputStream fos = new FileOutputStream("objectfile.ser");  
> ObjectOutputStream out = new ObjectOutputStream(fos);  
>   
> out.wirteObject(new UserInfo());  

> FileInputStream fis = new FileInputStream("objectfile.ser");  
> ObjectInputStream in = new ObjectInputStream(fis);  
>   
> UserInfo info = (UserInfo) in.readObject();  

  

객체를 직렬화/역직렬화하는 작업은 객체의 모든 인스턴스변수가 참조하고 있는 모든 객체에 대한 것이기 때문에 상당히 복잡하며 시간도 오래 걸린다. ReadObject()와 writeObject()를 사용한 자동 직렬화가 편리하기는 하지만 직렬화작업시간을 단축시키려면 직렬화하고자 하는 객체의 클래스에 추가적으로 다음과 같은 2개의 메서드를 직접 구현해주어야 한다.

```Java
private void writeObject(ObjectOupputStream out) {
	throws IOException {
		// write메서드를 사용해서 직렬화를 수행한다.
	}

private void readObject(ObjectInputStream in) {
	throws IOException, ClassNotFoundException e) {
	// read메서드를 사용해서 역직렬화를 수행한다.
}
```

  

### 직렬화가 가능한 클래스 만들기 - Serializable, transient

---

직렬화가 가능한 클래스를 만드는 방법을 간단하다. 직렬화하고자 하는 클래스가 java.io.Serializable인터페이스를 구현하도록 하면된다.

```Java
public class UserInfo implements java.io.Srializable {
	String name;
	String password;
	int age;
}
```

Serializable 인터페이스는 아무런 내용도 없는 빈 인터페이스이지만, 직렬화를 고려하여 작성한 클래스인지를 판단하는 기준이 된다.

Serializable을 구현한 클래스를 상속받는다면, Serializable을 구현하지 않아도 된다. UserInfo객체를 직렬화하면 조상인 SuperUserInfo에 정의된 인스턴스변수도 함께 직렬화된다.

그러나 다음과 같이 조상클래스가 Serializable을 구현하지 않았다면 자손 클래스를 직렬화할 때 조상클래스에 정의된 인스턴스변수는 직렬화 대상에서 제외된다.

조상클래스에 정의된 인스턴스변수를 직렬화 대상에 포함시키기 위해서 는 조상클래스가 Serializable을 구현하도록 하던가, UserInfo에서 조상의 인스턴스변수들이 직렬화되도록 처리하는 코드를 직접 추가해 주어야한다.

  

모든 클래스의 최고조상인 Object는 Serializable을 구현하지 않았기 때문에 직렬화할 수 없다.

```Java
public class UserInfo implements Serializable {
	String name;
	String password;
	int age;

	Object obj = new Object();    // Object객체는 직렬화할 수 없다.
}
```

  

위의 경우와 비교해서 다음과 같은 경우에는 직렬화가 가능하다는 것을 알아두자. 인스턴스변수의 타입이 아닌 실제로 연결된 객체의 종류에 의해서 결정된다는 것을 기억하자.

```Java
public class UserInfo implements Serializable {
	String name;
	String password;
	int age;

	Object obj = new String("abc");    // String은 직렬화될 수 있다.
}
```

직렬화하고자 하는 객체의 클래스에 직렬화가 안 되는 객체에 대한 참조를 호함하고 있다면, 제어자 transient를 붙여서 직렬화 대상에서 제외되도록 할 수 있다.  
또는 password와 같이 보안상 직렬화되면 안되는 값에 대해서 transient를 사용할 수 있다. 다르게 표현하면 transient가 붙은 인스턴스변수의 값은 그 타입의 기본값으로 직렬화된다고 볼 수 있다.  
즉, UserInfo객체를 역직렬화하면 참조변수인 obj와 password의 값은 null이 된다.  

```Java
public class UserInfo implements Serializable {
	String name;
	transient String password;    // 직렬화 대상에서 제외된다.
	int age;

	transient Object obj = new Object();    // 직렬화 대성에서 제외된다.
}
```

  

### 직렬화가능한 클래스의 버전관리

---

직렬화된 객체를 역직렬화할 때는 직렬화 했을 때와 같은 클래스를 사용해야 한다. 그러나 클래스의 이름이 같더라도 클래스의 내용이 변경된 경우 역직렬화는 실패하며 다음과 같은 예외가 발생한다.

```Java
java.io.InvalidClassException: UserInfo; local class incompatible:
```

  

네트웍으로 객체를 직렬화하여 전송하는 경우, 보내는 쪽과 받는 쪽이 모두 같은 버전의 클래스를 가지고 있어야하는데 클래스가 조금만 변경되어도 해당 클래스를 재배포하는 것은 프로그램을 관리하기 어렵게 만든다.

이럴 때는 클래스의 버전을 수동으로 관리해줄 필요가 있다.
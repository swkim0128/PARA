---
type: Java
archive: false
---
## 공공데이터와 XML

### 공공데이터란?

---

공공기간이 만들어내는 모든 공적인 정보

각 공공기관이 보유한 데이터를 개방하여 누구나 원하는 기능에 활용 가능

[www.data.go.kr](http://www.data.go.kr) 등 회원 가입 후 개별 키를 발급 받아 사용

  

### XML

---

**Markup Language**

태그등을 이용하여 문서나 데이터의 구조를 명기하는 언어

HTML, SGML, ...

  

**XML**

Extensible Markup Language

HTML과 달리 필요에 따라서 태그를 확장해서 사용 가능

정확한 문법을 지켜야 동작 : Well formed

  

**기본 문법**

문서의 시작은 <?xml version="1.0" encoding="UTF-8"?>로 한다.

만드시 root element가 존재한다. 나머지 태그들은 Tree 형태로 구성된다.

시작태그와 종료 태그는 일치해야 한다.

시작 태그는 key-value구조의 속성을 가질 수 있다.

속성 값은 "" 또는 ''로 묶어서 표현한다.

대소문자를 구별한다.

  

**vaild**

xml 태그는 자유롭게 생성하기 때문에 최초 작성자의 의도대로 작성되는지 확인할 필요(DTD 또는 Schema를 이용해서 문서의 규칙 작성)

  

### XML파싱

---

**파싱**

문서에서 필요한 정보를 얻기 위해 태그를 구별하고 내용을 추출하는 과정

  

**SAX parser**

Simple API for XML parser

문서를 읽으면서 태그의 시작, 종료 등 이벤트 기반으로 처리하는 방식

빠르고 한번에 처리하기 때문에 다양한 탐색이 어렵다.

  

**DOM parser**

Document Object Model

문서를 다 읽고 난 후 문서 구조 전체를 자료구조에 저장하여 탐색하는 방식

다양한 탐색이 가능하지만 느리고 무거우며 큰 문서를 처리하기 어렵다.

  

### SAX(Simple API for XML) Parser

---

**정보를 저장하기 위한 클래스 구성**

```Java
public class BoxOffice {
	private Integer rank;
	private String movieNm;
	private Date openDt;
	private Integer audiAcc;

	public Date toDate(String date) {
		SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
		try {
			return format.arse(date);
		}
		catch (ParseException e) {
			e.printStackTrace();
			return new Date();
		}
	}
}
```

  

**Handler 작성**

```Java
public class BoxOfficeSaxParser extends DefaultHandler {
	private final Fild xml = new File(".../boxoffice.xml");
	private List<BoxOffice> list = new ArrayList<>();
	private BoxOffice current;
	private String content;
	public List<BoxOffice> getBoxOffice() {
		try {
			SAXParserFactory factory = SAXParserFactory.newInstance();
			SAXParser parser = factory.newSAXParser();
			parser.parse(xml, this);
		}
		catch (IOException | SAXException | ParserConfigurationException e) {
			e.printStackTrace();
		}
		return list;
	}

	@Override
	public void startDocument() throws SAXException {
		Syste.out.println("문서시작");
	}

	@Override
	public void endDocument() throws SAXException {
		System.out.println("문서 종료");
	}

	@Override
	public void startElement(String uri, String localname, String qName, 
										Attributes attirbutes) throws SAXException {
		if (qName.equals("dailyBoxOffice")) {
			current = new BoxOffice();
		}
	}

	@Override
	public void characters(char[]ch, int start, int length) throws SAXException {
		this.content = new String(ch, start, length);
	}

	@Override
	public void endElement(String uri, String localName, String qName) throws SAXException {
		if (qName.equals("dailyBoxOffice")) {
			list.add(current);
			current = null;
		}
		else if (qName.equals("rank")) {
			current.setRank(Integer.parseInt(content));
		}
		else if (qName.equals("movieNm")) {
			current.setMovieNm(Integer.parseInt(content));
		}
		else if (qName.equals("openDt")) {
			current.setOpenDt(current.toDate(this.content));
		}
		else if (qName.equals("audiAcc")) {
			current.setAudiAcc(Integer.parseInt(content));
		}
	}
}
```

  

**XML 파싱 및 결과 확인**

```Java
public class SaxParserTest {
	public static void main(String[] args) {
		BoxOfficeSaxParser hanlder = new BoxOfficeSaxParser();

		List<BoxOffice> list = hanlder.getBoxOffice();
		for (BoxOffice boxOffice : list) {
			System.out.println(boxOffice);
		}
	}
}
```

  

### DOM Parser

---

DOM Tree

문서를 구성하는 모든 요소를 Node(태그, 속성, 값)로 구성

태그들은 root 노드(주소록)을 시작으로 부모-자식의 관계 구성
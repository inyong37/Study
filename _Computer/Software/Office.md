# Office

## Document Object Model(DOM) | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EB%AC%B8%EC%84%9C_%EA%B0%9D%EC%B2%B4_%EB%AA%A8%EB%8D%B8)
DOM은 객체 지향 모델로써 구조화된 문서를 표현하는 형식이다. DOM은 플랫폼/언어 중립적으로 구조화된 문서를 표현하는 W3C의 공식 표준이다. DOM은 또한 W3C가 표준화한 여러 개의 API의 기반이 왼다. DOM은 HTML 문서의 요소를 제거하기 위해 web browswer에서 처음 지원되었다. DOM은 동적으로 문서의 내용, 구조, 스타일에 접근하고 변경하는 수단이었다. Browswer 사이에 DOM 구현이 호환되지 않음에 따라, W3C에서 DOM 표준 규격을 작성하게 되었다. DOM은 문서의 기반이 되는 데이터 구조에 제한을 두지 않는다. 잘 구조화된 문서는 DOM을 사용하여 트리 구조를 얻어낼 수 있다. 대부분의 XML 해석기와 XSL 처리기는 트리 구조의 이용에 대응해 개발되었다. 이 같은 구현에서는 문서의 전체 내용이 해석되어 메모리 저장되어야 한다. 때문에 DOM은 문서 요소가 임의적으로 접근되고 변경할 수 있어야 하는 응용 프로그램에 가장 적합하다. 한 번 해석 시 단 한 번의 선택적 읽기/쓰기가 이루어지는 XML 기반 응용 프로그램에서, DOM은 메모리에 상당한 부하를 가져온다. 이 경우처럼 속도와 효율적인 메모리 소비가 중요한 상황일 경우 SAX 모델이 장점을 가진다.

DOM은 HTML, XML 문서의 프로그래밍 interface이다. DOM은 문서의 structured representation을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공하여 문서 구조, 스타일, 내용 등을 변경할 수 있게 돕는다. DOM은 구조화된 nodes와 property와 method를 갖고 있는 objects로 문서를 표현한다. Web pages를 script 또는 프로그래밍 언어들에서 사용될 수 있게 연결시켜주는 역할을 한다. Web pages는 일종의 document다. 이 문서는 web browser를 통해 그 내용이 해석되어 web browser 화면에 나타나거나 HTML 소스 자체로 나타나기도 한다. 동일한 문서를 사용하여 이처럼 다른 형태로 나타날 수 있다는 점에 주목할 필요가 있다. DOM은 동일한 문서를 표현하고 저장하고 조작하는 방법을 제공한다. DOM은 web pages의 객체 지향 표현이며 자바스크립트와 같은 scripting language를 이용해 DOM을 수정할 수 있다.

## Office Open XML(OOXML) | [Homepage](http://officeopenxml.com/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EC%98%A4%ED%94%BC%EC%8A%A4_%EC%98%A4%ED%94%88_XML)
OOXML은 XML 기반으로 한 file format으로, Microsoft가 추진했으며 2006, 2008년 2차례에 걸쳐 ECMA International에 유럽 표준(ECMA-376), ISO/IEC에 국제 표준(ISO/IEC 29500)으로 승인되었다. 이 문서 규격은 문서, 프레젠테이션, 스프레드시트를 포함한다. 확장자는 .docx(문서, .pptx(프레젠테이션), .xlsx(스프레드시트)로 통일되어 있다.

OOXML file format은 zip 형태로 압축된 XML 기반의 file format이다. Package(OOXML file의 zip 파일 해제 시 나오는 폴더와 파일 구조들)의 구조는 pptx, xlsx, docx 파일은 UTF-8  또는 UTF-16으로 encoding된 여러 파트 또는 XML 파일들을 담고 있는 zip 파일을 해제하면 볼 수 있다.

## Extensible Markup Lanaguage(XML) | [Homepage](https://www.w3.org/XML/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/XML)
XML은 W3C에서 개발된 다른 특수한 목적을 갖는 마크업 언어를 만드는데 사용하도록 권장하는 다목적 마크업 언어이다. XML은 SGML의 단순화된 부분집합으로 다른 많은 종류의 데이터를 기술하는 데 사용할 수 있다. XML은 주로 다른 종류의 시스템, 특히 인터넷에 연결된 시스템끼리 데이터를 쉽게 주고 받을 수 있게 하여 HTML의 한계를 극복할 목적으로 만들어졌다.

## Parsing(구문 분석) | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EA%B5%AC%EB%AC%B8_%EB%B6%84%EC%84%9D)
언어학에서 구문 분석(구문 해석, 문장 해석) 또는 parsing은 문장을 이루고 있는 구성 성분으로 분해하고 그들 사이의 위계 관계를 분석하여 문장의 구조를 결정하는 것을 말한다.

In computer science, parsing은 일련의 문자열을 의미있는 token으로 분해하고 이들로 이루어진 parse tree를 만드는 과정을 말한다. Parsing 방식에는 top-down(하향식), and bottom-top(상향식)이 있다. 전산 언어, 자연어 처리, 기계 번역 등의 분야에서는 전산학의 parsing method를 인간 언어를 구문 분석하는 데 적용하려고 한다.

## Document Object Model(DOM) Parsing
XML 문서를 모두 메모리에 로드한 후 값을 읽는다. XML 문서가 메모리에 모두 로드외어 있기 떄문에 노드의 검색, 수정, 구조 변경 등이 빠르고 용이하다. 직관적이고 SAX보다 파싱하기 단순하다.

## Simple API for XML(SAX) Parsing
XML 문서를 순차적으로 읽어들이면서 노드가 열리고 닫히는 과정에서 이벤트가 발생한다. XML 문서를 메모리에 전부 로딩하고 파싱하는 것이 아니라서 메모리 사용량이 적고 단순히 읽기만 할 떄 속도가 빠르다. 발생한 이벤트를 핸들링하여 변수에 저장, 활용하는 것이기 때문에 복잡하고 노드 수정이 어렵다. DOM parsing보다 어렵다.

#### Reference
- Office Open XML, http://officeopenxml.com/, 2021-03-09-Tue.
- Office Open XML Wiki KR, https://ko.wikipedia.org/wiki/%EC%98%A4%ED%94%BC%EC%8A%A4_%EC%98%A4%ED%94%88_XML, 2021-03-09-Tue.
- OOXML Blog KR, https://blog.naver.com/PostView.nhn?blogId=empty7792&logNo=221508900148&parentCategoryNo=&categoryNo=11&viewDate=&isShowPopularPosts=true&from=search, 2021-03-09-Tue.
- XML, https://www.w3.org/XML/, 2021-03-09-Tue.
- XML Wiki KR, https://ko.wikipedia.org/wiki/XML, 2021-03-09-Tue.
- DOM Wiki KR, https://ko.wikipedia.org/wiki/%EB%AC%B8%EC%84%9C_%EA%B0%9D%EC%B2%B4_%EB%AA%A8%EB%8D%B8, 2021-03-09-Tue.
- DOM Blog KR, https://developer.mozilla.org/ko/docs/Web/API/Document_Object_Model/Introduction, 2021-03-09-Tue.
- Parsing Wiki KR, https://ko.wikipedia.org/wiki/%EA%B5%AC%EB%AC%B8_%EB%B6%84%EC%84%9D, 2021-03-09-Tue.
- DOM Parsing vs. SAX Parsing Blog KR, https://humble.tistory.com/23, 2021-03-09-Tue.

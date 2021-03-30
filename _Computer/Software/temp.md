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


# View

### Combo Box
#### Basic
선택항목이 숨어있지 않고 화면에 처음부터 노출되어 있다. 사용자가 텍스트를 입력할 수 있다.

#### Dropdown
선택항목이 숨어있어 화살표 버튼을 누르면 펼쳐져서 사용자가 선택할 수 있다. 텍스트를 입력할 수 있다.

#### Dropdown list
선택항목이 숨어있다 콤보박스를 선택하면 선택항목이 펼쳐져 선택할 수 있다. 텍스트를 입력할 수 없다. 선택항목 중에 한가지만 선택 가능하다.

## Widget | [Wiki](https://en.wikipedia.org/wiki/Graphical_widget)
컴퓨터 프로그램에서 Widget(위젯) 또는 Control(컨트롤)은 사용자가 상호 작용하는 인터페이스 요소이다. 위젯은 위젯 스스로를 물리적인 대응물과 구별하기 위해 virtual 자격을 갖는다. 마우스 커서로 클릭되는 가상 버튼과 그의 대응물인 손가락으로 눌리는 물리적 버튼을 들 수 있다. Widget이라는 용어는 소형 장치나 요소를 뜻한다. 1980년애데 프로젝트 아테나가 최초로 GUI 요소를 widget이라고 부르기 시작했다.

Widget (GUI), a control element in a graphical user interface – an element of interaction, such as a button or a scroll bar.

## Window | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EC%B0%BD_(%EC%BB%B4%ED%93%A8%ED%8C%85))
Window(창)은 컴퓨터 프로그램에서 보통 사각형의 모양을 갖는 시각적인 영역이다. 여러 종류의 사용자 인터페이스를 포함하며 동시에 실행하는 수많은 컴퓨터 프로세스들 가운데 하나에 대해 입력을 허용하고 출력물을 보여준다. 창은 주로 그래픽 디스플레이와 연결되어 있으며, 여기서 창은 포인터로 쓰일 수 있다. 창을 주변형들 가운데 하나로 사용하는 Graphic User Interface(GUI, 그래픽 사용자 인터페이스)를 윈도 시스템이라고 부른다.

처음에 이 개념은 더글러스 엥겔바트 주도하에 스탠포드 연구소의 연구원들이 개발한 것이다. 이 시스템은 겹치지 않는 정렬된 창을 사용하였다. 나중에 앨런 케이의 주도하에 PARC의 제록스사 팔로 알토 연구 센터의 WIMP의 일부로 개발되었다. 이 시스템은 창을 겹치는 것을 허용하였다. 창을 겹치는 시스템은 창을 겹치지 못하는 시스템보다 더 일상화로 자리 잡기 시작하였다. 애플 사의 창립자 스티브 잡스는 PARC를 방문하여 GUI의 잠재력을 보고 제록스와 인터페이스의 버전을 가꿔나가기 시작했다. 끝내 애플의 리사를 위해 독립적으로 개발하였고, 나중에 매킨토시 컴퓨터 라인에 추가되었다. 이 라인은 GUI 시장에 처음으로 성공을 가져다 주었다. 마이크로소프트 사의 창립자 빌 게이츠는 이러한 인터페이스의 초기 지원자였고, 마이크로소프트가 오늘날 개인용 컴퓨터 시장을 지배했던 이와 비슷한 시스템을 개발하기 앞서 처음에 잡스의 파트너로서 맥을 위한 창 기반의 응용 프로그램을 개발하는 데에 집중하였다.

창은 거의 언제나 바탕 화면 위에 정리된 두 개의 객체(종이와 책과 같은)로 그려진다. 대부분의 창은 크기를 조절하고, 움직이고, 숨기고, 원래 크기로 되돌리고, 사용자의 의지로 닫을 수 있다. 두 창이 겹칠 때, 하나는 위에 있고 다른 하나는 일부가 가려져 보이지 않는다. 그러나 텍스트 사용자 인터페이스를 사용하는 많은 프로그램들(Emacs)은 창으로 불리는 영역을 분리하는 것을 허용하였다. 이러한 기능들을 관리하는 창 시스템 일부를 창 관리자라고 부른다.

### *CWM, Calm Window Manager* | [Wiki](https://en.wikipedia.org/wiki/Cwm_(window_manager))
Calm Window Manager(CWM) is a stacking window manager for the X Window System. While it is primarily developed as a part of OpenBSD's base system, portable versions are available on other Unix-like operating systems.

### *Stacking Window Manager* | [Wiki](https://en.wikipedia.org/wiki/Stacking_window_manager)
A stacking window manager (also called floating window manager) is a window manager that draws all windows in a sepcific order, allowing them to overlap, using a technique called painter's algorithm. All window managers that allow the overlapping of windows but are not compositing window managers are considered stacking window managers, although it is possible that not all use exactly the same methods. Other window managers that are not considered stacking window managers are those that do not allow the overlapping of windows, which are called tiling window managers.

A stacking window manageres allow windows to overlap by drawing them one at a time. STacking, or repainting (in reference to painter's algorithm) referes to the rendering of each window as an image, painted directly over the desktop, and over any other windows that might already have been drawn, effectively erasing the areas that are covered. The process usually starts with the desktop, and proceeds by drawing each window and any child windows from back to front, until finally the foreground window is drawn.

The order in which windows are to be stacked is called their z-order.

### *Compositing Window Manager* | [Wiki](https://en.wikipedia.org/wiki/Compositing_window_manager)
A compositing window manager, or compositor, is a window manager that provides applications with an off-screen buffer for each window. The window manager composites the window buffers into an image representing the screen and writes the result into the display memory.

Compositing window managers may perform additional processing on buffered windows, applying 2D and 3D animated effects such as blending, fading, scaling, rotation, duplication, bending and contortion, shuffling, blurring, redirecting applications, and translating windows into one of a number of displays and virtual desktops. Computer graphics technology allows for visual effects to be rendered in real time such as drop shadows, live previews, and complex animation. Since the screen is double buffered, it does not flicker during updates.

The most commonly used compositing window managers include: Linux, BSD, Hurd and OpenSolaris - Compiz, KWin, Xfwm, Enlightenment, xcompmgr, picom and Mutter. Windows - the Desktop Window Manager. macOS - the Quartz Compositor.

### *Tiling Window Manager* | [Wiki](https://en.wikipedia.org/wiki/Tiling_window_manager)
A tiling window manager is a window manager with an organizztion of the screen into mutually non-overlapping frames, as opposed to the more popular approach of coordinate-based stacking of overlapping objects(windows) that tries to fully emulate the desktop metaphor.

### *Compositing* | [Wiki](https://en.wikipedia.org/wiki/Compositing)
Compositing is the process or technique of combining visual elements from separate sources into the single images, often to create the illusion that all those elements are parts of the same scene. Live-action shooting for compositing is variously called chroma key, blue screen, green screen and other names.

### *DWM, Desktop Window Manager* | [Wiki](https://en.wikipedia.org/wiki/Desktop_Window_Manager)
Desktop Window Manager(DWM, previsouly Desktop Compositing Engine, DCE) is the window manager in Windows Vista, Windows 7, Windows 8 and Windows 10 that enables the use of hardware accleration to render the graphical user interface of Windows. DWM is a compositing window manager that each program has a buffere that it writes data to; DWM then composites each program's buffer into a final image. The stacking window manager in Windows XP and earlier comprises a single display buffer to which all programs write.

### *X11, X Window System* | [Wiki](https://en.wikipedia.org/wiki/X_Window_System)
The X Window System (X11, or simply X) is a windowing system for bitmap displays, common on Unix-like operating systems. X provides the basic framework for a GUI environment: drawing and moving windows on the display device and interacting with a mouse and keyboard. X does note mandate the user interface - this is handled by individual programs. X originated as part of Project Athena at MIT in 1984. The X protocol has been at version 11 (hence X11) since September 1987. The X.Org Foundation leads the X project, with the current reference implementation, X.Org Server, available as free and open-source software under the MIT License and similar permissive licenses.

### *OpenBSD* | [Wiki](https://en.wikipedia.org/wiki/OpenBSD)
OpenBSD is a security-focused, free and open-source, Unix-like operating system based on the Berkeley Software Distribution(BSD). Theo de Raadt created OpenBSD in 1996 by forking NetBSD. OpenBSD project emphasizes portabiliy, standardization, correctness, proactive security and integrated cryptography.

### *MFC, Microsoft Foundation Class Library* | [Wiki](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library)
Microsoft Foundation Class Library(MFC) is a C++ object-oriented library for developing desktop applications for Windows. MFC was introduced by Microsoft in 1992 and quickly gained widespread use. While Microsoft has introduced alterantive application frameworks since the, MFC remains widely used.

### *Rendering* | [Wiki](https://en.wikipedia.org/wiki/Rendering_(computer_graphics))
Rendering or image synthesis is the process of generating a photorealistic or non-photorealistic image from a 2D or 3D model by means of a computer program. The resulting image is referred to as the render. Multiple models can be defined in a scene file containing objects in a strictly defined language or data structure. The scene file contains geometry, viewpoint, texture, lighting, and shading information describing the virtual scene. The data contained in the scene file is then passed to a rendering program to be processed and output to a digital image or raster graphics image file. The term rendering is analogous to the concept of an artist's impression of a scene. The term rendering is also used to describe the process of calculating effects in a video editing program to produce the final video output.

### *Compound Document* | [Wiki](https://en.wikipedia.org/wiki/Compound_document)
A compound document is a document that combines multiple document formats, either by reference, by inclusion, or both. Compound documents are often produced using word processing software, and may include text and non-text elements such as barcodes, spreadsheets, pictures, digital videos, digital audio, and other multimedia features. Compound document technologies are commonly utilized on top of a software componentry framework, but the idea of software componentry includes serveral other concepts apart from compound documents, and software components alone do not enable compound documents. Well-known technologies for compound documents include: Active X Documents, Bonobon by Ximian(primarily used by GNOME), Object linking and embedding(OLE) by Microsoft; see Compound File Binary Foramt, OpenDoc by IBM and Apple Computer(now defunct) and XML and XSL are encapsulation formats used for compound documents of all kinds. The first public implementation of compound documents was on the Xerox Star workstation, released in 1981.

### *Component-based Software Engineering* | [Wiki](https://en.wikipedia.org/wiki/Component-based_software_engineering)
Component-based software engineering (CBSE), also called components-based development (CBD), is a branch of software engineering that emphasizes the separation of concerns with respect to the wide-ranging functionality available throughout a given software system. It is a reuse-based approach to defining, implementing and composing loosely coupled independent components into systems. This practice aims to bring about an equally wide-ranging degree of benefits in both the short-term and the long-trem for the software itself and for organizations that sponsor such software.

### *Object Linking and Embedding* | [Wiki](https://en.wikipedia.org/wiki/Object_Linking_and_Embedding)
Object Linking and Embedding (OLE) is a proprietary technology developed by Microsoft that allows embedding and linking to documents and other objects. For developers, it brought OLE Control Extension (OCX), a way to develop and use custom user interface elements. On a technical level, an OLE object is any object that implements the IOleObject interface, possibly along with a wide range of other interfaces, depending on the object's needs.

Linked Object는 원본 파일 데이터에 대한 포인터이다. 원본 파일 데이터가 변경되면 변경 내용이 반영된다. Linked Object의 데이터는 원본 파일에 저장되므로 Linked Object를 편집해야 하는 경우 서버 application이 있어야한다. 원본 파일이 이동, 삭제된 경우에는 해당 파일과 Linked Object를 다시 만들어야 한다.

Embedded Object는 원본 파일의 데이터 사본이다. 원본 파일 데이터를 변경해도 Embedded Object에는 반영되지 않는다. Embedded Object의 데이터는 문서에 저장되므로 편집해야 할 경우 원본 파일에 액세스할 필요가 없다. 이 기능을 이용하면 개체에 대한 코드를 문서 안에 그대로 끼워 넣기 때문에 파일 크기가 커지는 단점이 있다.

### *Compound File Binary Format* | [Wiki](https://en.wikipedia.org/wiki/Compound_File_Binary_Format)
Compound File Binary Format (CFBF), also called Compound File, Compound Document format, or Composite Document File V2 (CDF), is a compound document file format for storing numerous files and streams within a single file on a disk. CFBF is developed by Microsoft and is an implementation of Microsoft COM Structured Storage. Microsoft has opened the format for use by others and it is now used in a variety of programs from Microsoft Word and Microsoft Access to Business Objects. It also forms the basis of the Advanced Authoring Format. CFBF is a container, with little restriction on what can be stored within it. CFBF file structure loosely resembles a FAT filesystem. The file is partitioned into Sectors which are chained together with a File Allocation Table(not to be mistaken with the file system of the same name) which contains chains of sectors related to each file, a Directory holds information for contained files with a Sector ID (SID) for the starting sector of a chain and so on.

### *Skia Graphics Library* | [Homepage](https://skia.org/)
Skia is an open source 2D graphics library which provides common APIs that work across a variety of hardware and software platforms. It serves as the graphics engine for Google Chrome and Chrome OS, Android, Flutter, Mozilla Firefox and Firefox OS, and many ohter products. Skia is sponsored and managed by Google, but is available for use by anyone under the BSD Free Software License. 

#### Reference
- Combo box, https://clack.tistory.com/335, 2020-08-26-Wed.
- Dropdown menu, https://kuzuro.blogspot.com/2018/08/htmlcss.html, 2020-08-26-Wed.
- Widget Wiki KR, https://ko.wikipedia.org/wiki/GUI_%EC%9C%84%EC%A0%AF, 2021-03-09-Tue.
- https://ko.wikipedia.org/wiki/%EC%B0%BD_(%EC%BB%B4%ED%93%A8%ED%8C%85), 2021-03-09-Tue.
- CWM Wiki, https://en.wikipedia.org/wiki/Cwm_(window_manager), 2021-03-26-Fri.
- Stacking Window Manager Wiki, https://en.wikipedia.org/wiki/Stacking_window_manager, 2021-03-26-Fri.
- Compositing Window Manager Wiki, https://en.wikipedia.org/wiki/Compositing_window_manager, 2021-03-26-Fri.
- Tiling Window Manager Wiki, https://en.wikipedia.org/wiki/Tiling_window_manager, 2021-03-26-Fri.
- Compositing Wiki, https://en.wikipedia.org/wiki/Compositing, 2021-03-26-Fri.
- Desktop Window Manager Wiki, https://en.wikipedia.org/wiki/Desktop_Window_Manager, 2021-03-26-Fri.
- X Window System Wiki, https://en.wikipedia.org/wiki/X_Window_System, 2021-03-26-Fri.
- OpenBSD Wiki, https://en.wikipedia.org/wiki/OpenBSD, 2021-03-26-Fri.
- MFC Wiki, https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library, 2021-03-26-Fri.
- Rendering Wiki, https://en.wikipedia.org/wiki/Rendering_(computer_graphics), 2021-03-26-Fri.
- Compound Document Wik, https://en.wikipedia.org/wiki/Compound_document, 2021-03-26-Fri.
- Compound-based Software Engineering Wiki, https://en.wikipedia.org/wiki/Component-based_software_engineering, 2021-03-26-Fri.
- Object Linking and Embedding Wiki, https://en.wikipedia.org/wiki/Object_Linking_and_Embedding, 2021-03-26-Fri.
- Compound File Binary Format Wiki, https://en.wikipedia.org/wiki/Compound_File_Binary_Format, 2021-03-26-Fri.
- Skia, https://skia.org/, 2021-03-26-Fri.
- OLE Blog KR, https://securityfactory.tistory.com/357, 2021-03-26-Fri.
- Widget Wiki, https://en.wikipedia.org/wiki/Widget, 2021-03-27-Sat.
- Graphical Widget Wiki, https://en.wikipedia.org/wiki/Graphical_widget, 2021-03-27-Sat.

# View

### Combo Box
#### Basic
선택항목이 숨어있지 않고 화면에 처음부터 노출되어 있다. 사용자가 텍스트를 입력할 수 있다.

#### Dropdown
선택항목이 숨어있어 화살표 버튼을 누르면 펼쳐져서 사용자가 선택할 수 있다. 텍스트를 입력할 수 있다.

#### Dropdown list
선택항목이 숨어있다 콤보박스를 선택하면 선택항목이 펼쳐져 선택할 수 있다. 텍스트를 입력할 수 없다. 선택항목 중에 한가지만 선택 가능하다.

## Widget
컴퓨터 프로그램에서 Widget(위젯) 또는 Control(컨트롤)은 사용자가 상호 작용하는 인터페이스 요소이다. 위젯은 위젯 스스로를 물리적인 대응물과 구별하기 위해 virtual 자격을 갖는다. 마우스 커서로 클릭되는 가상 버튼과 그의 대응물인 손가락으로 눌리는 물리적 버튼을 들 수 있다. Widget이라는 용어는 소형 장치나 요소를 뜻한다. 1980년애데 프로젝트 아테나가 최초로 GUI 요소를 widget이라고 부르기 시작했다.

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
Component-based software engineering(CBSE), also called components-based development(CBD), is a branch of software engineering that emphasizes the separation of concerns with respect to the wide-ranging functionality available throughout a given software system. It is a reuse-based approach to defining, implementing and composing loosely coupled independent components into systems. This practice aims to bring about an equally wide-ranging degree of benefits in both the short-term and the long-trem for the software itself and for organizations that sponsor such software.

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

# :art: [Graphics Library](https://en.wikipedia.org/wiki/Graphics_library)

A graphics library is a program library designed to aid in rendering computer graphics to a monitor. This typically involves providing optimized versions of functions that handle common rendering tasks. This can be done purely in software and running on the CPU, common in embedded systems, or being hardware accelerated by a GPU, more common in PCs. By employing these functions, a program can assemble an image to be output to a monitor. This relieves the programmer of the task of creating and optimizing these functions, and allows them to focus on building the graphics program. Graphics libraries are mainly used in video games and simulations.

### [GTK](https://www.gtk.org/) | [Wiki](https://en.wikipedia.org/wiki/GTK)

GTK (formerly GTK+) is a free and open-source cross-platform widget toolkit for creating graphical user interfaces (GUIs). It is licensed under the terms of the GNU Lesser General Public License, allowing both free and proprietary software to use it. It is one of the most popular toolkits for the Wayland and X11 windowing systems.

리눅스에서 GUI를 다루기 위한 라이브러리 중 하나임. Ubuntu의 Gnome Desktop Environment가 GTK로 만들어짐. 이외에도 다양한 애플리케이션, 프로그램들이 GTK로 만들어짐. C로 구현된 객체지향 GUI 라이브러리임. 소스 코드 공개 의무가 없는 자유 라이센스임. QT와의 차이점으로는 C를 지원하고 한글 버그가 적음.

### [Mesa 3D](https://www.mesa3d.org/) | [Wiki](https://en.wikipedia.org/wiki/Mesa_(computer_graphics))

Mesa, also called Mesa3D and The Mesa 3D Graphics Library, is an open source implementation of OpenGL, Vulkan, and other graphics API specifications. Mesa translates these specifications to vendor-specific graphics hardware drivers.

### [Vulkan](https://www.vulkan.org/) | [Wiki](https://en.wikipedia.org/wiki/Vulkan)

Vulkan is a low-overhead, cross-platform API, open standard for 3D graphics and computing.

### [Qt](https://www.qt.io/) | [Wiki](https://en.wikipedia.org/wiki/Qt_(software))

Qt (pronounced "cute") is a cross-platform software for creating graphical user interfaces as well as cross-platform applications that run on various software and hardware platforms such as Linux, Windows, macOS, Android or embedded systems with little or no change in the underlying codebase while still being a native application with native capabilities and speed.

C++를 기본으로 하는 GUI 제작 크로스 플랫폼 프레임워크임. GUI 제작, 웹 앱 제작이 편리함. 오픈소스 라이센스와 상업 라이센스가 있는데, 상업 라이센스를 유료로 사용하면 소스 코드 공개하지 않아도 됨. 구글 어스, 스카이프, KED(리눅스 운영체제), Autodesk의 Maya(Animation)이 있음.

### [OpenGL](https://www.opengl.org/) | [Wiki](https://en.wikipedia.org/wiki/OpenGL)

OpenGL (Open Graphics Library) is a cross-language, cross-platform application programming interface (API) for rendering 2D and 3D vector graphics. The API is typically used to interact with a graphics processing unit (GPU), to achieve hardware-accelerated rendering.

Silicon Graphics, Inc. (SGI) began developing OpenGL in 1991 and released it on June 30, 1992; applications use it extensively in the fields of computer-aided design (CAD), virtual reality, scientific visualization, information visualization, flight simulation, and video games. Since 2006, OpenGL has been managed by the non-profit technology consortium Khronos Group.

### [OpenGL ES](https://www.khronos.org/opengles/) | [Wiki](https://en.wikipedia.org/wiki/OpenGL_ES)

OpenGL for Embedded Systems (OpenGL ES or GLES) is a subset of the OpenGL computer graphics rendering application programming interface (API) for rendering 2D and 3D computer graphics such as those used by video games, typically hardware-accelerated using a graphics processing unit (GPU). It is designed for embedded systems like smartphones, tablet computers, video game consoles and PDAs. OpenGL ES is the "most widely deployed 3D graphics API in history". The API is cross-language and multi-platform. 

### Tizen Graphics and UI

EFL(Enlightenment Foundation Libraries, 그래픽 컴포넌트 라이브러리들)를 포함함, Evas cancas API, 기본 위젯 라이브러리가 있음. window management system(x11 for Tizen 2.x / Wayland for Tizen 3.0)을 포함함. Webkit-based 그래픽이 제공됨. Tizen의 자체 HTML5 canvas WebKitEFL 구현임, WebGL, jQuery Mobile 지원함.

###  webOS Graphics and Input

자체 구현한 Luna Sufrace Manager(LSM)을 사용함, Wayland와 호환됨. 

LSM은 1. QPA(Qt Platform Abstarction, Qt 애플리케이션을 위한 그래픽/인풋 하드웨어 추상화 계층), 2. QtWayland 컴포지터, 그리고 3. System UI in QML으로 구성됨. 

다른 webOS 구성요소들과 Luna Bus, LS2를 통해 통신함.

### Wayland

리눅스 데스크탑 환경을 구현하기 위한 프로토콜임.

리눅스 데스크탑 환경은 크게 컴포지터와 쉘로 구분됨, UI를 쉘이 그리고 애플리케이션 윈도우가 겹쳐졌을 때 처리를 컴포지터가 함, Wayland는 컴포지터와 쉘의 구현을 돕는 API와 쉘이 애플리케이션과 통신할 수 있도록 프로토콜을 제공함.

Wayland 이전에는 x11이 컴포지터(x server) 역할을 했고, 이 위에서 Gnome, KDE 같은 서드파티 쉘이 동작함. x11 단일 컴포지터가 모든 쉘을 관리하는 모델은 리눅스 GUI 환경의 변화를 따라오긴 너무 거대하고 유연하지 않음.

### Android Graphics

스크린을 3가지 방법(Canvas, OpenGL ES, Vulkan(벌칸))으로 그릴 수 있음.

### Blink

블링크는 렌더링 엔진임. 블링크는 Chromium에서 사용함.

### Browser Engine

브라우저 엔진은 layout 엔진 또는 렌더링 엔진이라고 함. HTML 문서를 변환함. 웹 페이지의 다른 리소스들을 사용자 화면에 보여줌.

### Web Browser Engines

WebKit은 Apple에서 만듦.

Blink는 Google에서 만듦. Chrome과 Chromium 기반 브라우저들(Edge, Samsung Internet, Opera)에서 사용함. 즉, Linux 기반의 Mobile OS인 Android, Tizen, webOS 모두 Chrome/Chromium 기반 브라우저를 사용하기 때문에 Blink를 사용함.

Gecko는 Mozilla에서 만듦.

EdgeHTML은 Microsoft에서 만들고 옛날 Edge에서 사용함.

---

### Reference
- Graphics Library Wiki, https://en.wikipedia.org/wiki/Graphics_library, 2023-05-12-Fri.
- GTK, https://www.gtk.org/, 2023-05-12-Fri.
- GTK Wiki, https://en.wikipedia.org/wiki/GTK, 2023-05-12-Fri.
- Mesa 3D, https://www.mesa3d.org/, 2023-05-12-Fri.
- Mesa 3D Wiki, https://en.wikipedia.org/wiki/Mesa_(computer_graphics), 2023-05-12-Fri.
- Vulkan, https://www.vulkan.org/, 2023-05-12-Fri.
- Vulkan Wiki, https://en.wikipedia.org/wiki/Vulkan, 2023-05-12-Fri.
- Qt, https://www.qt.io/, 2023-05-12-Fri.
- Qt Wiki, https://en.wikipedia.org/wiki/Qt_(software), 2023-05-12-Fri.
- OpenGL, https://www.opengl.org/, 2023-05-12-Fri.
- OpenGL Wiki, https://en.wikipedia.org/wiki/OpenGL, 2023-05-12-Fri.
- OpenGL ES, https://www.khronos.org/opengles/, 203-05-12-Fri.
- OpenGL ES Wiki, https://en.wikipedia.org/wiki/OpenGL_ES, 2023-05-12-Fri.
- GTK KR, https://www.kernelpanic.kr/25, 2023-05-11-Thu.
- QT Blog KR, https://gamestory2.tistory.com/12, 2023-05-11-Thu.
- Wayland KR, https://www.kernelpanic.kr/5, 2023-05-11-Thu.
- Tizen Architecture, https://docs.tizen.org/platform/porting/overview/, 2023-05-11-Thu.
- webOS Graphics and Input, https://www.webosose.org/docs/guides/core-topics/graphics-input/graphics-input-overview/, 2023-05-11-Thu.
- Android Graphics, https://source.android.com/docs/core/graphics, 2023-05-11-Thu.
- Surface and SurfaceHolder, https://source.android.com/docs/core/graphics/arch-sh, 2023-05-11-Thu.
- EGLSurfaces and OpenGL ES, https://source.android.com/docs/core/graphics/arch-egl-opengl, 2023-05-11-Thu.
- Vulkan, https://source.android.com/docs/core/graphics/arch-vulkan, 2023-05-11-Thu.
- Wayland/Weston, https://prographics.tistory.com/2, 2023-05-12-Fri.
- Blink (Redering Engine) The Chromium Projects, https://www.chromium.org/blink/, 2023-05-12-Fri.
- Comparison of browser engines Wiki, https://en.wikipedia.org/wiki/Comparison_of_browser_engines, 2023-05-12-Fri.
- Browser Engine Wiki, https://en.wikipedia.org/wiki/Browser_engine, 2023-05-12-Fri.
- List of display Server Wiki, https://en.wikipedia.org/wiki/List_of_display_servers, 2023-05-12-Fri.
- Windowing System Wiki, https://en.wikipedia.org/wiki/Windowing_system, 2023-05-12-Fri.
- List of Display Servers Wiki, https://en.wikipedia.org/wiki/List_of_display_servers, 2023-05-12-Fri.
- X.Org, https://www.x.org/wiki/, 2023-05-12-Fri.
- X Window System Wiki, https://en.wikipedia.org/wiki/X_Window_System, 2023-05-12-Fri.
- Wayland, https://wayland.freedesktop.org/, 2023-05-12-Fri.

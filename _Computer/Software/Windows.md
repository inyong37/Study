# *Windows* | [Windows 10 Homepage](https://www.microsoft.com/en-us/windows/) | [Wiki](https://en.wikipedia.org/wiki/Microsoft_Windows)
```This page is from the 'System' page.```

Microsoft Windows, commonly referred to as Windows, is a group of several proprietary graphical operating system families, all of which are developed and marketed by Microsoft. Each family caters to a certain sector of the computing industry. Active Microsoft Windows families include Windows NT and Windows IoT; these may encompass subfamilies, e.g. Windows Server or Windows Embedded Compact (Windows CE). Defunct Microsoft Windows families include Windows 9x, Windows Mobile and Windows Phone.

Microsoft introduced an operating environment named Windows on November 20, 1985, as a graphical operating system shell for MS-DOS in response to the growing interest in graphical user interfaces (GUIs). Microsoft Windows came to dominate the world's personal computer (PC) market with over 90% market share, overtaking Mac OS, which had been introduced in 1984. Apple came to see Windows as an unfair encroachment on their innovation in GUI development as implemented on products such as the Lisa and Macintosh (eventually settled in court in Microsoft's favor in 1993). On PCs, Windows is still the most popular operating system. However, in 2014, Microsoft admitted losing the majority of the overall operating system market to Android, because of the massive growth in sales of Android smartphones. In 2014, the number of Windows devices sold was less than 25% that of Android devices sold. This comparison, however, may not be fully relevant, as the two operating systems traditionally target different platforms. Still, numbers for server use of Windows (that are comparable to competitors) show one third market share, similar to that for end user use.

As of February 2020, the most recent version of Windows for PCs, tablets and embedded devices is Windows 10, version 2004. The most recent version for server computers is Windows Server, version 2004. A specialized version of Windows also runs on the Xbox One video game console.

### *Download*
[Windows 10 Download](https://www.microsoft.com/en-us/software-download/windows10)

[Windows 8.1 Download](https://www.microsoft.com/en-us/software-download/windows8ISO)

[Windows 7 Download](https://www.microsoft.com/en-us/software-download/windows7)

## *MFC (Microsoft Foundation Class Library)* | [Wiki](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library)
Microsoft Foundation Class Library(MFC) is a C++ object-oriented library for developing desktop applications for Windows. MFC was introduced by Microsoft in 1992 and quickly gained widespread use. While Microsoft has introduced alterantive application frameworks since the, MFC remains widely used.

## *Windows API* | [Wiki](https://en.wikipedia.org/wiki/Windows_API)
The Windows API (informally WinAPI) is Microsoft's core set of application programming interfaces (APIs) available in the Microsoft Windows operating systems. The name Windows API collectively refers to several different platform implementations that are often referred to by their own names (for example, Win32 API). Almost all Windows programs interact with the Windows API. On the Windows NT line of operating systems, a small number (such as programs started early in the Windows startup process) use the Native API. There are Win16, Win32, Win32s, Win64, and WinCE versions.

## *DWM (Desktop Window Manager)* | [Wiki](https://en.wikipedia.org/wiki/Desktop_Window_Manager)
Desktop Window Manager(DWM, previsouly Desktop Compositing Engine, DCE) is the window manager in Windows Vista, Windows 7, Windows 8 and Windows 10 that enables the use of hardware accleration to render the graphical user interface of Windows. DWM is a compositing window manager that each program has a buffere that it writes data to; DWM then composites each program's buffer into a final image. The stacking window manager in Windows XP and earlier comprises a single display buffer to which all programs write.

## *COM (Component Object Model)* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/com/the-com-library) | [Wiki](https://en.wikipedia.org/wiki/Component_Object_Model)

## *Microsoft Developer Network (MSDN)* | [Homepage](https://social.msdn.microsoft.com/forums/en-us/home) | [Wiki](https://en.wikipedia.org/wiki/Microsoft_Developer_Network) | [Docs](https://docs.microsoft.com/en-us/) | [GitHub](https://github.com/MicrosoftDocs)
Microsoft Developer Network (MSDN) was the division of Microsoft responsible for managing the firm's relationship with developers and testers, such as hardware developers interested in the operating system (OS), and software developers developing on the various OS platforms or using the API or scripting languages of Microsoft's applications. The relationship management is situated in assorted media: web sites, newsletters, developer conferences, trade media, blogs and DVD distribution.

From January 2020, the website has been fully integrated with Microsoft Docs.

## *.NET* | [MS Docs](https://docs.microsoft.com/en-us/dotnet/) | [What is .NET?](https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet?&WT.mc_id=Educationaldotnet-c9-scottha)
.NET is a free, cross-platform, open source developer platform for building many different types of applications. It makes developer can use multiple languages; C#, F#, or Visual Basic, editors, and libraries to build for web, mobile, desktop, games and IoT.

### *.NET Languages*
- C# is a simple, modern, object-oriented, and type-safe programming language.
- F# is a cross-platform, open-source, functional programming language for .NET. It also includes object-oriented and imperative programming.
- Visual Basic is an approachable language with a simple syntax for building type-safe, object-oriented apps.

### *.NET Cross Platform*
The code will run natively on any compatible OS. Different .Net implementations handle the heavy lifting for developers.
- .NET Core is a cross-platform .NET implementation for websites, servers, and consol apps on Windows, Linux, and macOS.
- .NET Framework supports websites, services, desktop apps, and more on Windows.
- Xamarin/Mono is a .NET implementaion for running apps on all the major mobile operating systems.

## *.NET Framework* | [MS Docs](https://docs.microsoft.com/en-us/dotnet/framework/)
.NET Framework is a technology that supports building and running Windows apps and web services.

## *Interprocess Communications (IPC)* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/ipc/interprocess-communications)
The Windows operating system provides mechanism for facilitating communications and data sharing between applications. Typically, applications can use IPC categorized as clients or servers. A client is an application or a process that requests a servce from some other application or process. A server is an application or a process that responds to a client request. Many applications act as both a client and a server, depending on the situation. 

The answers to below questions determine whether an application cna benefit by using one or more IPC mechanisms.
- Should the applications be able to communicate with other applications running on other computers on a network, or is it sufficient for the applications to communicate only with applications on the local computer?
- Should the application be able to communicate with applications running on other computers that may be running under different operating systems (sych as 16-bit Windows or UNIX)?
- Should the user of the application have to choose the other applications with which the application communicates, or can the application implicitly find its cooperating partners?
- Should the application communicate with many different applications in a general way, such as allowing cut-and-paste operations with any other application, or should its communications requirements be limited to a restricted set of interactions with specific other application?
- Is performance a critical aspect of the application? All IPC mechanisms include some amount of overhead.
- Should the application be a GUI appliction or a consol application? Some IPC mechanisms require a GUI application.

### *IPC: Clipboard*
The clipboard acts as a depository for data sharing among applications.

**All applications should support the clipboard for those data formats that they understand.**

### *IPC: COM (Component Object Model)*
Applications that use OLE manage compound documents-that is, documents made up for data from a variety of different applications. OLE provides services that make it easy for applications to call on other applications for data editing.

**OLE supports compound documents and enables an application to include embedded or linked data that, when chosen, automatically starts another application for data editing.**

### *IPC: Data Copy* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/dataxchg/data-copy)
Data copy enables an application to send information to another application using the `WM_COPYDATA` message. This method requires cooperation between the sending application and the receiving application. 

**Data copy can be used to quickly send information to another application using Windows messaging.**

### *IPC: DDE (Dynamic Data Exchange)*
DDE is a protocol that enables applications to exchange data in a variety of formats. 

**DDE is not as efficient as newer technologies. However, you can still use DDE if other IPC mechanisms are not suitable or if you must interface with an existing application that only supports DDE.**

### *IPC: File Mapping* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/memory/file-mapping)
File mapping is the association of a file's contents with a portion of the virtual address space of a process. The system creates a file mapping object (also known as a section object) to maintain this association. A file view is the portion of virtual address space that a process uses to access the file's contents. File mapping allows the process to use both random input and output (I/O) and sequential I/O. It also allows the process to work efficiently with a large data file, such as a database, without having to map the whole file into memory. Multiple processes can also use memory-mapped files to share data.

Processes read from and write to the file view using pointers, just as they would with dynamically allocated memory. The use of file mapping imporves efficiency because the file resides on disk, but the file view resides in memory. Processes can also manipulate the file view with the VirtualProtect function.

The file on disk can be any file that you want to map into memory, or it can be the system page file.

File mapping enables a process to treat the contents of a file as if they were a block of memory in the process's address space. The process can use simple pointer operations to examine and modify the contents of the file.

**File mapping is an efficient way for two or more processes on the same computer to share data, but you must provide synchronization between the processes.**

### *Creating Named Shared Memory* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/memory/creating-named-shared-memory)
To share data, multiple processes can use memory-mapped files that the system paging file stores.

### *IPC: Mailslot*
Mailslots provide on-way communication. Any process that creates a mailslot is a mailslot server. Other processes, called mailslot clients, send messages to the mailslot erver by writing a message to its mailslot. Incoming messages are always appended to the mailslot. The mailslot saves the messages until the mailslot server has read them. A process can be both a mailslot server and a mailslot client, so two-way communication os possible using multiple mailslots.

**Mailslots offer an easy way for applications to send and receive short messages. They also proved the ability to broadcast messages across all computers in a network domain.**

### *IPC: Pipe* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/ipc/pipes) | [Anonymous Pipe Operations](https://docs.microsoft.com/en-us/windows/win32/ipc/anonymous-pipe-operations)
A pipe is a section of shared memory that processes use for communication. The process that creates a pipe is the pipe server. A process that connects to a pipe is a pipe client. One process writes information to the pipe, then the other process reads the information from the pipe.

There are two types of pipes for two-way communication: anonymous pipes and named pipes. 

Anonymous pipes require less overhead than named pipes, but offer limited services. An anonymous pipe is an unnamed, one-way pipe that typically transfers data between a parent process and a child process. Anonymous pipes are always local; they cannot be used for communication over a network.

Anonymous pipes eanable related processes to transfer information to each other. Typically, an anonymous pipe is used for redirecting the standard input or output of a child process so that it can exchange data with its parent process. To exchange data in both directions (duplex operation), you must create two anonymous pipes. The parent process writes data to one pipe using its write handle, while the cihld process reads the data from that pipe using its read handle. Similarly, the child process writes data to the other pipe and the parent process reads from it. Anonymous pipes cannot be used over a network, nor can they be used between unrelated processes.

Named pipes are used to transfer data between processes that are not related processes and between processes on different computers. Typically, a named-pipe server process creates a named pipe with a well-known name or a name that is to be communicated to its clients. A named-pipe client process that knows the name of the pipe can open its other end, subject to access restrictions specified by named-pipe server process. After both the server and client have connected to the pipe, they can exchange data by performing read and write operations on the pipe.

**Anonymous pipes provides an efficient way to redirect standard input or output to child processes on the same computer. Named pipes provide a simple programming interface for transferring data between two processes, whether they reside on the same computer or over a network.**

### *IPC: RPC* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/rpc/microsoft-rpc-components)
**RPC enables applications to call functions remotely. Therefore, RPC makes IPC as easy as calling a function. RPC operates between processes on a single computer or on different computers on a network.**

The RPC provided by Windows is compliant with the Open Software Foundation (OSF) Distributed Computing Environment (DCE). This means that applications that use RPC are able to communicate with applications running with other operating systems that support DCE. RPC automatically supports data conversion to account for different hardware architectures and for byte-ordering between dissimilar environment.

**RPC is a function-level interface, with support for automatic data conversion and for communications with other operating systems. Using RPC, you can create high-performance, tightly coupled distributed applications.**

### *IPC: Windows Sockets* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-start-page-2)
Windows Sockets 2 (Winsock) enables programmers to create advanced Internet, intranet, and other network-capable applications to transmit application data across the wire, independent of the network protocol being used.

Windows Sockets is a protocol-independent interface. It takes advantage of the communication capabilities of the underlying protocols. In Windows Sockets 2, a socket handle can optionally be used as a file handle with the standard file I/O functions.

**Windows Sockets are based on the sockets first popularized by Berkeley Software Distribution (BSD). An application that uses Windows Sockets can communicate with other socket implementation on other types of systems. However, not all transport service providers support all available options.**

**Windows Sockets is a protocol-independent interface capable of supporting current and emerging networking capabilities.**

## *Signal* | [MS Docs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/signal?view=msvc-160)
Sets interrupt signal handling

- sig value
  - SIGABRT: Abnormal termination
  - SIGFPE: Floating-point error
  - SIGILL: Illegal instruction
  - SIGINT: `Control` + `c` signal
  - SIGSEGV: Illegal storage access
  - SIGTERM: Termination request

### *Data Types* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/winprog/windows-data-types)
- LPARAM: A message parameter. This type is declared in WinDef.h as `typedef LONG_PTR LPARAM;`
- LRESULT: Signed result of message processing. This type is declared in WinDef.h as `typedef LONG_PTR LRESULT;`
- WPARAM: A message parameter. This type is declared in WinDef.h as `typedef UINT_PTR WPARAM;`
- DWORD: A 32-bit unsigned integer (range: 0 throught 4294967295 decimal) `typedef unsigned long DWORD, *PDWORD, *LPDWORD;`

### *What do the letters W and L stand for in WPARAM and LPARAM?* | [MS](https://devblogs.microsoft.com/oldnewthing/20031125-00/?p=41713)
When Windows was 16-bit, each message could carry with it two pieces of data, called WPARAM and LPARAM. The WPARAM was a 16-bit value ("word"), so it was called W. The LPARAM was a 32-bit value ("long"), so it was called L. W parameter is used to pass things like handles and integers, and L parameter is used to pass pointers.

When Windows was converted to 32-bit, the WPARAM grew to a 32-bit value as well. So even thought the "W" stands for "word", it isn't a word any more. And in 64-bit Windows, both parameters are 64-bit values. When you look at the design of window messages, you will see that if the message takes a pointer, the pointer is usually passed in the LPARAM, whereas if the message takes a handle or an integer, then it is passed in the WPARAM. And if a message takes both, the integer goes in the WPARAM and the pointer goes in the LPARAM.

### *What happens to WPARAM, LPARAM, and LRESULT when they travel between 32-bit and 64-bit windows?* | [MS](https://devblogs.microsoft.com/oldnewthing/20110629-00/?p=10303)
Truncation. When 64-bit process sends a message to a 32-bit window, the 64-bit WPARAM and LPARAM values are truncated to 32 bits. Similary, when a 64-bit window returns an LRESULT back to a 32-bit sender, the value is truncated.

The WPARAM is zero-extended, while LPARAM and LRESULT are sign-extended. WORD is an unsigned type (therefore zero-extended) and LONG is a signed type (therefore sign-extended). UNIT_PTR is an unsigned type (therefore zero-extended) and LONG_PTR is a signed type (therefore sign-extended).

### *Data Type Ranges* | [MS Docs](https://docs.microsoft.com/en-us/cpp/cpp/data-type-ranges?view=msvc-160&viewFallbackFrom=vs-2019)

### *Built-in Types (C++)* | [MS Docs](https://docs.microsoft.com/en-us/cpp/cpp/fundamental-types-cpp?view=msvc-160)

### *Keywords (C++)* | [MS Docs](https://docs.microsoft.com/en-us/cpp/cpp/keywords-cpp?view=msvc-160)

### *Windows Coding Conventions* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/windows-coding-conventions)

### *Working with Strings* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/working-with-strings)

### *What Is a Window?* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/what-is-a-window-)
Windows are central to Windows. They are so important that they named the operating system after them. This type of window is called an application window or main window. It typically has a frame with a title bar, Minimize and Maximize buttons, and other standard UI elements. The frame is called the non-client area of the window, so called because the operating system manages that portion of the window. The area within the frame is the client area. This is the part of the window that programmer manages.

UI controls, such as buttons and edit boxes are themselves windows. The major difference between a UI control and an application window is that a control does not exist by itsef. Instead, the control is positioned relative to the application window. When user drags the application window, the control moves with it, as user would expect. Also, the control and the application window can communicate with each other. For example, the application window receives click notifiations from a button.

Therefore, when thinking window, do not simply think application window. Instead, think of a window as a programming construct that: Occupies a certain portion of the screen. May or may not be visible at a given moment. Knows how to draw itself. Responds to events from the user or the operating system.

In the case of a UI control, the control window is said to be the cihld of the application window. The application window is the parent of the control window. The parent window provides the coordinate system used for positioning a child window. Having a parent window affects aspects of a window's appearance; for example, a child window is clipped so that no part of the child window can appear outside the borders of its parent window.

Another relationship is the relation between an application window and a model dialog window. When an application display a modal dialog, the application window is the owner window, and the dialog is an owned window. An owned window always appears in front if its owner window. It is hidden when the owner is minimized, and is destroyed at the same time as the owner.

Windows are objects-they have both code and data-but they are not C++ classes. Instead, a program references a window by using a value called a handle. A handle is an opaque type. Essentially, it is just a nimber that the operating system uses to identify an object. You can picture Windows as having a big table of all the windows that have been created. It uses this table to look up windows by their handles. (Whether that's exactly how it works internally is not important.) The data type for window handles is HWND, which is usually pronounced "aitch-wind"." Window handles are returned by the functions that create windows: CreateWindow and CreateWindowEX.

To perform an operation on a window, you will typically call some function that takes an HWND value as a parameter. Keep in mind that handles are not pointers. If hwnd is a variable that contains a handle, attempting to dereference the handle by writing *hwnd is an error.

Coordinates are measured in device-independent pixles, We'll have more to say about the device indepenedent part of device-independent pixels when we discuss graphics. Depending on your task, you might measure coordinates relative to the screen, relative to a window (including the frame), or relative to the client area of a window. For example, you would position a window on the screen using coordinates, but you would draw inside a window using client coordinates. In each case, the origin (0, 0) is always the top-left corner of the region.

### *WinMain: The Application Entry Point* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/winmain--the-application-entry-point)
Every Windows pogram includes an entry-point function that is named either WinMain or wWinMain
- `int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow);`
- `INT WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR lpCmdLine, INT nCmdShow) {return 0;}`

`hInstance` is something called a "handle to an instance" or "handle to a module". The operating system uses this value to identify the executable (EXE) when it is loaded in memory. The instance handle is needed for certain Windows functions-for exmplae, to load icons or bitmaps. `hPrevInstance` has no meaning. It was used in 16-bit Windows, but is now always zero. `pCmdLine` contains the command-line arguments as a Unicode string. `nCmdShow` is a flag that says whether the main application window will be minimized, maximized, or shown normally. The function returns an int value. The return value is not used by the oeprating system, but you can use the reutnr value to convey a status code to some other program that you write. `WINAPI` is the calling convention. A calling convention defines how a function receives parameters from the caller. For example, it defines the order that parameters appear on the stack. Just make sure to declare your wWinMain function as shown.

The WinMain function is identical to wWinMain, except the command-line arguments are passed as an ANSI string. The Unicode version is perferred. You can use the ANSI WinMain function even if you compile your program as Unicode. To get a Unicode copy of the command-line arguments in a single string. If you want the arguments as an argv-style array, pass this string to CommandLineToArgvW.

How does the compiler know to invoke wWinMain instead of the standard main function? What actually happens is that the Microsoft C runtime library (CRT) provides an implementation of main that calls either WinMain or wWinMain. The CRT does some additional work inside main. For example, any static initializers are called before wWinMain. Althought you can tell the linker to use a different entry-point function, use the default if you link to the CRT. Otherwise, the CRT initialization code will be skipped, with unpredictable results. (For example, global objects will not be initialized correctly.)

### *WINAPI vs. APIENTRY*
```C++
// <windef.h>
...
#define WINAPI      CDECL
#define WINAPIV     CDECL
#define APIENTRY    WINAPI
...
#define WINAPI __stdcall
#define WINAPIV __cdecl
#define APIENTRY WINAPI
#define APIPRIVATE __stdcall
...
#define WINAPI
#define WINAPIV
#define APIENTRY    WINAPI
...
```

### *Walkthrought: Create a tranditional Windows Desktop application (C++)* | [MS Docs](https://docs.microsoft.com/en-us/cpp/windows/walkthrough-creating-windows-desktop-applications-cpp?view=msvc-160&viewFallbackFrom=vs-2019)

### *Overview* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/your-first-windows-program)

### *Creating a Window* | [MS DOcs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [WNDCLASSA](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-wndclassa)
- [CreateWindowA](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowa)

### *Window Messages* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/window-messages)
A GUI application must respond to events from the user and from the oeprating system. Events from the user include all the ways that someone can interact with your program: mouse clicks, key strokes, touch-screen gestures, and so on. Events from the operating system include anything "outside" of the program that can affect how the porgram behaves. For example, the user might plug in a new hardware device, or Windows might enter a lower-power state (sleep or hibernate). These events can occur at any time while the program is running, in almost any order. Windows uses a meesage-passing model. The operating system communuicates with your application window by passing messages to it. A message is simply a numeric code that designates a particular event. For example, if the user presses the left mouse button, the window receives a message that has the following message code. To pass a message to a window, the operating system calls the window procedure registered for that window.

An application will receive thousands of messages while it runs. Additionally, an application can have several windows, each with its own window procedure. The application needs a loop to retrieve the messages and dispatch them to the correct windows. For each thread that creates a window, the operating system creates a queue for window messages. This queue holds messages for all the windows that are created on that thread. The queue holds messages for all the windows that are created on that thread. The queue itself is hidden from your program. You cannot manipulate the queue directly. However, you call pull a message from the queue by calling the GetMessage function. `MSG msg; GetMessage(&msg, NULL, 0, 0);` This function removes the first message from the head of the queue. If the queue is empty, the function blocks until another message is queued. The fact that GetMessage blocks will not make you program unresponsive. If there are no messages, there is nothing for the program to do. If you have to perform background processing, you can create additional threads that continue to run while GetMessage waits for another message.

The first parameter of GetMessage is the address of a MSG structure. If the function succeeds, it fills in the MSG structure with information about the message. This includes the target window and the message code. The other three parameters let you filter which messages you get from the queue. In almost all cases, you will set these parameters to zero.

Althought the MSG structure contains information about the message, you will almost never examine this sturcture directly. Instead, you will pass it directly to two other functions. `TranslateMessage(&msg); DispatchMessage(&msg);` The TranslateMessage function is related to keyboard input. It translates keystrokes (key down, key up) into characters. You do not really have to know how this function works; just remember to call it before DispatchMessage. The DispatchMessage function tells the operating system to call the window procedure of the window that is the target of the message. In other words, the operating system looks up the window handle in its table of windows, finds the function pointer associated with the window, and invokes the function.

When the window procedure returns, it returns back to Dispatch Message. This returns to the message loop for the next message. As long as your program is running, messages will continue to arrive on the queue. Therefore, you must have a loop that continually pulls messages from the queue and dispatches them. Normally, GetMessage returns a nonzero value. When you want to exit the application and break out of the message loop, call the PostQuitMessage function `PostQuitMessage(0);`. The PostQuitMessage function puts a WM_QUIT message on the message queue. WM_QUIT is a special message: it causes GetMessage to return zero, signaling the end of the message loop.

### *Posted Messages vs. Sent Meesages*
Sometimes, the operating system will call a window procedure directly, bypassing the queue. The terminology for this distinction can be confusing: Posting a message means the message goes on the message queue, and is dispatched through the message loop (GetMessage and DispatchMessage). Sending a message means the message skips the queue, and the operating system calls the window procedure directly. The window procedure handles all messages. However, some messages bypass the queue and go directly to your window procedure. However, it can make a difference if your application communicates between windows.

### *Writing the Window Procedure* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/writing-the-window-procedure)
The DispatchMessage function calls the window procedure of the window that is the target of the message. `LRESULT CALLBACK WindowProc(HWND hwnd, UNIT uMSG, WPARAM wParam, LPARAM lParam);` hwnd is a handle to the window. uMsg is the message code; for example, the WM_SIZE message indicates the window was resized. wParam and lParam contain additional data that pertains to the message. The exact meaning depends on the message code. LRESULT is an integer value that your program returns to Windows. It contains your program's respones to a particular message. The meaning of this value depends on the message code. CALLBACK is the calling convention for the function.

A typical window procedure is simply a large switch statement that switches on the message code. Add cases for each message that you want to handle. Additional data for the message is contained in the lParam and wParam parameters. Both parameters are integer values the size of a pointer width (32 bits or 64 bits). The meaning of each depends on the message code (uMSG). For each message, you will need to look up the message code on MSDN and cast the parameters to the correct data type. Usually the data is either a numeric value or a pointer to a structure. Some messages do not have any data. One way to make your code more modular is to put the logic for handling each message in a seperate function. In the window procedure, cast the wParam and lParam parameters to the correct data type, and pass those values to the function. DefWindowProc function performs the default action for the message, which varies by message type. `return DefWindowProc(hwnd, uMsg, wParam, lParam);`

### *Avoding Bottlenecks in You Window Procedure*
While your window procedure executes, it blocks any other messgaes for windows created on the same thread. Therefore, avoid lengthy processing inside your window procedure. For example, suppose your program opens a TCP connection and waits indefinitely for the server to respond. If you do that inside the window procedure, your UI will not respond until the request completes. During that time, the window cannot process mouse or keyboard input, repaint itself, or even close. Instead, you should move the work to another thread, using one of the multitasking facilities that are built into Windows: Create a new thread, use a thread pool, use asynchronous I/O calls, use asynchronous procedure calls.

### *Painting the Window* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/painting-the-window)

### *Closing the Window* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/closing-the-window)

### *Managin Application State* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/managing-application-state-)

## *Folder*

### *Program Files*
Program Files 폴더에는 64-bit 프로그램들이 설치되고 Program Files (x86) 폴더에는 32-bit 프로그램들이 나눠서 설치된다. 옛날 컴퓨터는 Intel 의 8086 칩을 사용했는데 처음에는 16-bit 였고 그 이후 32-bit 가 되었다. 따라서 16-bit와 32-bit는 x86 이라 불리고 64-bit 는 x64 라 불린다. (지금 대부분의 컴퓨터는 16-bit 는 지원하지 않는다.) 현재 컴퓨터는 다양한 칩을 사용하는데 대부분 64-bit 를 지원한다. 32-bit 로 만들어진 응용 프로그램들은 'WOW64 (Windows on Windows 64-bit)' 를 통해 64-bit 에서도 실행이 가능하다. 따라서 Windows 에서는 32-bit 프로그램과 64-bit 프로그램을 섞이지 않고 나눠서 저장하고자 했다. 그래서 'C:/' 에는 'Program Files' 와 'Program Files (x86)' 2개의 폴더에 각각 나눠서 저장하게 설계되었다.

## *File*

### *Solution (.sln) File* | [MS Docs](https://docs.microsoft.com/en-us/visualstudio/extensibility/internals/solution-dot-sln-file?view=vs-2019)
A solution is a structure for organizing projects in Visual Studio. The solution maintains the state information for projects in two files: sln file (text-based, shared), and .suo file (binary, user-specific solution options).

### *Static Link Libray (.lib)*
Windows의 정적 라이브러리로, 정적 링크로 컴파일 시점에 라이브러리가 링커에 의해 연결되어 실행 파일의 일부분이 된다.

A LIB file contains a library of information used by a specific program. It may store a variety of information, which may include functions and constants referenced by a program or actual objects, such as text clippings, images, or other media. LIB files are typically referenced by applications and should not be opened manually.

### *How to import LIB in MSVC* | [Blog (KR)](https://scripter.co.kr/294)
Visual Studio를 사용하는 경우, lib을 사용 (외부 라이브러리 import) 하기 위해서는 "Linker>General>Additional Library Directories"에 lib 파일의 경로를 입력하고, "Linker>Input>Additional Dependencies"에 lib 파일의 이름을 입력하고, "C/C++>General>Additional Include Directories"에 h (include) 파일의 경로를 입력하면 된다.

### *Dynamic Link Library (.dll)* | [MS (KR)](https://support.microsoft.com/ko-kr/help/815065/what-is-a-dll) | [Wiki](https://en.wikipedia.org/wiki/Dynamic-link_library)
Windows의 동적 라이브러리로, DLL은 여러 프로그램에서 동시에 사용할 수 있는 코드와 데이터를 포함하는 라이브러리이다. 코드를 쉽게 재사용할 수 있으며 메모리 사용 효율성을 높일 수 있다. DLL을 사용하면 프로그램을 여러 개별 구성 요소로 모듈화할 수 있다. 각 모듈은 설치되어 있는 경우 런타임에 주 프로그램으로 로드할 수 있다. 모듈은 서로 분리되어 있으므로 프로그램의 로드 시간이 빨라지며 해당 기능을 요청할 때만 모듈이 로드된다. 또한 프로그램의 다른 부분에 영향을 주지 않고 업데이트를 각 모듈에 더 쉽게 적용할 수 있다. 변경 내용이 DLL 하나에만 적용되는 경우 전체 프로그램을 다시 빌드하거나 설치할 필요 없이 업데이트를 적용할 수 있다.

동적 링크로 실행 파일에서 라이브러리의 기능을 사용 시에만, 라이브러리 파일을 참조 또는 다운로드해서 기능을 호출한다. 정적 링크와 다르게 컴파일 시점에 실행 파일에 함수를 복사하지 않고, 함수의 위치 정보만 갖고 그 함수를 호출할 수 있게 한다. 더 적은 리소스를 사용하며, 모듈식 구조를 사용할 수 있으며, 배포와 설치가 비교적 쉬우며, 개발을 나눠서 할 수 있으며 재사용이 가능하며 디버깅도 용이하다. 종속성을 유의해야한다.

A DLL file is a compiled library that contains a set of precedures and/or drivers that are referenced and executed by a Windows program. It allows multiple programs to access shared functions through common libraries. DLL files are dynamically linked into a program at runtime, meaning they are only loaded when needed.

### *How to import DLL in MSVC* | [Blog (KR)](https://wnsgml972.github.io/setting/2018/11/01/dll_lib/)
기본 lib과 h (include) 파일을 설정하는 방법은 "VC++ 디렉터리>포함 디렉터리"에 h (include) 파일들 경로를 설정하고, "VC++ 디렉터리>라이브러리 디렉터리"에 lib 파일들 경로를 설정하면 된다.

Visual Studio를 사용하는 경우, dll을 사용 (외부 라이브러리 import) 하기 위해서는 "링커>일반>추가 라이브러리 디렉터리"에 lib 파일의 경로를 입력하고, "링커>입력>추가 종속성"에 lib 파일의 파일명을 입력하고, "C/C++>일반>추가 포함 디렉터리"에 h (include) 파일의 경로를 입력하고, "구성 속성>디버깅>환경"에 dll 파일의 경로를 입력하면 된다.

### *Export File (.exp)* | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/reference/dot-exp-files-as-linker-input?view=msvc-160)
Export file (.exp) contain information about exported functions and data items. When LIB creates an import library, it also creates an .exp file.

### *EXE (.exe)* | [Wiki (KR)](https://ko.wikipedia.org/wiki/EXE)
EXE는 일반적인 파일 확장자로 컴퓨터 프로그램의 실행 파일을 가리킨다. 오픈VMS, 도스, 마이크로소프트 윈도우, 리엑트오에스, OS/2 운영 체제에서 사용할 수 있다.

실행 프로그램 자체뿐 아니라, 많은 EXE 파일들은 비트맵, 실행 프로그램이 그래픽 사용자 인터페이스를 사용하는, 아이콘과 같은 리소스라고 불리는 다른 구성 요소들을 포함할 수 있다.

도스 실행 파일 포맷은 64 킬로바이트로 크기가 제한되는 COM 실행 파일과 다르다. 도스 실행 파일 헤더는 여러 개의 세그먼트가 DMA에서 로드될 수 있으며 64 킬로바이트 이상의 실행 파일을 지원하는 리로케이션 정보를 포함하고 있다.

### *Shortcut (.lnk, 바로가기)* | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EB%B0%94%EB%A1%9C_%EA%B0%80%EA%B8%B0)
바로 가기(Shortcut)는 다른 파일의 위치를 포함하는 작은 파일이며, 실행을 위해 특정한 매개 변수를 사용하기도 한다. 이 바로 가기 아이콘은 다양한 운영 체제의 바탕 화면, 시작 메뉴, 작업 표시줄에 놓이며, 명령 줄에서가 아닌 GUI에서만 동작한다. "링크 파일", "LNK 파일"이라고도 부른다.

마이크로소프트 윈도는 .lnk를 파일 확장자로 사용하며, 아이콘에 굽은 화살표 모양을 기본으로 보여 준다. 이 확장자는 폴더 옵션의 "알려진 파일 형식의 파일 확장명 숨기기"에 체크를 없애도 윈도 탐색기에서는 보이지 않는다.

### *Universal Windows Platform (UWP) Application* | [MS Docs](https://docs.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide) | [MS Docs (KR)](https://docs.microsoft.com/ko-kr/windows/uwp/get-started/universal-application-platform-guide)
UWP is one of many ways to create client applications for Windows. UWP apps use WinRT APIs to provide powerful UI and advanced asynchronous features that are ideal for internet-connected devices.

UWP is one choice for creating apps that run on Windows 10 devices, and can be combined with other platforms. UWP apps can make use of Win32 APIs and .NET classes (see API Sets for UWP apps, Dlls for UWP apps, and .NET for UWP apps).

The Microsoft development story continues to evolve, and along with initiatives such as WinUI, MSIX, and Project Reunion, UWP is a powerful tool for creating client apps.

### *Extensible Application Markup Language (XAML)* | [Wiki](https://en.wikipedia.org/wiki/Extensible_Application_Markup_Language) | [Wiki (KR)](https://ko.wikipedia.org/wiki/XAML)
Extensible Application Markup Language (XAML) is a declarative XML-based language developed by Microsoft that is used for initializing structured values and objects. It is available under Microsoft's Open Specification Promise. The acronym originally stood for Extensible Avalon Markup Language, Avalon being the code-name for Windows Presentation Foundation (WPF).

### *Windows Presentation Foundation (WPF)* | [MS Docs](https://docs.microsoft.com/en-us/visualstudio/designers/getting-started-with-wpf?view=vs-2019) | [MS Docs (KR)](https://docs.microsoft.com/ko-kr/visualstudio/designers/getting-started-with-wpf?view=vs-2019)
Windows Presentation Foundation (WPF) is a UI framework that creates desktop client applications. The WPF development platform supports a broad set of application development features, including an application model, resources, controls, graphics, layout, data binding, documents, and security. The framework is part of .NET, so if you have previously built applications with .NET using ASP.NET or Windows Forms, the programming experience should be familiar. WPF uses the Extensible Application Markup Language (XAML) to provide a declarative model for application programming.

### *Wine (Wine is not a emulator)* | [Homepage](https://www.winehq.org/)
Wine은 Linux, maxOS, BSD와 같은 POSIX 호환 운영체제에서 Windows 프로그램을 실행할 수 있는 호환성 레이어이다. 가상 머신이나 에뮬레이터와 같이 내부 Windows 로직을 시뮬레이션하는 대신 Wine은 Windows API 호출을 POSIX 시스템 호출로 즉시 대체한다. 다른 방식과 다르게 성능이나 메모리 문제가 적으며, Windows 프로그램을 desktop에 깔끔하게 통합할 수 있다.

### *Windows GDI* | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/gdi/windows-gdi)
The Microsoft Windows graphics device interface (GDI) enables applications to use graphics and formatted text on both the video display and the printer. Windows-based applications do not access the graphics hardware directly. Instead, GDI interacts with device drivers on behalf of applications.

## *Command*

### *Compile a C Program on the Command Line, Command `cl`* | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/walkthrough-compile-a-c-program-on-the-command-line?view=msvc-160)
```cmd
Microsoft (R) C/C++ 최적화 컴파일러 버전 19.27.29111(x64)
Copyright (c) Microsoft Corporation. All rights reserved.

simple.c
Microsoft (R) Incremental Linker Version 14.27.29111.0
Copyright (C) Microsoft Corporation.  All rights reserved.

/out:simple.exe
simple.obj
```
#### How to use command cl with C
- Compile foo.c: `> cl foo.c`
  - output: foo.exe and foo.obj
  - run: `> foo` or `> foo.exe`
- Compile several source codes to bar.exe: `> cl foo1.c foo2c. foo3.c /link /out:bar.exe`, can add warning level option with: `> cl /W4 ...`
- --help: `> cl /?`

### *Compile a Native C++ Program on the Command Line, Command `cl`* | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/walkthrough-compiling-a-native-cpp-program-on-the-command-line?view=msvc-160)
```cmd
Microsoft (R) C/C++ 최적화 컴파일러 버전 19.27.29111(x64)
Copyright (c) Microsoft Corporation. All rights reserved.

hello.cpp
Microsoft (R) Incremental Linker Version 14.27.29111.0
Copyright (C) Microsoft Corporation.  All rights reserved.

/out:hello.exe
hello.obj
```
#### How to use command cl with C++
- Compile foo.cpp: `> cl /EHsc foo.cpp`
  - output: foo.exe and foo.obj
  - run: `> foo` or `> foo.exe`

### *`CL /EH` (Exception Handling Model)* | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/reference/eh-exception-handling-model?view=msvc-160)
The `/EHsc` command-line option instructs the compiler to enable standard C++ exception handling behavior. Without it, thrown exceptions can result in undestroyed objects and resource leaks. Full compiler support for the Standard C++ exception handling model that safely unwinds stack objects requires `/EHsc` (recommended), `/EHs`, or `/EHa`.

### *`CL /LD` (Linking)*
- Make/Compile a dll file with foo.c: `> cl /LD foo.c`
  - output: foo.dll, foo.lib, foo.exp, foo.obj
- Link a foo.dll to bar.exe

### *`LIB`* | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/reference/lib-reference?view=msvc-160)
The Microsoft Library Manager (LIB.exe) creates and managers a library of Comman Object File Format (COFF) object files. LIB can also be used to create export files and import libraries to reference exporte definitions.

### *`LIB /DEF`* | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/reference/working-with-import-libraries-and-export-files?view=msvc-160)
`LIB /DEF` creates an import library and an export file. LINK uses the export file to build a program that contains exports (usually a dynamic-link library (DLL)), and it uses the import library to resolve references to those exports in other program.

### *`LINK`* | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/reference/linking?view=msvc-160)
The `LINK` is a Incremental Linker. In a C++ project, the linking step is performed after the compiler has compiled the source code into object files (.obj). The linker (link.exe) combines the object files into a single executable file.

### *`DUMPBIN`* | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/reference/dumpbin-reference?view=msvc-160)
The Microsoft COFF Binary File Dumper (DUMPBIN.EXE) displays information about Common Object File Format (COFF) binary files. DUMPBIN can be used to examine COFF object files, standard libraries of COFF objects, executable files, and dynamic-link libraries (DLLs).

- Show symbolic links in a file: `> dumpbin /exports foo.dll` in Command Prompt for VS

### *HRESULT*

### *HWND*

### Find Files, Command `dir`
#### How to use command dir
- Show files in a folder: `> dir`
- Find foo files in current directory: `> dir /s *.foo`
- --help: `> dir /?`

### Find String in Files, Command `find`
#### How to use command find
- --help: `> find /?`

### Delete files, Command `del`
#### How to use command del
- --help: `> del /?`
- Delete foo.c: `> del foo.c`

### Move a file, Command `move`
#### How to use command move
- --help: `> move /?`
- Move file foo.c under folder bar: `> move foo.c bar/`

#### Reference
- Program Files, Program Files (x86), https://www.howtogeek.com/129178/why-does-64-bit-windows-need-a-separate-program-files-x86-folder/, 2019-03-21-Thu
- Symbolic Link, https://fruitdev.tistory.com/85, 2020-08-05-Wed.
- EXE Wiki (Kor), https://ko.wikipedia.org/wiki/EXE, 2020-08-06-Thu.
- 실행 파일 Wiki (Kor), https://ko.wikipedia.org/wiki/%EC%8B%A4%ED%96%89_%ED%8C%8C%EC%9D%BC, 2020-08-06-Thu.
- DLL 이란?, https://support.microsoft.com/ko-kr/help/815065/what-is-a-dll, 2020-08-06-Thu.
- DLL, https://goddaehee.tistory.com/185, 2020-08-06-Thu.
- Library, https://jasonjason.tistory.com/15, 2020-08-06-Thu.
- Shortcut, https://ko.wikipedia.org/wiki/%EB%B0%94%EB%A1%9C_%EA%B0%80%EA%B8%B0, 2020-08-08-Sat.
- MSDN, https://social.msdn.microsoft.com/forums/en-us/home, 2020-09-16-Wed.
- MSDN Wiki, https://en.wikipedia.org/wiki/Microsoft_Developer_Network, 2020-09-16-Wed.
- Microsoft Docs, https://docs.microsoft.com/en-us/, 2020-09-16-Wed.
- Windows Wiki, https://en.wikipedia.org/wiki/Microsoft_Windows, 2020-09-16-Wed.
- UWP MS Docs, https://docs.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide, 2020-09-18-Fri.
- UWP MS Docs (Kor), https://docs.microsoft.com/ko-kr/windows/uwp/get-started/universal-application-platform-guide, 2020-09-18-Fri.
- XAML Wiki, https://en.wikipedia.org/wiki/Extensible_Application_Markup_Language, 2020-09-18-Fri.
- XAML Wiki (Kor), https://ko.wikipedia.org/wiki/XAML, 2020-09-18-Fri.
- WPF MS Docs, https://docs.microsoft.com/en-us/visualstudio/designers/getting-started-with-wpf?view=vs-2019, 2020-09-18-Fri.
- WPF MS Docs (Kor), https://docs.microsoft.com/ko-kr/visualstudio/designers/getting-started-with-wpf?view=vs-2019, 2020-09-18-Fri.
- Wine, https://www.winehq.org/, 2021-03-29-Mon.
- DLL Wiki, https://en.wikipedia.org/wiki/Dynamic-link_library, 2021-03-29-Mon.
- EXP MS Docs, https://docs.microsoft.com/ko-kr/cpp/build/reference/dot-exp-files-as-linker-input?view=msvc-160, 2021-03-30-Tue.
- Using an Import Library and Export File, https://docs.microsoft.com/en-us/cpp/build/reference/using-an-import-library-and-export-file?redirectedfrom=MSDN&view=msvc-160, 2021-03-30-Tue.
- Working with Import Libraries and Export Files, https://docs.microsoft.com/ko-kr/cpp/build/reference/working-with-import-libraries-and-export-files?view=msvc-160, 2021-03-30-Tue.
- Command Get-ChildItem, https://superuser.com/questions/496092/view-a-list-of-symbolic-links-on-system, 2021-03-31-Wed.
- Command dumpbin Blog KR, https://copynull.tistory.com/33, 20201-03-31-Wed.
- MFC Wiki, https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library, 2021-03-26-Fri.
- Desktop Window Manager Wiki, https://en.wikipedia.org/wiki/Desktop_Window_Manager, 2021-03-26-Fri.
- Win32 API MS Docs, https://docs.microsoft.com/en-us/windows/win32/, 2021-03-31-Wed.
- Win32, and Win64 Blog KR, https://m.blog.naver.com/tipsware/220919155847, 2021-03-31-Wed.
- Windows API Wiki, https://en.wikipedia.org/wiki/Windows_API, 2021-03-31-Wed.
- Command find Blog KR, https://realforce111.tistory.com/10, 2021-04-01-Thu.
- Command dir Blog KR, http://mwultong.blogspot.com/2006/10/file-find-command.html, 2021-04-01-Thu.
- Compile C in CLI command cl, https://docs.microsoft.com/en-us/cpp/build/walkthrough-compile-a-c-program-on-the-command-line?view=msvc-160, 2021-04-01-Thu.
- Command del Blog,https://www.freecodecamp.org/news/cmd-delete-folder-how-to-remove-files-and-folders-in-windows/, 2021-04-01-Thu.
- Compile C++ in CLI command cl, https://docs.microsoft.com/en-us/cpp/build/walkthrough-compiling-a-native-cpp-program-on-the-command-line?view=msvc-160, 2021-04-01-Thu.
- Command move, https://www.computerhope.com/issues/ch001476.htm, 2021-04-01-Thu.
- /EH option, https://docs.microsoft.com/en-us/cpp/build/reference/eh-exception-handling-model?view=msvc-160, 2021-04-01-Thu.
- Linking lib or dll, https://docs.microsoft.com/en-us/cpp/build/reference/dot-lib-files-as-linker-input?view=msvc-160, 2021-04-01-Thu.
- Build dll, https://stackoverflow.com/questions/1130479/how-to-build-a-dll-from-the-command-line-in-windows-using-msvc, 2021-04-01-Thu.
- COM, https://docs.microsoft.com/en-us/windows/win32/com/the-com-library, 2021-04-01-Thu.
- COM Wiki, https://en.wikipedia.org/wiki/Component_Object_Model, 2021-04-01-Thu.
- DLL, https://fileinfo.com/extension/dll, 2021-04-02-Fri.
- LIB, https://fileinfo.com/extension/lib, 2021-04-02-Fri.
- How to import DLL Blog KR, https://wnsgml972.github.io/setting/2018/11/01/dll_lib/, 2021-04-02-Fri.
- How to import LIB Blog KR, https://scripter.co.kr/294, 2021-04-02-Fri.
- How to use DLL in MSVC Blog KR, https://blog.naver.com/PostView.nhn?blogId=tipsware&logNo=221359282016&parentCategoryNo=&categoryNo=83&viewDate=&isShowPopularPosts=true&from=search, 2021-04-02-Fri.
- LIB, https://docs.microsoft.com/en-us/cpp/build/reference/lib-reference?view=msvc-160, 2021-04-02-Fri.
- DUMPBIN, https://docs.microsoft.com/en-us/cpp/build/reference/dumpbin-reference?view=msvc-160, 2021-04-02-Fri.
- sln, https://docs.microsoft.com/en-us/visualstudio/extensibility/internals/solution-dot-sln-file?view=vs-2019, 2021-04-06-Tue.
- LIB /DEF, https://docs.microsoft.com/en-us/cpp/build/reference/working-with-import-libraries-and-export-files?view=msvc-160, 2021-04-06-Tue.
- Linking, https://docs.microsoft.com/en-us/cpp/build/reference/linking?view=msvc-160, 2021-04-06-Tue.
- .Net Framework Blog KR, https://hackersstudy.tistory.com/46, 2021-04-06-Tue.
- .Net Documentation, https://docs.microsoft.com/en-us/dotnet/, 2021-04-06-Tue.
- .Net Framework Documentation, https://docs.microsoft.com/en-us/dotnet/framework/, 2021-04-06-Tue.
- What is .NET?, https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet?&WT.mc_id=Educationaldotnet-c9-scottha, 2021-04-06-Tue.
- Windows IPC MS Docs, https://docs.microsoft.com/en-us/windows/win32/ipc/interprocess-communications, 2021-04-14-Wed.
- Windows IPC Blog KR, http://dolphin.ivyro.net/file/windows_api/windows_ipc.html, 2021-04-14-Wed.
- Signal MS Docs, https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/signal?view=msvc-160, 2021-04-14-Wed.
- Data Copy MS Docs, https://docs.microsoft.com/en-us/windows/win32/dataxchg/data-copy, 2021-04-14-Wed.
- File Mapping MS Docs, https://docs.microsoft.com/en-us/windows/win32/memory/file-mapping, 2021-04-14-Wed.
- Pipes MS Docs, https://docs.microsoft.com/en-us/windows/win32/ipc/pipes, 2021-04-14-Wed.
- RPC MS Docs, https://docs.microsoft.com/en-us/windows/win32/rpc/microsoft-rpc-components, 2021-04-14-Wed.
- Windows Sockets 2 MS Docs, https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-start-page-2, 2021-04-14-Wed.
- Anonymous Pipe Operations MS Docs, https://docs.microsoft.com/en-us/windows/win32/ipc/anonymous-pipe-operations, 2021-04-14-Wed.
- Creating Named Shared Memory, https://docs.microsoft.com/en-us/windows/win32/memory/creating-named-shared-memory, 2021-04-14-Wed.
- Data Types, https://docs.microsoft.com/en-us/windows/win32/winprog/windows-data-types, 2021-04-15-Thu.
- Data Type Ranges, https://docs.microsoft.com/en-us/cpp/cpp/data-type-ranges?view=msvc-160&viewFallbackFrom=vs-2019, 2021-04-15-Thu.
- Built-in Types (C++), https://docs.microsoft.com/en-us/cpp/cpp/fundamental-types-cpp?view=msvc-160, 2021-04-15-Thu.
- Keywords (C++), https://docs.microsoft.com/en-us/cpp/cpp/keywords-cpp?view=msvc-160, 2021-04-15-Thu.
- The meaning of W and L in WPARAM and LPARAM, https://archive.vn/hUc6B#selection-959.0-1011.199, 2021-04-15-Thu.
- The Old New Thing, https://devblogs.microsoft.com/oldnewthing/, 2021-04-15-Thu.
- What do the letters W and L stand for in WPARAM and LPARAM, https://devblogs.microsoft.com/oldnewthing/20031125-00/?p=41713, 2021-04-15-Thu.
- What happens to WPARAM, LPARAM, and LRESULT when they travel between 32-bit and 64-bit windows?, https://devblogs.microsoft.com/oldnewthing/20110629-00/?p=10303, 2021-04-15-Thu.
- Windows Coding Conventions, https://docs.microsoft.com/en-us/windows/win32/learnwin32/windows-coding-conventions, 2021-04-15-Thu.
- Working with Stings, https://docs.microsoft.com/en-us/windows/win32/learnwin32/working-with-strings, 2021-04-15-Thu.
- What Is a Window?, https://docs.microsoft.com/en-us/windows/win32/learnwin32/what-is-a-window-, 2021-04-15-Thu.
- WinMain, https://docs.microsoft.com/en-us/windows/win32/learnwin32/winmain--the-application-entry-point, 2021-04-15-Thu.
- WinMain (1) soen, http://soen.kr/lecture/win32api/lec2/lec2-2-1.htm, 2021-04-15-Thu.
- WinMain (2) soen, http://soen.kr/lecture/win32api/lec2/lec2-2-2.htm, 2021-04-15-Thu.
- Whole Process Walkthrough: Create a tranditional Windows Desktop application (C++), https://docs.microsoft.com/en-us/cpp/windows/walkthrough-creating-windows-desktop-applications-cpp?view=msvc-160&viewFallbackFrom=vs-2019, 2021-04-15-Thu.
- Overview, https://docs.microsoft.com/en-us/windows/win32/learnwin32/your-first-windows-program, 2021-04-15-Thu.
- Creating a Window, https://docs.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window, 2021-04-15-Thu.
- Window Messages (Get Started with Win32 and C++), https://docs.microsoft.com/en-us/windows/win32/learnwin32/window-messages, 2021-04-15-Thu.
- WNDCLASSA, https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-wndclassa, 2021-04-15-Thu.
- CreatWindowA, https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowa, 2021-04-15-Thu.
- WINAPI vs. APIENTRY Blog KR, https://m.blog.naver.com/PostView.nhn?blogId=k7102147&logNo=150029897435&proxyReferer=https:%2F%2Fwww.google.com%2F, 2021-04-16-Fri.
- Windows GDI, https://docs.microsoft.com/en-us/windows/win32/gdi/windows-gdi, 2021-04-16-Fri.
- DWORD, https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/262627d8-3418-4627-9218-4ffe110850b2, 2021-04-16-Fri.
- WD_COPYDATA size, https://forums.codeguru.com/showthread.php?464640-How-much-data-and-what-type-can-be-sent-using-WM_COPYDATA, 2021-04-16-Fri.
- Writing the Window Procedure, https://docs.microsoft.com/en-us/windows/win32/learnwin32/writing-the-window-procedure, 2021-04-16-Fri.
- Painting the Window, https://docs.microsoft.com/en-us/windows/win32/learnwin32/painting-the-window, 2021-04-16-Fri.
- Closing the Window, https://docs.microsoft.com/en-us/windows/win32/learnwin32/closing-the-window, 2021-04-16-Fri.
- Managin Application State, https://docs.microsoft.com/en-us/windows/win32/learnwin32/managing-application-state-, 2021-04-16-Fri.

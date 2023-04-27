# :iphone: Mobile

`This page is for the "Mobile Application".`

---

# :iphone: Mobile System/Platform

## :iphone: [Google Android](https://developer.android.com/) | [Wiki](https://en.wikipedia.org/wiki/Android_(operating_system))

`Contents of 'Android' is from the 'System' page.`

### [Android Wear OS by Google](https://developer.android.com/training/wearables)

With Wear OS by Google, you can write apps that enable users to stay connected, accomplish tasks, and express themselves.

Wear OS is based on Android and is optimized for the wrist. If you have developed for Android, then features such as apps, notifications, and Actions on Google may be familiar to you. In addition, Wear OS offers new development options such as watch faces.

### [Android TV](https://developer.android.com/training/tv)

If you've got an Android app or game, Android TV can bring it to your users in their living room. Android TV apps use the same architecture as those for phones and tablets. This approach means you can build new TV apps based on what you already know about building apps for Android, or extend your existing apps to also run on TV devices.

### [Android for Cars](https://developer.android.com/training/cars) | Android Auto | Android Automotive OS

- Supported app categories
  - Media apps (audio)
  - Messaging apps
  - Navigation apps
  - Point of Interest (POI) apps
  - Video apps

### Android Auto

요약: 스마트폰에 있는 앱을 자동차에서 사용가능케하는 OS, 자동차가 아닌 스마트폰에 앱을 설치함.

Android Auto provides a driver-optimized app experience for users with an Android phone and the Android Auto app, but who do not have a vehicle that uses Android Automotive OS. If a user's car or aftermarket stereo system supports Android Auto, they can use your app directly on their car's display by connecting their phone.

You enable Android Auto to connect with your phone app by creating services that Android Auto uses to display a driver-optimized interface to the driver. You reuse these services for your Android Automotive OS app, but users do not install your phone app on their cars.

### Android Automotive OS

요약: 자동차에 설치되는 infortainment 시스템을 위한 OS, 자동차에 직접 앱을 설치함.

Android Automotive OS is an Android-based infotainment system that is built into vehicles. The car's system is a stand-alone Android device that is optimized for driving. With Android Automotive OS, users install your app directly onto the car instead of their phones.

For media apps, your app must include a media browser service (see Build media apps for cars for instructions). You can use the same media browser service with both Android Automotive OS and Android Auto. However, there are some activities such as sign-in and settings that you must design specifically for Android Automotive OS. For more information, see Adapt sign-in flow and Design settings in the Android Automotive OS app design guidelines.

### [Android Core - Architecture](https://source.android.com/docs/core/architecture)

There are two levels of compatibility for devices implementing AOSP: AOSP compatibility and Android compatibility. An AOSP-compatible device must conform to the list of requirements in the Compatibility Definition Document (CDD). An Android-compatible device must conform to the list of requirements in the CDD and Vendor Software Requirements (VSR) and tests such as those in the Vendor Test Suite (VTS) and Compatiblity Test Suite (CTS). For further information on Android compatibility, refer to the Android compatibility program.

AOSP software stack architecture:
- Android Apps
- Privileged Apps
- Android API & System API
- Device Manufacturer Apps
- Android Framework
- System Services
- Android Runtime (ART): A Java runtime envrionment provided by AOSP.
- Hardware Abstraction Layer (HAL): A HAL is an abstraction layer with a standard interface for hardware vendors to implement.
- Native Daemons and Libraries
- Linux Kernel: The kernel is the central part of any operating system and talks to the underlying hardware on a device. Where possible, the AOSP kernel is split into hardware-agnostic modules and vendor-specific modules.

### [Android Core - Kernel](https://source.android.com/docs/core/architecture/kernel)

The Android kernel is based on an upstream Linux Long Term Supported (LTS) kernel. At Google, LTS kernels are combined with Android-specific patches to form what are known as Android Common Kernels (ACKs).

Newer ACKs (version 5.4 and above) are also known as GKI kernels. GKI kernels support the separation of the hardware-agnostic generic core kernel code and GKI modules from the hardware-specific vendor modules.

The GKI kernel interacts with hardware-specific vendor modules containing system on a chip (SoC) and board-specific code. The interaction between the GKI kernel and vendor modules is enabled by the Kernel Module Interface (KMI) consisting of symbol lists identifying the functions and global data required by vendor modules. Figure 1 shows the GKI kernel and vendor module architecture:

---

## :iphone: Apple | [Wiki](https://en.wikipedia.org/wiki/Apple_Inc.)

---

## :iphone: [Samsing Electronics Tizen](https://www.tizen.org/) | [Tizen .NET](https://developer.samsung.com/tizen)

### [Tizen Architecture](https://docs.tizen.org/platform/porting/overview/)

- Native Applications & Web Framework
- Native Subsystems
  - Application framework | Base | Connetivity | Graphics and UI | Location
  - Messaging | Multimedia | Personal Information Management (PIM) | Security | System
  - Telephony | Web: optimized for low-power devices2
- Linux Kernel and Device Drivers

---

## :iphone: [LG Electronics webOS Open Source Edition (OSE)](https://www.webosose.org/)

### [webOS Architecture](https://www.webosose.org/docs/guides/core-topics/architecture/architecture-overview/)

- Core Applications
  - System UI | System | Sample Apps
- Application Framework
  - SDK | Web
- Managers & Services
    - App | Display | Media | i18n/l10mn | Diagnostics
    - Connectivity | DB | Notification | Settings | Development
    - Misc. | Intelligence | External Device | SW Update
- Base Components
    - Bus | Display | Media | i18n/l10n | Diagnostics
    - Connectivity | JS Service | DB | HAL | Base Libs
    - Boot | Web Engine | Performance | Intelligence | SW Update
- BSP
    - Event | Display | Media | Device | Connectivity
    - Performance | General
- Kernel
    - Security

### [[CES 2022] 개인 맞춤형 플랫폼으로의 진화, LG webOS](https://live.lge.co.kr/life-style-webos/)

### [LG전자, webOS 앞세워 TV 플랫폼 사업 확 키운다](https://live.lge.co.kr/lg-web-os/)

---

## :books: Application Types

### Mobile Application | [Wiki](https://en.wikipedia.org/wiki/Mobile_app)

A mobile application, also referred to as a mobile app or simply an app, is a computer program or software application designed to run on a mobile device such as a phone, tablet, or watch.

Mobile applications often stand in contrast to desktop applications which are designed to run on desktop compuiters, and web applications which run in mobile web browsers rather than directly on the mobile device.

### Native Application | [Wiki](https://en.wikipedia.org/wiki/Mobile_app#Native_app)

All apps targeted toward a particular mobile platform are known as native apps. Therefore, an app intended for Apple device does not run in Android. As a result, most businesses develop apps for multiple platforms.

### Web Application (Web-based Application) | [Wiki](https://en.wikipedia.org/wiki/Mobile_app#Web-based_app)

A web-based app is implemented with the standard web technologies of HTML, CSS, and JavaScript. Internet access is typically required for proper behavior or being able to use all features compared to offline usage. Most, if not all, user data is stored in the cloud.

The performance of these apps is similar to a web application running in a browser, which can be noticeably slower than the equivalent native app. It also may not have the same level of features as the native app.

### Hybrid Application | [Wiki](https://en.wikipedia.org/wiki/Mobile_app#Hybrid_app)

The concept of the hybrid app is a mix of native and web-based apps. Apps developed using Apache Cordova, Xamarin, React Native, Sencha Touch, and other frameworks fall into this category.

These are made to support web and native technologies across multiple platforms. Moreover, these apps are easier and faster to develop. It involves ues of single codebase which works in multople mobile operating systems.

Despite such advantages, hybrid apps exhibit lower performance. Often, apps fail to bear the same look-and-feel in different mobile operating systems.

---

### Mobile Application Development | [Wiki](https://en.wikipedia.org/wiki/Mobile_app_development)

### Platform

Front-end Development Tools:
- Accelerator
- MobileTogether
- Android
- App Inventor for Android
- Appcelerator
- Basic4android
- BlackBerry
- Codename One
- Corona SDK
- DragonRAD
- GeneXus for Mobile and Smart Devices
- IBM MobileFirst Studio
- iOS SDK (1)
- iOS SDK (2)
- Java ME
- Lazarus
- LambdaNative
- LiveCode
- Macromedia Flash Lite
- Marmalade
- Meme IDE
- Mendix
- Monaca
- Mono for Android
- MonoTouch
- MoSync
- NetBeans
- OpenPlug
- OutSystems
- PhoneGap and Apache Cordova
- Qt SDK
- Rhomobile
- RubyMotion
- Sencha Touch
- Smartface
- Stencyl
- Telerik Platform, and AppBuilder
- Unity
- Verivo AppStudio
- ViziApps
- V-Play Engine
- Wakanda
- Xamarin
- Xojo

Back-end Servers:
- Altova MobileTogether Server
- GO!AppZone by Globo plc
- IBM MobileFirst Server
- Metismo
- Wakanda
- Verivo Akula
- WebORB Integration Server

System Software:
- Adobe AIR
- BREW
- Firefox OS
- .NET Compact Framework
- OpenFL
- Palm OS
- Python
- Symbian
- Tizen
- Ubuntu Touch
- webOS
- Windows Mobile
- Windows Phone

### Mobile Development Framework | [Wiki](https://en.wikipedia.org/wiki/Mobile_development_framework)

### Mobile Application Distribution Platform | [Wiki](https://en.wikipedia.org/wiki/List_of_mobile_app_distribution_platforms)

- Apple Store | [Wiki](https://en.wikipedia.org/wiki/App_Store_(iOS/iPadOS))
- Google Play | [Wiki](https://en.wikipedia.org/wiki/Google_Play)
- Microsoft Store | [Wiki](https://en.wikipedia.org/wiki/Microsoft_Store)
- Amazon Appstore
- BlackBerry World
- Nokia Ovi
- Microsoft Windows Phone Store
- Opera Mobile Sotre
- Samsung Apps

---

### Reference
- Mobile Application Wiki, https://en.wikipedia.org/wiki/Mobile_app, 2021-09-02-Thu.
- Android Wiki, https://en.wikipedia.org/wiki/Android_(operating_system), 2021-09-02-Thu.
- Apple Wiki, https://en.wikipedia.org/wiki/Apple_Inc. 2021-09-02-Thu.
- From Native Application to React Native Application Blog, https://ridicorp.com/story/react-native-1year-review/, 2021-08-19-Thu.
- Mobile Application Development Wiki, https://en.wikipedia.org/wiki/Mobile_app_development, 2021-09-02-Thu.
- Mobile Development Framework Wiki, https://en.wikipedia.org/wiki/Mobile_development_framework, 2021-09-02-Thu.
- Mobile Application Distribution Platform Wiki, https://en.wikipedia.org/wiki/List_of_mobile_app_distribution_platforms, 2021-11-12-Fri.
- Apple App Store Wiki, https://en.wikipedia.org/wiki/App_Store_(iOS/iPadOS), 2021-11-12-Fri.
- Google Play Wiki, https://en.wikipedia.org/wiki/Google_Play, 2021-11-12-Fri.
- Microsoft Store Wiki, https://en.wikipedia.org/wiki/Microsoft_Store, 2021-11-12-Fri.
- Android Wear, https://developer.android.com/training/wearables, 2022-08-08-Mon.
- Android TV, https://developer.android.com/training/tv, 2022-08-08-Mon.
- Android for Cars, https://developer.android.com/training/cars, 2022-08-08-Mon.
- Android Auto vs. Apple Car Play Blog KR, https://dukwon.tistory.com/67, 2022-08-08-Mon.
- Android vs. Linux distro Blog KR, https://mond.tistory.com/entry/%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C%EB%8A%94-%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B8%B0%EB%B0%98%EC%9D%B4%EB%8B%A4, 2022-08-08-Mon.
- Linux Smart Phone Blog KR, https://sergeswin.com/1247/, 2022-08-08-Mon.
- Android OS Architecture Blog KR, https://codingcoding.tistory.com/591, 2022-08-09-Tue.
- Android on Raspberry Pi 4 Blog KR, https://leehands.tistory.com/entry/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B44-%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-10-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0, 2022-08-10-Wed.
- Android TV on Raspberry Pi 4 Blog KR, https://blog.naver.com/PostView.naver?blogId=cosmosjs&logNo=222262221050&parentCategoryNo=&categoryNo=56&viewDate=&isShowPopularPosts=false&from=postView, 2022-08-10-Wed.
- Android Kernel, https://source.android.com/docs/core/architecture/kernel, 2023-04-24-Mon.
- Android Architecture, https://source.android.com/docs/core/architecture, 2023-04-25-Tue.
- Tizen Architecture, https://docs.tizen.org/platform/porting/overview/, 2023-04-25-Tue.
- webOS Architecture, https://www.webosose.org/docs/guides/core-topics/architecture/architecture-overview/, 2023-04-25-Tue.
- Tizen, https://www.tizen.org/, 2023-04-27-Thu.
- Tizen .NET, https://developer.samsung.com/tizen, 2023-04-27-Thu.
- LG webOS, https://live.lge.co.kr/lg-web-os/, 2023-04-27-Thu.
- LG Life Style webOS, https://live.lge.co.kr/life-style-webos/, 2023-04-27-Thu.
- webOS Open Source Edition, https://www.webosose.org/, 2023-04-27-Thu.

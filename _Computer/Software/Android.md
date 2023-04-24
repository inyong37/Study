# [Android](https://developer.android.com/)

`Contents of this page is from the 'System' page.`

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

---

### Reference
- Android Wear, https://developer.android.com/training/wearables, 2022-08-08-Mon.
- Android TV, https://developer.android.com/training/tv, 2022-08-08-Mon.
- Android for Cars, https://developer.android.com/training/cars, 2022-08-08-Mon.
- Android Auto vs. Apple Car Play Blog KR, https://dukwon.tistory.com/67, 2022-08-08-Mon.
- Android vs. Linux distro Blog KR, https://mond.tistory.com/entry/%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C%EB%8A%94-%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B8%B0%EB%B0%98%EC%9D%B4%EB%8B%A4, 2022-08-08-Mon.
- Linux Smart Phone Blog KR, https://sergeswin.com/1247/, 2022-08-08-Mon.
- Android OS Architecture Blog KR, https://codingcoding.tistory.com/591, 2022-08-09-Tue.
- Android on Raspberry Pi 4 Blog KR, https://leehands.tistory.com/entry/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B44-%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-10-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0, 2022-08-10-Wed.
- Android TV on Raspberry Pi 4 Blog KR, https://blog.naver.com/PostView.naver?blogId=cosmosjs&logNo=222262221050&parentCategoryNo=&categoryNo=56&viewDate=&isShowPopularPosts=false&from=postView, 2022-08-10-Wed.

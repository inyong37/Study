# Check "Line" & "KakaoTalk" and take screenshots.

## InyongLaptop
- Windows 10: 'Windows-10-10.0.19041-SP0'
- LINE
  - 대상: C:\\Users\\Inyong\\AppData\\Local\\LINE\\bin\\LineLauncher.exe
  - C:\\Users\\Inyong\\AppData\\Local\\LINE\\bin
- 카카오톡
  - 대상: "C:\\Program Files (x86)\\Kakao\\KakaoTalk\\KakaoTalk.exe"
  - 시작 위치: "C:\\Program Files (x86)\\Kakao\\KakaoTalk"
- 그림판
  - 대상: "C:\\Windows\\System32\\mspaint.exe"
  
## MyNotebook
- Windows 7: 'Windows-7-6.1.7601-SP1'
- LINE
  - 대상: "C:\\Users\\Administrator\\AppData\\Local\\LINE\\bin\\LineLauncher.exe"
  - 시작 위치: "C:\\Users\\Administrator\\AppData\\Local\\LINE\\bin"
- 카카오톡 (같음)
  - 대상: "C:\\Program Files (x86)\\Kakao\\KakaoTalk\\KakaoTalk.exe"
  - 시작 위치: "C:\\Program Files (x86)\\Kakao\\KakaoTalk"
- 그림판 (같음)
  - 대상: "C:\\Windows\\System32\\mspaint.exe"

### MyNotebook에서 추가로 발생한 문제
- Windows 7은 최신(2021-06-15-Tue 기준) Python release 최신 중 Python 3.9.5가 설치되지 않음. :heavy_check_mark:
  - Python 3.9.5는 Windows 7 지원 안함 -> Python 3.8.10 설치 및 사용함.
- 화면 해상도가 달라서 pg.click() 구현의 좌표 값은 다시 함. :heavy_check_mark:
  - 클릭할 좌표를 computer resolution 맞게 dataclass points 선언 및 정의함.
- Line 실행하면 컴퓨터 용량이 적어서 팝업 window 표시되는데 이를 없애야함. :heavy_check_mark:
  - MyNotebook platform 경우, 추가로 해당 window 확인 버튼 클릭하도록 추가함.
- file name 앞 글자가 잘렸는데 이것 또한 paint save window 로딩이 완료되지 않아서 발생함. :heavy_check_mark:
  - save 동작 전후로 time sleep 1초 하도록 함.
- print screen 키가 제대로 동작 안 하지만 이건 paint save window 로딩이 완료되지 않아서 저장하면서 발생함. :heavy_check_mark:
  - save 동작 전후로 time sleep 1초 하도록 함.
- LENOVO 하드웨어 테스트(정기 점검)가 자동으로 실행됨.
  - "Lenovo Solution Center>하드웨어 검색>검사 스케줄>스케줄러 열기": 매월 17일 1:00 AM에서 매월 1일 1:00 AM으로 변경함(비활성도 있음).
- Windows 7 업데이트를 꺼야함.

## 공통
- get executable file path by finding(grep) :heavy_check_mark:
  - folder, file 많아 searching 시간이 오래 걸림 -> 직접 수작업으로 Line, KakaoTalk 경로 찾아서 사용하도록 함.
- turn-on abd log-in: api vs. handmade :heavy_check_mark:
  - local desktop api는 없는 것 같음.
  - 정해진 시간에 line 키고 로그인하고, kakao talk 키고 로그인하고, paint 키고 스크린샷찍고 저장하고, paint 종료하고, kakao talk 종료하고, line 종료하도록 함.
  - line이 일반적으로 켰을 때는 캐럿이 비밀번호에 있어서 바로 입력하면 되지만, 업데이트 등 다른 window가 발생할 경우? :construction:
  - kakaotalk은 키면 자동 로그인 되어서 캐럿이 비밀번호에 있어서 바로 입력하면 되는데, 업데이트 등 다른 window가 발생할 경우? :construction:
    - set program on the top 코드를 넣었으나, 때때로 오류가 발생함 (window를 못 찾는 경우)
  - line, kakaotalk, Windows 모두 업데이트를 끌 수 있을까? :construction:
- line, kakaotalk 메세지 확인은 마우스/키보드로 하나씩 클릭하도록? 클릭하고 스크린샷 하나 더 찍도록 하기 :heavy_check_mark:
- check message: api vs. handmade :heavy_check_mark:
  - API 없음 -> pyautigui를 이용함.
- screenshot :heavy_check_mark:
  - pyautogui를 이용함.
- laptop과 notebook이 각각 정해진 시간에 동작하도록 하기 :heavy_check_mark:
  - Windows 업데이트는 컴퓨터를 끄지 않는 한 발생하지 않을 것으로 예상함.
  - Line 또는 KakaoTalk 업데이트가 발생할 수도 있음.
  - schedule library 사용함.
- python dataclass에서 dictionary 만드는 방법 :construction:
- 그림판이 킨 이후에 foreground에서 background로 돌아감 :heavy_check_mark:
  - printscreen 후에 그림판이 들어감 순서가 꼬인 듯 싶음.
  - 2번 key를 부르고 있었음 -> 1번으로 변경함.
- 그림판이 저장할 때 이미 저장되어 있으면 count를 해야하는가? :heavy_check_mark:
  - count에 따라서 3가지로 나눠서 하도록 함.
- task kill 실행해서 process(line, kakaotalk, paint)를 껐지만 숨겨진 아이콘에 남아있음. :heavy_check_mark:
  - 한번 마우스로 휘저으면 바로 사라짐.
  - 한번 돌도록 함수 구현함.
- sending message to army -> BootCamp.py :construction:
  - 휴대폰 본인 인증을 해결할 방법을 찾아야함
    .- 맥이였으면 폰에 문자가 온 알림을 가져올 수 있었을 듯
    - computer vision을 이용하는 방안
- 프로그램(Line 또는 KakaoTalk)이 다른 컴퓨터에서 종료되지 않고 켜져있으면 로그인하겠냐는 팝업이 발생함.
  - 꼭 프로그램을 종료하기.
- 화상 키보드는 무조건 최상단으로 되기 때문에 조심(항상 연결 해제할 때 꺼야함).

## Program Update Pop-up
- Windows :heavy_check_mark:
  - 재시작하지 않으면 발생하지 않을 것으로 예상됨.
  - 업데이트 중지 기간을 설정하는 방안: "설정>Windows 업데이트>고급 옵션>업데이트 일시 중지>날짜 선택"
- Line
  - 방안 필요함.
- KakaoTalk
  - googling 결과, "KakaoTalkUpdate.exe"를 빈 파일(txt를 확장자 변경 등의 방식)으로 교체하는 방법 있음.
    - 교체하지 않고 삭제만 할 경우, Windows 재시작을 한다고 해서 교체를 해야함.
    - 단, 업데이트를 하고 싶으면 수동으로 설치해야함 - 위험.
    - reference: https://stadrem.tistory.com/21
  - 다른 방안 필요함.
- Paint :heavy_check_mark:
  - Windows 큰 변화 없으면 없을 것이라 예상됨.
- Teamviewer :heavy_check_mark:
  - 입소 전에 컴퓨터 2대의 Teamviwer를 종료하기.
- ipTIME의 "ipDISK Drive"와 "ipTIME NAS Utility"가 자꾸 시도때도 없이 업데이트 했는데, 하라고 팝업이 뜸. :heavy_check_mark:
  - ipTIME NAS Utility 삭제하려고 했더니 ipDISK Drive가 종속성이 있음.
  - 지금 삭제하고 나중에 다시 설치하기.

## Teamviewer Pop-up :heavy_check_mark:
- 다른 컴퓨터와 연결한 뒤, 종료하면 ["후원 세션"](Teamviewer_Donation_Session.JPG) 또는 ["세션 시간 초과"](Teamviewer_Session_Timeout.JPG) 팝업 window가 발생해서 enter, 화살표 등의 keyboard input이 원하는 window로 들어가지 않음.
  - "Chrome Remote Desktop"을 사용하기

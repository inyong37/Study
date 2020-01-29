# 'Program Files' versus 'Program Files (x86)'

## 'Program Files' 에는 64-bit program 이, 'Program Files (x86)' 에는 32-bit program 들이 나눠서 설치된다.
```
옛날 컴퓨터는 Intel 의 8086 칩을 사용했는데 처음에는 16-bit 였고 그 이후 32-bit 가 되었다.
따라서 16-bit와 32-bit는 x86 이라 불리고 64-bit 는 x64 라 불린다.
(지금 대부분의 컴퓨터는 16-bit 는 지원하지 않는다.)
현재 컴퓨터는 다양한 칩을 사용하는데 대부분 64-bit 를 지원한다.
32-bit 로 만들어진 응용 프로그램들은 'WOW64 (Windows on Windows 64-bit)' 를 통해 64-bit 에서도 실행이 가능하다.
따라서 Windows 에서는 32-bit 프로그램과 64-bit 프로그램을 섞이지 않고 나눠서 저장하고자 했다.
그래서 'C:/' 에는 'Program Files' 와 'Program Files (x86)' 2개의 폴더에 각각 나눠서 저장하게 설계되었다.
2019-03-21-Thu
```

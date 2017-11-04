# Web Scrap
Scrap and Collect Text Data via Web

## 패키지 설치
우선, web-scrap은 python3 기반으로 구현되어 있다.
다음 단계에서 파이썬 패키지를 설치하기 위하여 pip를 함께 설치한다.

### Mac, Ubuntu
맥과 우분투는 apt-get을 이용하여 설치한다. 
계정 모드에 따라 설치해야 권한 문제가 발생하지 않는다.
로컬의 docker 환경인 경우, 관리자 계정을 따른다.

계정모드 | Command 
------- | --------
일반 계정 | sudo apt-get install python3 python3-pip  
관리자 계정 | apt-get install python3 python3-pip  

### 윈도우
윈도우는 OS 플랫폼에 설치해야 한다. (2017년 11월 4일 최신 버전은 3.6.3이다.)

|플랫폼|다운로드 링크| 
|:-------:|:--------|
|x86|[Python3 3.6.3-x86](https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe)|
|x64|[Python3-3.6.3-x64](https://www.python.org/ftp/python/3.6.3/python-3.6.3-amd64.exe)|

## 패키지 설치
프로그램 구동을 위하여 필요한 패키지는 아래와 같다.

1. BeautifulSoup4
2. Notedown
3. Selenium

Command 화면으로 이동하여 해당 플랫폼에 해당하는 코드를 실행한다.

|플랫폼|Command| 
|:-------:|:--------|
|Windows, 가상환경|pip install BeautifulSoup4 notedown selenium|
|Mac/Ubuntu 일반계정|pip3 install BeautifulSoup4 notedown selenium|
|Mac/Ubuntu 관리계정|pip3 install BeautifulSoup4 notedown selenium|

## phantomjs 설치
별도로 WebDriver 중 하나인 phantomjs를 설치한다.

## 프로그램 실행하기
위의 단계를 모두 수행이 완료되면, Command창에서 다음과 같은 Command를 실행한다. 

|플랫폼|Command| 
|:-------:|:--------|
|Windows, 가상환경|python newclip.py|
|Mac/Ubuntu 일반계정|python3 newclip.py|

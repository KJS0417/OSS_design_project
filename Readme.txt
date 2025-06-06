1. Python 설치 (미설치 시)

Python이 설치되어 있지 않다면 공식 웹사이트에서 설치:
-> https://www.python.org/downloads/


2. VS Code 설치 및 확장 기능 설정

VS Code 다운로드: https://code.visualstudio.com/
VS Code 실행 후, 왼쪽 사이드바의 Extensions (확장 프로그램) 아이콘 클릭 → Python 확장 설치


3. 제출한 PayLog.zip 파일을 바탕화면에 압축 해제 

PayLog.zip --(압축 풀기)--> PayLog 폴더


4. 프로젝트 폴더 열기

VS Code 상단 메뉴에서 
파일 -> 폴더 열기 -> PayLog 폴더 선택


5. 필요한 패키지 설치

VS Code 터미널(Ctrl + ` )을 열고 아래 명령 실행:
pip install matplotlib chardet


6. main.py 실행

(1) VS Code에서 main.py 파일 열기(더블 클릭) -> 오른쪽 상단의 ▶ Run 버튼 클릭

(2) VS Code 터미널(Ctrl + ` )을 열고 아래 명령 실행:
python main.py


7. 첫 실행 시 비밀번호 설정

프로그램을 처음 실행하면 비밀번호 설정 창이 뜨고, 설정 후 메인 창이 열림

비밀번호는 C:\Users\사용자이름\Documents\PayLog\password.txt에 저장됨


[참고 사항]

비밀번호를 잊은 경우: 

C:\Users\사용자이름\Documents\PayLog\password.txt 파일 삭제 후 프로그램 재실행
비밀번호 설정 창이 뜨고, 비밀번호 설정 후 다시 프로그램 사용 가능

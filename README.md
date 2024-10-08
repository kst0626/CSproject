## CSproject-AI 헬스 트레이너
## 조이름: CS

## 조원: 김승태, 한지상, 정의찬, 이채은

## 작품개요: 실시간으로 카메라를 이용해 운동영상을 띄운 뒤에 음성으로 자세를 교정하게 해주는 ai 헬스 케어

## 블럭도
<img width="481" alt="블록도" src="https://github.com/kst0626/CSproject/assets/152972876/f1dce628-9309-4a83-872e-fa6908931556">


*미디어파이프(Mediapipe)-구글에서 주로 인체를 대상으로 하는 비전 인식기능들을 AI모델 개발과 기계 학습까지 마친 상태로 제공하는 서비스

*OpenCV - Open Source Computer Vision의 약자로 영상 처리에 사용할 수 있는 오픈 소스 라이브러리

*JSON - "JavaScript Object Notation"의 약자로 데이터를 쉽게 교환하고 저장하기 위한 텍스트 기반의 개방형 데이터 교환 형식

## 라즈베리파이 가상 환경 구축 후 가속도 센서를 통해  x, y, z 좌표 출력 (5/2)
https://github.com/Cubechan/Capston_Design/assets/168626501/7437446c-05b3-48f4-8e73-ec88bbc936ec



## tts 가상환경에서 구현(5/22)
https://github.com/Cubechan/Capston_Design/assets/168626501/3d385356-4651-469c-9038-358d5fbac586

## stt 테스트 구현
https://github.com/kst0626/CSproject/assets/152972876/fd75ce74-9bac-451b-b54d-f4fa6701f7d0


## tts와 stt를 활용한 스케줄러 구현 (6/6)
https://github.com/kst0626/CSproject/assets/152972876/19fa4aa9-7ce5-4d55-ad13-f54d98fb4a22


## Mediapipe 랜드 마크
![미디어 파이프](https://github.com/kst0626/CSproject/assets/152972876/043f3e18-848f-4ec4-93c1-b7aefcbf517e)

## Mediapipe에서 스쿼트 운동 자세 실시간으로 출력, tts 출력
https://github.com/kst0626/CSproject/assets/152972876/72130d87-24df-4c5d-a6f4-ecf50c7630af

## 기능 업데이트 (9/20)
스쿼트 운동 중에 음악재생 기능 추가

stt 기능을 활용하여 음성인식 키(우리 조는 'm'키로 설정)로 음악 재생 및 정지 구현

이후의 다양한 기능 추가 예정

https://github.com/user-attachments/assets/ce859edb-1f91-49af-b696-0fb9953744dc

## 웹페이지 구현 (9/27)
URL:  https://kboard-e627d0c6b98a.herokuapp.com

기존 코드의 관리를 용이하기 위해 python 사용

윈도우 기반이기 때문에 Waitress로 어플리케이션 실행

heroku를 이용하여 어플리케이션 배포(url 생성)

## 부가기능 추가구현 (10/11)
<코드>

![music_1](https://github.com/user-attachments/assets/d94551d6-cd3e-4bca-a0eb-d5938feb400b)

![music_2](https://github.com/user-attachments/assets/6cc8f571-a93f-4c60-8f41-fc4105d6e87f)


https://github.com/user-attachments/assets/c07b8276-9fb6-46dc-863c-84fa5541cd07

사용자가 원하는 음악 요청시 설정된 API(우리 조는 youtube로 설정)에 음악을 검색 후 음악 송출

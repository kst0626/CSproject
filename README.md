## 헬스 트레이너
## 조이름: 야 너두 몸짱이 될 수 있어

## 조원: 김승태, 한지상, 정의찬, 이채은, 서정원

## 작품개요: 실시간으로 카메라를 이용해 운동영상을 띄운 뒤에 음성으로 자세를 교정하게 해주는 ai 헬스 케어

## 블럭도
![최종블럭도](https://github.com/user-attachments/assets/e6543997-958c-4c59-8fa3-e294d4d574d9)

*미디어파이프(Mediapipe)-구글에서 주로 인체를 대상으로 하는 비전 인식기능들을 AI모델 개발과 기계 학습까지 마친 상태로 제공하는 서비스

*OpenCV - Open Source Computer Vision의 약자로 영상 처리에 사용할 수 있는 오픈 소스 라이브러리



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

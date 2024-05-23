### CSproject

# 가상환경에서 tts구동
https://github.com/kst0626/CSproject/assets/152972876/0f66261b-3045-458d-b34f-8ecafec1bd1b

ssh로 구동하였으며 myenv는 가상환경 이름임
# mediapipe

# 오류1-네트워크 연결문제
  브릿지, nat 등 연결 방식을 바꿔도 해결이 안되어서
  네트워크 연결문제로 vmware 재설치  
  
  해당 명령어 사용
  
  ![network solution](https://github.com/kst0626/CSproject/assets/152972876/62063067-f10c-4a7d-9bd1-a832df535dea)
  
  dhcp 서버로부터 아이피를 받아오는 명령어
 
  그러나 vmware 재시작할 때마다 해당 명령어를 입력해야만 연결되는 문제있음

# 오류2-mediapipe 설치오류
  ![mperror1](https://github.com/kst0626/CSproject/assets/152972876/a64ab6c4-84f2-462a-8ab0-556036c4e258)
  
  sol1)해당 오류 발생으로 conda가 아닌 코드로 직접 설치시도했으나 아래의 문구가 뜨며 오류발생
  ![mperror2](https://github.com/kst0626/CSproject/assets/152972876/e821a659-4533-4c44-b5bc-85285c0d685d)

  sol2) 아예 새로운 콘다 가상환경(python version 3.9)을 만들고 패키지 설치 중 아래의 문구가 뜨며 오류발생
  ![condaerror1](https://github.com/kst0626/CSproject/assets/152972876/71eb5730-f376-4f64-837e-f8261c6d2b70)
  ![condaerror2](https://github.com/kst0626/CSproject/assets/152972876/2074e1f9-5cf7-465d-963a-368b56ca83ad)
   

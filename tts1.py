import pygame
from gtts import gTTS
import time

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

def main():
    pygame.init()

    # 윈도우 생성 전 초기화
    pygame.display.init()

    # 화면 설정
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Workout Counter')

    # 운동 횟수 초기화
    count = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # 스페이스바를 눌렀을 때 운동 횟수 증가 및 음성 출력
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    count += 1
                    print(f"Current count: {count}")
                    text = f"You have completed {count} reps."
                    filename = "count.mp3"
                    
                    # 텍스트를 음성으로 변환하여 파일로 저장
                    text_to_speech(text, filename)
                    
                    # 저장된 파일 재생
                    play_audio(filename)

        # 화면을 흰색으로 채우고 화면을 업데이트
        screen.fill((255, 255, 255))
        pygame.display.flip()

        # 프로그램이 너무 빨리 종료되지 않도록 대기
        time.sleep(0.1)

    pygame.quit()

if __name__ == "__main__":
    main()

import cv2
import mediapipe as mp
import numpy as np
import threading
from gtts import gTTS
import pygame
import speech_recognition as sr
import os
import time
from playsound import playsound

# Initialize Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Initialize pygame mixer for music control
pygame.mixer.init()

# Function to calculate angle between three points
def calculate_angle(a, b, c):
    a = np.array(a)  # First point
    b = np.array(b)  # Mid point
    c = np.array(c)  # End point
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle

# Function to provide voice feedback using gTTS and playsound
def voice_feedback(message):
    tts = gTTS(text=message, lang='ko')
    filename = "feedback.mp3"
    tts.save(filename)
    
    def play_feedback():
        playsound(filename)  # playsound로 음성 재생
        os.remove(filename)

    threading.Thread(target=play_feedback).start()

# Function to play music using pygame.mixer
def play_music():
    music_file = "/home/jisang20/Desktop/ai_health_care/work_music.mp3"  # 음악 파일 경로
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(0.2)  # 볼륨을 더 낮게 설정 (0.2)
        pygame.mixer.music.play(-1)  # 무한 반복 재생
    else:
        print("Music file not found.")

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Function to recognize user speech commands for music control
def recognize_speech():
    recognizer = sr.Recognizer()
    
    # 음악을 잠시 일시 정지
    pygame.mixer.music.pause()
    
    with sr.Microphone() as source:
        print("음성 인식 중... (음악 재생을 위해 '시작', 음악 중지를 위해 '정지'를 말하세요)")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio, language="ko-KR")
            print(f"인식된 명령어: {command}")
            if "시작" in command:
                threading.Thread(target=play_music).start()
            elif "정지" in command:
                threading.Thread(target=stop_music).start()
        except sr.UnknownValueError:
            print("명령을 인식하지 못했습니다.")
        except sr.RequestError as e:
            print(f"음성 인식 서비스에 문제가 있습니다: {e}")
    
    # 음성 인식이 끝나면 음악 다시 재생
    pygame.mixer.music.unpause()

# Function to periodically check for voice commands
def periodic_speech_recognition():
    while pygame.mixer.music.get_busy():  # 음악이 재생 중일 때
        recognize_speech()  # 음성 인식 시도
        time.sleep(5)  # 5초마다 음성 인식 시도

# Initialize camera feed
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture")
    exit()

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    normal_feedback_given = False  # Add a flag for normal posture feedback
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to capture image")
            break
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # Make detections
        results = holistic.process(image)
        
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Draw landmarks
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Get coordinates for left side
            left_shoulder = [landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y]
            left_hip = [landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].y]
            left_knee = [landmarks[mp_holistic.PoseLandmark.LEFT_KNEE.value].x,
                         landmarks[mp_holistic.PoseLandmark.LEFT_KNEE.value].y]
            
            # Get coordinates for right side
            right_shoulder = [landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].x,
                              landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].y]
            right_hip = [landmarks[mp_holistic.PoseLandmark.RIGHT_HIP.value].x,
                         landmarks[mp_holistic.PoseLandmark.RIGHT_HIP.value].y]
            right_knee = [landmarks[mp_holistic.PoseLandmark.RIGHT_KNEE.value].x,
                          landmarks[mp_holistic.PoseLandmark.RIGHT_KNEE.value].y]
            
            # Calculate angles
            left_angle = calculate_angle(left_shoulder, left_hip, left_knee)
            right_angle = calculate_angle(right_shoulder, right_hip, right_knee)
            
            # Visualize angles
            cv2.putText(image, str(left_angle), 
                        tuple(np.multiply(left_hip, [640, 480]).astype(int)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
            cv2.putText(image, str(right_angle), 
                        tuple(np.multiply(right_hip, [640, 480]).astype(int)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
            # Provide "정상자세입니다" feedback if angle is less than 90 degrees
            if (left_angle < 90 and right_angle < 90) and not normal_feedback_given:
                threading.Thread(target=voice_feedback, args=("정상자세입니다",)).start()
                normal_feedback_given = True
            elif left_angle >= 90 and right_angle >= 90:
                normal_feedback_given = False  # Reset flag when angle is not normal anymore

        except Exception as e:
            print(e)
            pass

        # Display the image
        cv2.imshow('Squat Analysis', image)

        # Check for key press 'm' to start speech recognition for music control
        if cv2.waitKey(10) & 0xFF == ord('m'):
            threading.Thread(target=recognize_speech).start()

        # Check for key press 'p' to start periodic speech recognition
        if cv2.waitKey(10) & 0xFF == ord('p'):
            threading.Thread(target=periodic_speech_recognition).start()

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

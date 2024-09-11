import cv2
import mediapipe as mp
import numpy as np
import threading
from gtts import gTTS
from playsound import playsound
import os

# Initialize Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

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

# Function to provide voice feedback using gTTS
def voice_feedback():
    tts = gTTS(text="허리를 똑바로 피세요", lang='ko')
    filename = "feedback.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# Initialize camera feed
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture")
    exit()

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    feedback_given = False
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
            
            # Get coordinates for left and right shoulders, hips, and knees
            left_shoulder = [landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y]
            left_hip = [landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].y]
            left_knee = [landmarks[mp_holistic.PoseLandmark.LEFT_KNEE.value].x,
                         landmarks[mp_holistic.PoseLandmark.LEFT_KNEE.value].y]
            
            right_shoulder = [landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].x,
                              landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].y]
            right_hip = [landmarks[mp_holistic.PoseLandmark.RIGHT_HIP.value].x,
                         landmarks[mp_holistic.PoseLandmark.RIGHT_HIP.value].y]
            right_knee = [landmarks[mp_holistic.PoseLandmark.RIGHT_KNEE.value].x,
                          landmarks[mp_holistic.PoseLandmark.RIGHT_KNEE.value].y]
            
            # Calculate angles between shoulder, hip, and knee
            left_angle = calculate_angle(left_shoulder, left_hip, left_knee)
            right_angle = calculate_angle(right_shoulder, right_hip, right_knee)
            
            # Calculate back angles (between shoulder and hip)
            left_back_angle = calculate_angle(left_shoulder, left_hip, [left_hip[0], left_hip[1] + 0.1])
            right_back_angle = calculate_angle(right_shoulder, right_hip, [right_hip[0], right_hip[1] + 0.1])
            
            # Visualize angles
            cv2.putText(image, f"Left: {left_back_angle:.2f}", 
                        tuple(np.multiply(left_hip, [640, 480]).astype(int)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
            cv2.putText(image, f"Right: {right_back_angle:.2f}", 
                        tuple(np.multiply(right_hip, [640, 480]).astype(int)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
            # Give feedback if back angle is incorrect (greater than 30 degrees)
            if (left_back_angle > 30 or right_back_angle > 30) and not feedback_given:
                threading.Thread(target=voice_feedback).start()
                feedback_given = True
            elif left_back_angle <= 30 and right_back_angle <= 30:
                feedback_given = False
    
        except Exception as e:
            print(e)
            pass

        # Display the image
        cv2.imshow('Squat Analysis', image)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

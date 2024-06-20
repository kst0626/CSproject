import cv2
import mediapipe as mp
import pyttsx3
import numpy as np
import threading

# Initialize Mediapipe and pyttsx3
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
engine = pyttsx3.init()

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

# Function to provide voice feedback
def voice_feedback():
    engine.say("허리를 똑바로 피세요")
    engine.runAndWait()

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
            
            # Give feedback if angle is incorrect
            if (left_angle < 150 or right_angle < 150) and not feedback_given:
                threading.Thread(target=voice_feedback).start()
                feedback_given = True
            elif left_angle >= 150 and right_angle >= 150:
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

import speech_recognition as sr
from gtts import gTTS
import os

def text_to_speech(text, lang='ko'):
    """텍스트를 음성으로 변환하고 재생"""
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # Windows

def speech_to_text():
    """음성을 텍스트로 변환"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='ko-KR')
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

if __name__ == "__main__":
    while True:
        user_input = speech_to_text()
        if user_input:
            if user_input.lower() == "종료":
                text_to_speech("프로그램을 종료합니다.")
                break
            response = f"당신이 말한 것은: {user_input}"
            text_to_speech(response)

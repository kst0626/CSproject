import json
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS 
import os

# TTS 기능
def text_to_speech(text, lang='ko'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")

# 음성 인식 기능
def speech_to_text():
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

# 운동 스케줄 관리 기능
def save_schedule(schedule):
    with open("schedule.json", "w") as f:
        json.dump(schedule, f, indent=4, ensure_ascii=False)

def load_schedule():
    try:
        with open("schedule.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add_exercise(schedule, exercise, date):
    schedule.append({"exercise": exercise, "date": date})
    save_schedule(schedule)

def view_schedule(schedule):
    if not schedule:
        print("No scheduled exercises.")
        text_to_speech("예약된 운동이 없습니다.")
        return

    for entry in schedule:
        entry_text = f"{entry['date']}: {entry['exercise']}"
        print(entry_text)
        text_to_speech(entry_text)

def remove_exercise(schedule, date):
    new_schedule = [entry for entry in schedule if entry['date'] != date]
    save_schedule(new_schedule)
    return new_schedule

# 메인 함수
def main():
    schedule = load_schedule()

    while True:
        print("\n1. Add Exercise\n2. View Schedule\n3. Remove Exercise\n4. Quit")
        text_to_speech("원하는 작업을 선택하세요: 추가, 조회, 삭제, 종료")
        choice = speech_to_text()

        if choice:
            if "추가" in choice:
                text_to_speech("운동 설명을 말해주세요.")
                exercise = speech_to_text()
                if exercise:
                    text_to_speech("날짜를 말해주세요. 예: 2024년 6월 6일")
                    date = speech_to_text()
                    if date:
                        date = datetime.strptime(date, "%Y년 %m월 %d일").strftime("%Y-%m-%d")
                        add_exercise(schedule, exercise, date)
                        response = f"{date}에 {exercise}가 추가되었습니다."
                        print(response)
                        text_to_speech(response)

            elif "조회" in choice:
                print("Scheduled exercises:")
                view_schedule(schedule)

            elif "삭제" in choice:
                text_to_speech("삭제할 운동의 날짜를 말해주세요. 예: 2024년 6월 6일")
                date = speech_to_text()
                if date:
                    date = datetime.strptime(date, "%Y년 %m월 %d일").strftime("%Y-%m-%d")
                    schedule = remove_exercise(schedule, date)
                    response = f"{date}의 운동이 삭제되었습니다."
                    print(response)
                    text_to_speech(response)

            elif "종료" in choice:
                text_to_speech("프로그램을 종료합니다.")
                break

            else:
                text_to_speech("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()

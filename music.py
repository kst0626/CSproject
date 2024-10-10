import os
import re
import json
import yt_dlp as youtube_dl
import googleapiclient.discovery
from pydub import AudioSegment
from pydub.playback import play

# YouTube API 설정
API_KEY = "AIzaSyDemJ0bUI9tavsl0tQ5sFYTc_lyKwWJ7Pk"
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

def search_music(query):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=5
    )
    response = request.execute()
    videos = response.get('items', [])
    return [(video['id']['videoId'], video['snippet']['title']) for video in videos]

def download_audio(video_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(title)s.%(ext)s',  # 파일 이름 설정
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'https://www.youtube.com/watch?v={video_id}'])

def play_audio(filename):
    try:
        # pydub로 오디오 재생
        print(f"재생 중: {filename}")  # 재생 중인 파일 이름 출력
        audio = AudioSegment.from_mp3(filename)  # MP3 파일 읽기
        play(audio)  # 오디오 재생
    except Exception as e:
        print(f"오디오 재생 중 오류 발생: {e}")

def main():
    while True:
        user_input = input("추천을 원하는 음악 제목이나 가수 이름을 입력하세요 (종료하려면 'exit' 입력): ")
        if user_input.lower() == 'exit':
            break
        
        videos = search_music(user_input)
        
        if not videos:
            print("검색 결과가 없습니다.")
            continue
        
        print("검색된 결과:")
        for index, (video_id, title) in enumerate(videos, start=1):
            print(f"{index}: {title} (ID: {video_id})")

        selected_index = int(input("재생할 음악의 번호를 선택하세요: ")) - 1
        if 0 <= selected_index < len(videos):
            selected_video_id, selected_title = videos[selected_index]
            download_audio(selected_video_id)
            play_audio(f"{selected_title}.mp3")  # 다운로드한 파일을 재생
        else:
            print("잘못된 번호를 선택했습니다.")

if __name__ == "__main__":
    main()

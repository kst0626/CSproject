import requests

def olami_stt(audio_file, api_key):
    url = "https://cn.olami.ai/cloudservice/api"

    headers = {
        "Content-Type": "audio/wav",
        "Authorization": "Bearer " + api_key
    }

    params = {
        "appkey": "YOUR_APP_KEY",
        "api": "asr",
        "timestamp": "1609459288",
        "seq": "abcde12345",
        "sign": "SIGNATURE"
    }

    with open(audio_file, 'rb') as f:
        audio_data = f.read()

    response = requests.post(url, headers=headers, params=params, data=audio_data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to recognize speech."}

# 사용 예시
if __name__ == "__main__":
    audio_file = "your_audio_file.wav"
    api_key = "YOUR_API_KEY"
    result = olami_stt(audio_file, api_key)
    print(result) 

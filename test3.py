import moviepy.editor as mp
import speech_recognition as sr

# 動画ファイルのパス
video_path = "IMG_5531.MOV"
# 出力ファイルのパス
output_text_path = "moji.txt"

# 動画ファイルから音声を抽出
video = mp.VideoFileClip(video_path)
audio = video.audio
audio_path = "temp_audio.wav"
audio.write_audiofile(audio_path)

# 音声ファイルを文字起こし
recognizer = sr.Recognizer()
with sr.AudioFile(audio_path) as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language="ja-JP")
    except sr.UnknownValueError:
        text = "音声を認識できませんでした。"
    except sr.RequestError as e:
        text = f"音声認識サービスにアクセスできませんでした: {e}"

# 文字起こし結果をファイルに保存
with open(output_text_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"文字起こしが完了しました。結果は {output_text_path} に保存されました。")
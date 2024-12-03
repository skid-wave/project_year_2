from pytube import YouTube
from moviepy.editor import AudioFileClip
import speech_recognition as sr
from langdetect import detect
import os

def download_audio(youtube_link):
    try:
        video = YouTube(youtube_link)
        audio_stream = video.streams.filter(only_audio=True).first() 
        if audio_stream is None:
            raise Exception("No audio streams available for this video.")
        audio_file_path = audio_stream.download(filename='audio.mp4')  
        return audio_file_path 
    except Exception as e:
        raise Exception(f"Error downloading audio: {str(e)}")

def convert_audio_to_wav(audio_file_path):
    wav_file_path = 'audio.wav'
    with AudioFileClip(audio_file_path) as audio_clip:
        audio_clip.write_audiofile(wav_file_path, codec='pcm_s16le') 
    return wav_file_path 

def transcribe_audio(wav_file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_file_path) as source:
            audio_data = recognizer.record(source)  
            text = recognizer.recognize_google(audio_data) 
        return text 
    except sr.UnknownValueError:
        raise Exception("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        raise Exception(f"Could not request results from Google Speech Recognition service; {str(e)}")

def detect_language(text):
    return detect(text)

def process_youtube_audio(youtube_link):
    try:
        audio_file_path = download_audio(youtube_link)  
        wav_file_path = convert_audio_to_wav(audio_file_path)  
        transcribed_text = transcribe_audio(wav_file_path) 
        language = detect_language(transcribed_text)  
    finally:
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)  
        if os.path.exists(wav_file_path):
            os.remove(wav_file_path)  
    return transcribed_text, language
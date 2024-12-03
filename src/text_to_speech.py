from gtts import gTTS
import os

def generate_audio(text, language, format='mp3'):
    audio_file = f"static/audio.{format}"  
    tts = gTTS(text=text, lang=language)
    tts.save(audio_file)
    return f"/static/audio.{format}"  

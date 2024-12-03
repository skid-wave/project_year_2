from src.audio_processing import process_youtube_audio
from flask import Flask, render_template, request, jsonify
import logging
from src.get_transcript import get_transcript
from src.summarize import summarize_text
from src.text_to_speech import generate_audio

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        youtube_link = request.json['youtube_link']
        language = request.json['language']

        transcript = get_transcript(youtube_link) 

        if "No transcript found" in transcript:
            logging.warning(transcript)
            transcript, language = process_youtube_audio(youtube_link)  #agar trabscript mila to sumarize karega nahi to exception 
        else:
            # Summarize transcript
            summary = summarize_text(transcript, language)

            # Generate audio
            audio_url = generate_audio(summary, language)

            return jsonify({'summary': summary, 'audioUrl': audio_url})

    except Exception as e:
        logging.error(f"Error in summarize route: {str(e)}")
        return jsonify({'error': 'Failed to process request'}), 500

@app.route('/download_summary', methods=['POST'])
def download_summary():
    summary = request.json['summary']
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)

from transformers import pipeline
from googletrans import Translator
import logging

def summarize_text(transcript, language):
    try:
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        translator = Translator()
        input_length = len(transcript.split())

        max_length = min(150, input_length // 2)
        min_length = min(30, input_length // 4)
        
        if input_length > 1024:
            chunks = [transcript[i:i + 2048] for i in range(0, len(transcript), 2048)]  # Larger chunks
            summaries = []
            for chunk in chunks:
                try:
                    summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
                    summaries.append(summary[0]['summary_text'])
                except Exception as e:
                    logging.error(f"Error summarizing chunk: {str(e)}")
                    summaries.append("Error in summarizing this part.")
            summary = ' '.join(summaries)
        else:
            summary = summarizer(transcript, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']

        if language != 'en':
            summary = translator.translate(summary, dest=language).text

        return summary
    except Exception as e:
        logging.error(f"Error during summarization: {str(e)}")
        return "Error in processing the summary."

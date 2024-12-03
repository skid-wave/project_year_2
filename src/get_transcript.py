from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(youtube_link):
    video_id = youtube_link.split('v=')[1]  
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id) 
        return ' '.join([entry['text'] for entry in transcript])
    except Exception:
        return "No transcript found, making one or extracting one."

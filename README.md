# YouTube Transcript Summarizer

This project summarizes YouTube video transcripts and converts the summary to speech. It supports multiple languages for summarization and audio generation.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/youtube-transcript-summarizer.git
    cd youtube-transcript-summarizer
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Requirements
- Python 3.7 or higher

## Usage

To start the web application, run the following command:

```
python app.py
```

Then, open your web browser and navigate to `http://127.0.0.1:5000/`.

### Example

1. Enter the YouTube video URL in the input field.
2. Select the desired language for summarization.
3. Click the "Summarize" button to generate the summary and audio.

## API Endpoints

### `POST /summarize`

- **Description**: Summarizes the transcript of a YouTube video and generates an audio file.
- **Request Body**:
    ```json
    {
        "youtube_link": "https://www.youtube.com/watch?v=example",
        "language": "en"
    }
    ```
- **Response**:
    ```json
    {
        "summary": "This is the summarized text.",
        "audioUrl": "/static/audio.mp3"
    }
    ```

### Notes
- Ensure you have the necessary permissions to access the YouTube videos.
- The application may require an internet connection to fetch transcripts and generate audio.

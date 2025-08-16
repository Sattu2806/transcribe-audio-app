# Audio Analysis API with HTML Template

This Flask application provides an audio transcription service using Deepgram's AI-powered speech recognition, along with a beautiful HTML interface for testing.

## Features

- 🎵 **Audio Transcription**: Convert audio files to text using Deepgram's Nova-2 model
- 🌐 **Web Interface**: Beautiful, responsive HTML template for easy testing
- 📁 **Multiple Formats**: Supports WAV, MP3, OGG, FLAC, M4A, AAC, OPUS, WEBM
- 🔍 **Smart Analysis**: Includes punctuation, smart formatting, and speaker diarization
- 📱 **Mobile Friendly**: Responsive design that works on all devices

## Setup

### 1. Install Dependencies

```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install flask deepgram-sdk requests
```

### 2. Set Deepgram API Key

Set your Deepgram API key as an environment variable:

```bash
export DEEPGRAM_API_KEY="your-actual-api-key-here"
```

Or create a `.env` file in the flask-backend directory:

```bash
echo "DEEPGRAM_API_KEY=your-actual-api-key-here" > .env
```

### 3. Run the Flask Application

```bash
python app.py
```

The server will start at `http://localhost:5000`

## Usage

### Web Interface

1. Open your browser and go to `http://localhost:5000`
2. Click "Choose Audio File" to select an audio file
3. Click "Analyze Audio" to start transcription
4. View the results including filename and transcription

### API Testing

#### Using the Test Script

```bash
python test_api.py path/to/your/audio/file.mp3
```

#### Using curl

```bash
curl -X POST -F "file=@path/to/your/audio/file.mp3" http://localhost:5000/api/analyse
```

#### Using Python requests

```python
import requests

with open('audio_file.mp3', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:5000/api/analyse', files=files)
    print(response.json())
```

## API Endpoints

### POST /api/analyse

Upload an audio file for transcription.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: Form data with `file` field containing audio file

**Response:**
```json
{
    "message": "File transcribed successfully",
    "filename": "audio_file.mp3",
    "transcription": "This is the transcribed text from the audio file."
}
```

**Error Response:**
```json
{
    "error": "Error message describing what went wrong"
}
```

## Supported Audio Formats

- **WAV** - Waveform Audio File Format
- **MP3** - MPEG Audio Layer III
- **OGG** - Ogg Vorbis
- **FLAC** - Free Lossless Audio Codec
- **M4A** - MPEG-4 Audio
- **AAC** - Advanced Audio Coding
- **OPUS** - Opus Audio Codec
- **WEBM** - WebM Audio

## File Size Considerations

- Larger files will take longer to process
- Consider file compression for very large audio files
- The API processes files in memory, so extremely large files may cause issues

## Troubleshooting

### Common Issues

1. **"No file part in request"**
   - Make sure you're sending the file with the field name `file`

2. **"File type not allowed"**
   - Check that your audio file has one of the supported extensions

3. **"Error transcribing file"**
   - Verify your Deepgram API key is correct
   - Check that the audio file is not corrupted
   - Ensure the file is actually an audio file

4. **Connection errors**
   - Make sure the Flask server is running
   - Check that you're using the correct URL

### Debug Mode

The Flask app runs in debug mode by default. Check the console output for detailed error information.

## Security Notes

- Store your Deepgram API key securely (use environment variables)
- Consider adding authentication for production use
- Validate file types and sizes on the server side
- Implement rate limiting for production deployments

## Next Steps

- Add user authentication
- Implement file storage
- Add batch processing capabilities
- Create user management dashboard
- Add audio preprocessing options

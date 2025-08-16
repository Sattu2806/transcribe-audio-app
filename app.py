from flask import Flask, request, jsonify, render_template
import os
from io import BytesIO
from deepgram import DeepgramClient, PrerecordedOptions
from config import Config

# Initialize Flask app
app = Flask(__name__)

# Deepgram API key (store securely, e.g., in environment variables)
DEEPGRAM_API_KEY = Config.DEEPGRAM_API_KEY

# Allowed audio file extensions
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'ogg', 'flac', 'm4a', 'aac', 'opus', 'webm'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/api/analyse", methods=["POST"])
def analyse():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files['file']
    
    # Check if file is selected
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Validate file extension
    if not allowed_file(file.filename):
        return jsonify({'error': f'File type not allowed. Supported types: {", ".join(ALLOWED_EXTENSIONS)}'}), 400
    
    try:
        #read file into memory
        file_bytes = BytesIO(file.read())
        mimetype = f"audio/{file.filename.rsplit('.', 1)[1].lower()}"

        #initialize deepgram client
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)

        #create options for prerecorded audio
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            punctuate=True,
            diarize=True
        )

        # Prepare audio source
        source = {
            "buffer": file_bytes,
            "mimetype": mimetype
        }

        response = deepgram.listen.rest.v("1").transcribe_file(source, options)
        
        # Extract transcription
        transcription = response['results']['channels'][0]['alternatives'][0]['transcript']
        
        return jsonify({
            'message': 'File transcribed successfully',
            'filename': file.filename,
            'transcription': transcription
        }), 200
    
    except Exception as e:
        return jsonify({'error': f'Error transcribing file: {str(e)}'}), 500
if __name__ == "__main__":
    app.run(debug=True)
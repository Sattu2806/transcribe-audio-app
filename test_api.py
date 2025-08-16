#!/usr/bin/env python3
"""
Simple test script for the Audio Analysis API
"""

import requests
import os
import sys

def test_audio_analysis_api(audio_file_path):
    """
    Test the /api/analyse endpoint with an audio file
    """
    if not os.path.exists(audio_file_path):
        print(f"Error: File {audio_file_path} does not exist")
        return
    
    url = "http://localhost:5000/api/analyse"
    
    try:
        with open(audio_file_path, 'rb') as audio_file:
            files = {'file': audio_file}
            
            print(f"Uploading {audio_file_path} to {url}...")
            response = requests.post(url, files=files)
            
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {dict(response.headers)}")
            
            if response.status_code == 200:
                result = response.json()
                print("\n✅ Success!")
                print(f"Message: {result.get('message')}")
                print(f"Filename: {result.get('filename')}")
                print(f"Transcription: {result.get('transcription')}")
            else:
                print(f"\n❌ Error: {response.status_code}")
                try:
                    error_data = response.json()
                    print(f"Error Message: {error_data.get('error')}")
                except:
                    print(f"Response Text: {response.text}")
                    
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the Flask server is running on http://localhost:5000")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python test_api.py <path_to_audio_file>")
        print("Example: python test_api.py sample_audio.mp3")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    test_audio_analysis_api(audio_file)

if __name__ == "__main__":
    main()

# voicechat
An application that generates voice based off-of the voice supplied by external users through stages ordered in a way: voice-2-text, text-2-text, text-2-voice.


**Summary**
Users can record an audio file (sound input) with this Flask application, and it will convert it to text. Following text processing (Text-to-Text conversion), the application converts the output back to audio (Text-to-Sound conversion). This application shows how text-to-speech and speech recognition may be combined within a Flask framework.

**File Structure**
    flask_app/
      |--_pycache_
      |--static/
          |--CSS/
              |--custom.css
          |--  JS/
              |--script.js
          |--response.wav  
      |--templates/
          |--index.html
      |--uploads/
          |--recorded_audio.wav
      |--app.py
      |--main1.py
      |--main2.py
      |--main3.py
      |--maip_builder.py
      |--maip_client.py
      |--maip_context.py
      |--maip_resolver.py
      


**License**
This project is open-source and available under the MIT License.


import transformers
import time
import librosa
import os
from huggingface_hub import hf_hub_download


def voice_to_text(in_path):

    if not os.path.isfile(in_path):
        raise FileNotFoundError(f"This file {in_path} does not exist.")

    # Example of downloading a file from the Hub
    file_path = hf_hub_download(repo_id="facebook/wav2vec2-base-960h", filename="config.json", force_download=True)


    os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

    device="cpu"


    start_time = time.time()
    #print("Loading audio transcripting model...")
    transcription_model_name = 'facebook/wav2vec2-base-960h'  # Example model for audio transcription
    transcription_model = transformers.pipeline('automatic-speech-recognition', model=transcription_model_name,device=device)
    #print(f"Audio transcripting model loaded in {time.time() - start_time} seconds.")

    try:
    #path = "C:\\Users\\Deren\\Desktop\\AI_Project\\sound1.wav"
        audio, sr = librosa.load(in_path, sr=16000)
        #return audio, sr
    except Exception as e:
        print(f"Error loading audio file: {e}")
        

    #print(f"Audio loaded. Duration: {librosa.get_duration(y=audio, sr=sr)} seconds")
    #print(f"Audio data: {audio[:10]}... (showing first 10 samples)")
    #print(f"Sampling rate: {sr}")
    #print(f"Audio shape: {audio.shape}")
    #print(f"Audio dtype: {audio.dtype}")


    # Convert the audio data to the format expected by the model
    audio_data = {
        'array': audio,
        'sampling_rate': sr
    }


    # Test audio transcription model
    #print("Running audio transcription test...")
    try:
        transcripted_response = transcription_model(audio_data)
        #print("Audio transcription test successful.")
        #print(transcripted_response)
    except Exception as e:
        print(f"Error during audio transcription test: {e}")

    transcripted_text = transcripted_response["text"]
    #print(f"Transcripted text: {transcripted_text}")

    return transcripted_text

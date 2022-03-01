import json
from pathlib import Path
import os
from aiohttp import request
from dotenv import load_dotenv
from pip import main
from google.cloud import speech_v1p1beta1 as speech
import fire
import requests



# 1


##################################################


def get_transcripts_json(gcsPath="https://storage.cloud.google.com/outputdirectory/write_transcription.txt", langCode="ar", speakerCount=1):
    """Transcribes audio files.
    Args:
        gcsPath (String): path to file in cloud storage (i.e. "gs://audio/clip.mp4")
        langCode (String): language code (i.e. "en-US", see https://cloud.google.com/speech-to-text/docs/languages)
        phraseHints (String[]): list of words that are unusual but likely to appear in the audio file.
        speakerCount (int, optional): Number of speakers in the audio. Only works on English. Defaults to None.
        enhancedModel (String, optional): Option to use an enhanced speech model, i.e. "video"
    Returns:
        list | Operation.error
    """

    # Helper function for simplifying Google speech client response
    def _jsonify(result):
        json = []
        for section in result.results:
            data = {
                "transcript": section.alternatives[0].transcript,
                "words": []
            }
            for word in section.alternatives[0].words:
                data["words"].append({
                    "word": word.word,
                    "start_time": word.start_time.total_seconds(),
                    "end_time": word.end_time.total_seconds(),
                    "speaker_tag": word.speaker_tag
                })
            json.append(data)
        return json

    client = speech.SpeechClient()  
    audio = speech.RecognitionAudio(uri=gcsPath)

    diarize = speakerCount if speakerCount > 1 else False
    print(f"Diarizing: {diarize}")
    diarizationConfig = speech.SpeakerDiarizationConfig(
        enable_speaker_diarization=speakerCount if speakerCount > 1 else False,
    )

    config = speech.RecognitionConfig(
        language_code="ar" if langCode == "en" else langCode,
        enable_automatic_punctuation=True,
        enable_word_time_offsets=True,
        diarization_config=diarizationConfig,
    )
    res = client.long_running_recognize(config=config, audio=audio).result()

    return _jsonify(res)





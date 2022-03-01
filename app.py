###IMPORTS###
import os
import shutil
import ffmpeg
import time
import json
import sys
import tempfile
import uuid
from dotenv import load_dotenv
import fire
import html
from pydub import AudioSegment
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import texttospeech
from google.cloud import translate_v2 as translate
from google.cloud import storage
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip, TextClip




from dubapp.01vid_wav import inFile
from dubapp.01vid_wav import outFile
from dubapp.01vid_wav import translatedText
from dubapp.01vid_wav import text
from dubapp.01vid_wav import audio_data
from dubapp.02configure_speech_text import get_transcripts_json
from dubapp.03parse import parse_sentence_with_speaker
from dubapp.04translate import translate_text
from dubapp.05text_to_speech import speak
from dubapp.06transcript_srt import toStr
from dubapp.07stitch_audio import stitch_audio
from data.transcript import transcript 
from data.transcript import translation 




def dub():
    #Get Audio File and Transcription
    
 
    
    
    
    
    
    
    #Configure
    
    
    
    
    #Parse
    
    
    
    
    #Translate
    
    
    
    #Text to Speech
    
    
    
    #Transcribe
    
    
    
    #Pipline
    
    
if __name__ == "__main__":
    fire.Fire(dub)  
    

    
    
Args:
        videoFile (String): 
        
        
        outputDir (String): 
        
        
        
        srcLang (String): "ar"
        
        
        targetLangs (list, optional): "en"
        
        
        
        storageBucket (String, optional): GCS bucket temp storage 
        
        
        phraseHints (list, optional): none
        
        
        dubSrc (bool, optional): 
            
            
            
        speakerCount (int, optional): 
            
            
        voices (dict, optional): 
            
            
        srt (bool, optional): 
            
            
        newDir (bool, optional): 
            
            
        genAudio (bool, optional): 
            
            
        noTranslate (bool, optional):
            



#For general JSON API requests, excluding object uploads, use the following endpoint, replacing PLACEHOLDER with the appropriate values:

https://storage.googleapis.com/storage/v1/PATH_TO_RESOURCE


#For JSON API object uploads, use the following endpoint, replacing PLACEHOLDER with the appropriate values:

https://storage.googleapis.com/upload/storage/v1/b/BUCKET_NAME/o


#For batched requests, use the following endpoint, replacing PLACEHOLDER with the appropriate values

https://storage.googleapis.com/batch/storage/v1/PATH_TO_RESOURCE

#Optionally, for JSON API object downloads, you can use the following endpoint, replacing PLACEHOLDER with the appropriate values:

https://storage.googleapis.com/download/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?alt=media
    

    
    
    
#Encoding !, #, $, &, ', (, ), *, +, ,, /, :, ;, =, ?, @, [, ], and space characters.

#For example, if you send a JSON API GET request for the object named foo??bar in the bucket example-bucket, then your request URI should be:

GET https://storage.googleapis.com/storage/v1/b/example-bucket/o/foo%3f%3fbar
    
    
################################################

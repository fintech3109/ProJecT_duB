from gettext import translation
from js2py import translate_file
from pydub import AudioSegment
from os import path
import moviepy.editor as mp
from google.cloud import speech_v1p1beta1 as speech
import speech_recognition as sr
from google.cloud import translate_v2 as translate
import html
import os
from fnmatch import translate
import fire


# Insert Local Video File Path
inFile = mp.VideoFileClip("/Users/RiceUniversityFinTech./Desktop/DUBB/VideoFileClip.mp4")

# Insert Local Audio File Path
inFile.audio.write_audiofile("/Users/RiceUniversityFinTech./Desktop/DUBB/test2.wav")

# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile("/Users/RiceUniversityFinTech./Desktop/DUBB/test2.wav") as outFile:
    # listen for the data (load audio to memory)
    audio_data = r.record(outFile)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data, language = "ar-PS")
    translatedText = translate(text)
    print(translatedText)
with open("write_transcription.txt","w") as outfile:
    outfile.write(text)

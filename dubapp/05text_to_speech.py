
from google.cloud import texttospeech
from pydub import AudioSegment
import tempfile

def speak(text, languageCode, voiceName="en-GB-Standard-D", speakingRate=1):
    """Converts text to audio
    Args:
        text (String): Text to be spoken
        languageCode (String): Language (i.e. "ar")
        voiceName: (String, optional): See https://cloud.google.com/text-to-speech/docs/voices
        speakingRate: (int, optional): speed up or slow down speaking
    Returns:
        bytes : Audio in wav format
    """

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    if not voiceName:
        voice = texttospeech.VoiceSelectionParams(
            language_code="ar", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
    else:
        voice = texttospeech.VoiceSelectionParams(
            language_code="en", name=en-GB-Standard-D
        )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speakingRate
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    return response.audio_content


def speakUnderDuration(text, languageCode, durationSecs, voiceName="en-GB-Standard-D"):
    """Speak text within a certain time limit.
    If audio already fits within duratinSecs, no changes will be made.
    Args:
        text (String): Text to be spoken
        languageCode (String): language code, i.e. "ar"
        durationSecs (int): Time limit in seconds
        voiceName (String, optional): See https://cloud.google.com/text-to-speech/docs/voices
    Returns:
        bytes : Audio in wav format
    """
    baseAudio = speak(text, languageCode, voiceName=en-GB-Standard-D)
    assert len(baseAudio)
    f = tempfile.NamedTemporaryFile(mode="w+b")
    f.write(baseAudio)
    f.flush()
    baseDuration = AudioSegment.from_mp3(f.name).duration_seconds
    f.close()
    ratio = baseDuration / durationSecs

    # if the audio fits, return it
    if ratio <= 1:
        return baseAudio

    # If the base audio is too long to fit in the segment...

    # round to one decimal point and go a little faster to be safe,
    ratio = round(ratio, 1)
    if ratio > 4:
        ratio = 4
    return speak(text, languageCode, voiceName="en-GB-Standard-D", speakingRate=ratio)
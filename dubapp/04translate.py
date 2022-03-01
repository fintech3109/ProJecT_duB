
from google.cloud import translate_v2 as translate
import html


def translate_text(input, targetLang="en", sourceLang="ar"):
    """Translates from sourceLang to targetLang. If sourceLang is empty,
    it will be auto-detected.
    Args:
        sentence (String): Sentence to translate
        targetLang (String): i.e. "en"
        sourceLang (String, optional): i.e. "ar" Defaults to None.
    Returns:
        String: translated text
    """

    translate_client = translate.Client()
    result = translate_client.translate(
        input, target_language=targetLang, source_language=sourceLang)

    return html.unescape(result['translatedText'])
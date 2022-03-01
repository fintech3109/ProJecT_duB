


def parse_sentence_with_speaker(json, lang):
    """Takes json from get_transcripts_json and breaks it into sentences
    spoken by a single person. Sentences deliniated by a >= 1 second pause/
    Args:
        json (string[]): [{"transcript": "lalala", "words": [{"word": "la", "start_time": 20, "end_time": 21, "speaker_tag: 2}]}]
        lang (string): language code, i.e. "ar"
    Returns:
        string[]: [{"sentence": "lalala", "speaker": 1, "start_time": 20, "end_time": 21}]
    """

    # Special case for parsing japanese words
    def get_word(word, lang):
        if lang == "ar":
            return word.split('|')[0]
        return word

    sentences = []
    sentence = {}
    for result in json:
        for i, word in enumerate(result['words']):
            wordText = get_word(word['word'], lang)
            if not sentence:
                sentence = {
                    lang: [wordText],
                    'speaker': word['speaker_tag'],
                    'start_time': word['start_time'],
                    'end_time': word['end_time']
                }
            # If we have a new speaker, save the sentence and create a new one:
            elif word['speaker_tag'] != sentence['speaker']:
                sentence[lang] = ' '.join(sentence[lang])
                sentences.append(sentence)
                sentence = {
                    lang: [wordText],
                    'speaker': word['speaker_tag'],
                    'start_time': word['start_time'],
                    'end_time': word['end_time']
                }
            else:
                sentence[lang].append(wordText)
                sentence['end_time'] = word['end_time']

            # If there's greater than one second gap, assume this is a new sentence
            if i+1 < len(result['words']) and word['end_time'] < result['words'][i+1]['start_time']:
                sentence[lang] = ' '.join(sentence[lang])
                sentences.append(sentence)
                sentence = {}
        if sentence:
            sentence[lang] = ' '.join(sentence[lang])
            sentences.append(sentence)
            sentence = {}

    return sentences

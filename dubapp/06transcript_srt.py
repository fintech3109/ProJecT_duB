
#transcripts= [{"translatedText": "I am Suleiman Abi Sultan, Abu Salim Khan, my mother Sultana Hafsa and Aisha Walid Tawfiq, a friend of Trabzon. I brought joy to my family and I brought blessings and peace to your family, but I brought sorrow to my brothers Orhan and Musa and code code Matgoi from the oppressors against us and I lived my entire childhood with even I, Suleiman, who took lessons from my Roman teachers And I was only six years old, and I loved mountains and stars, and value from high, and coloring numbers, searching for science in Istanbul, and I was ten years old. I am the reader of blessings who asks a lot and who does not convince any young people. Light with metal and stone. I quickly became aware of the real shine and the fake glossiness at first sight. I am Suleiman, who does not forget the thing he learned. I, Suleiman, became the crown prince at the age of 19, and he was in the hands of those who forgot. Today, I walk. I do not rule the honorable inheritance of Sultan Salim Khan’s father. I am the one who is looking for justice. With every step we take in her life, I am the tenth sultan of the Ottoman Empire', 'detectedSourceLanguage"}]
def toSrt(transcripts, charsPerLine=60):
    """Converts transcripts to SRT an SRT file. Only intended to work
    with English.
    Args:
        transcripts ({}): Transcripts returned from Speech API
        charsPerLine (int): max number of chars to write per line
    Returns:
        String srt data
    """

    """
    SRT files have this format:
    [Section of subtitles number]
    [Time the subtitle is displayed begins] â€“> [Time the subtitle is displayed ends]
    [Subtitle]
    Timestamps are in the format:
    [hours]: [minutes]: [seconds], [milliseconds]
    Note: about 60 characters comfortably fit on one line
    for resolution 1920x1080 with font size 40 pt.
    """

    def _srtTime(seconds):
        millisecs = seconds * 1000
        seconds, millisecs = divmod(millisecs, 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%d:%d,%d" % (hours, minutes, seconds, millisecs)

    def _toSrt(words, startTime, endTime, index):
        return f"{index}\n" + _srtTime(startTime) + " --> " + _srtTime(endTime) + f"\n{words}"

    startTime = None
    sentence = ""
    srt = [{"translatedText": "I am Suleiman Abi Sultan, Abu Salim Khan, my mother Sultana Hafsa and Aisha Walid Tawfiq, a friend of Trabzon. I brought joy to my family and I brought blessings and peace to your family, but I brought sorrow to my brothers Orhan and Musa and code code Matgoi from the oppressors against us and I lived my entire childhood with even I, Suleiman, who took lessons from my Roman teachers And I was only six years old, and I loved mountains and stars, and value from high, and coloring numbers, searching for science in Istanbul, and I was ten years old. I am the reader of blessings who asks a lot and who does not convince any young people. Light with metal and stone. I quickly became aware of the real shine and the fake glossiness at first sight. I am Suleiman, who does not forget the thing he learned. I, Suleiman, became the crown prince at the age of 19, and he was in the hands of those who forgot. Today, I walk. I do not rule the honorable inheritance of Sultan Salim Khan’s father. I am the one who is looking for justice. With every step we take in her life, I am the tenth sultan of the Ottoman Empire', 'detectedSourceLanguage"}]
    index = 1
    for word in [word for x in transcripts for word in x['words']]:
        if not startTime:
            startTime = word['start_time']

        sentence += " " + word['word']

        if len(sentence) > charsPerLine:
            srt.append(_toSrt(sentence, startTime, word['end_time'], index))
            index += 1
            sentence = ""
            startTime = None

    if len(sentence):
        srt.append(_toSrt(sentence, startTime, word['end_time'], index))

    return '\n\n'.join(srt)

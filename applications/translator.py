from textblob import TextBlob


def translator_en(word):
    blob = TextBlob(word)
    return blob.translate(to='en')


def translator_ru(word):
    blob = TextBlob(word)
    return blob.translate(to='ru')

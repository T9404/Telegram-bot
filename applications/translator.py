# pip install  textblob
from textblob import TextBlob


def translator_en(word):
    blob = TextBlob(word)
    return blob.translate(to='en')


def translator_ru(word):
    blob = TextBlob(word)
    return blob.translate(to='ru')

#print(translator_en('привет'))
#print(translator_ru('Hello'))
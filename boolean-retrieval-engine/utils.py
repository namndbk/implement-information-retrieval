import re
import string

from underthesea import word_tokenize


def remove_duplicate(text):
    text = re.sub(r"([A-Za-z])\1+", lambda m: m.group(1),text)
    return text


def get_stop_words(path):
    stop_words = set([])
    with open(path, encoding="utf-8") as f:
        for line in f:
            stop_words.add(line.lower().strip())
    return stop_words


def normalize(text):
    text = text.lower()
    text = text.replace("\n", " ")
    text = remove_duplicate(text)
    return text


stop_words = get_stop_words("stopwords.txt")
def get_words(text):
    text = normalize(text)
    text = word_tokenize(text)
    words = [word.replace(" ", "_") for word in text if word not in stop_words and " " in word]
    return words
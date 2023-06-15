import requests
from bs4 import BeautifulSoup
import re

def get_english_words(url):
    # get html page
    r = requests.get(url)
    # create soup object
    soup = BeautifulSoup(r.content, 'html.parser')
    # get all text in page in unicode line
    text = soup.get_text()
    # find only eglish words
    english_words = re.findall(r'\b([a-zA-Z]+)\b', text)
    # make unique list with lower words
    return_case = []
    for index,word in enumerate(english_words):
        word = word.lower()
        if len(word) == 1:
            continue
        if word not in return_case:
            return_case.append(word)
    return return_case
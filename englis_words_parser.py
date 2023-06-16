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
    prepositions = ['about', 'above', 'across', 'after', 'against', 'along', 'among', 'around', 'at', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond', 'but', 'by', 'concerning', 'considering', 'despite', 'down', 'during', 'except', 'for', 'from', 'in', 'inside', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'outside', 'over', 'past', 'regarding', 'round', 'since', 'through', 'throughout', 'till', 'to', 'toward', 'under', 'underneath', 'until', 'up', 'upon', 'with', 'within', 'without']
    english_words = [word.lower() for word in english_words if word.lower() not in prepositions and len(word) > 2]
    return set(english_words)

print(get_english_words("https://stackoverflow.com/questions/69593352/how-to-get-all-copyable-text-from-a-web-page-python"))
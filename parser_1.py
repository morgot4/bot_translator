import requests
import re
from bs4 import BeautifulSoup
import string

def get_words(url):
    try:
        # get html page
        req = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(req.text, 'html.parser')
        # select text from all paragraphs
        paragraphs = soup.find_all('p')
        # select text from all heads
        for i in range(1,4):
            paragraphs.extend(soup.find_all(f'h{i}'))
        # select text from all a blocks 
        paragraphs.extend(soup.find_all('a'))
        # select text from all div blocks 
        paragraphs.extend(soup.find_all('div'))

        # create one list for words
        for par in paragraphs:
            try:
                text = par.text.split(' ')
                for index_word,word in enumerate(text): 
                    word = list(word)
                    for index_symbol, symbol in enumerate(word):
                        if symbol.lower() not in string.ascii_lowercase:
                            if len(word) == 0:
                                text.pop(index_word)
                            word.pop(index_symbol)
                    word = "".join(word)
                    print(word)

            except Exception:
                continue
        # clear list
        uniq_words_list = []
        
    except Exception as e:
        print(e)
        



get_words("https://www.google.com/search?q=Please+ensure+JavaScript+is+enabled.&oq=Please+ensure+JavaScript+is+enabled.&aqs=chrome..69i57j0i512j0i22i30l4j0i390i650l4.663j0j7&sourceid=chrome&ie=UTF-8")
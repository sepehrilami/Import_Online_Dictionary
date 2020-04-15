import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.vocabulary.com/lists/172112')

if resp.status_code == 200:
    print("connected successfully")
    word_list = BeautifulSoup(resp.text, 'html.parser').find("ol", {"id": "wordlist"})
    print("list fetched:")

    dictionary = {}
    words = list(map(lambda x: x.text, word_list.findAll("a")))
    definitions = list(map(lambda x: x.text, word_list.findAll("div", {"class": "definition"})))
    for i in range(len(words)):
        dictionary[words[i]] = definitions[i]
    for word in dictionary:
        print(f'{word:20}: {dictionary[word]}')
else:
    print(f'{resp.status_code} Error!')
    
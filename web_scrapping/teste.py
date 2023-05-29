import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

URL = 'https://www.superprof.com.br/blog/aprendendo-coreografias-de-festejos-juninos/'

def filter_visible_elements(element):
    nao_quero = ['style', 'script', 'head', 'title', 'meta', '[document]']
    if element.parent.name in nao_quero:
        return False
    if isinstance(element, Comment):  # Tira o texto que está dentro de comentários
        return False
    return True
def extract_visible_text(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    visible_texts = (text.strip()
                        for text in soup.find_all(string=filter_visible_elements))
    return " ".join(visible_texts)
print(extract_visible_text(URL))

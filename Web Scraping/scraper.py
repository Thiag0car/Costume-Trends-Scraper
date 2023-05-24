import re
import string

import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

# Read the contents of the readme.md file
with open('Web Scraping/Websites.md', 'r') as file:
    sites = file.read()

# Find all HTTPS URLs using regular expressions
urls = re.findall(r'https://[^\s]+', sites)

# Ver apenas texto visível
def is_visible(element):
    # Tira o texto que está dentro dessas tags, CSS, JavaScript, etc
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):  # Tira o texto que está dentro de comentários
        return False
    return True

# Extrair texto visível
def extract_visible_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    visible_texts = (text.strip() for text in soup.find_all(string=is_visible))
    return " ".join(visible_texts)


# Junta todos os resultados
#textos = []
#for url in urls:
#    texto = extract_visible_text(url)
#    textos.append(result)
#
#print(textos)

# Roda site a site
url = 'https://www.receiteria.com.br/receitas-de-festa-junina/#01'

texto = extract_visible_text(url)

print(texto)
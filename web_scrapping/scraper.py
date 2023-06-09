import csv
import os
import re
import string

import requests
from bs4 import BeautifulSoup
from bs4.element import Comment


def pegar_sites(arquivo):
    with open(f'web_scrapping/{arquivo}.md', 'r') as file:
        websites = file.read()
    return websites


def extrair_urls(arquivo):
    pattern = r'\((.*?)\)'
    urls = re.findall(pattern, pegar_sites(arquivo))
    return urls


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


def teste_um_site(url):
    texto = extract_visible_text(url)
    print(texto)


def extract_links_from_pages():
    urls = extrair_urls('blogs')
    todos_links = []
    for url in urls:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [
            link.get('href')
            for link in soup.find_all('a')
            if link and link.get('href', '').startswith('https://')
            and not link.get('href', '').endswith('.pdf')
            and 'facebook' not in link.get('href', '')
            and 'instagram' not in link.get('href', '')
            and 'youtube' not in link.get('href', '')
            and 'twitter' not in link.get('href', '')
            and 'pinterest' not in link.get('href', '')
            and 'google' not in link.get('href', '')
            and 'linkedin' not in link.get('href', '')
            and 'itunes' not in link.get('href', '')
            and 'tiktok' not in link.get('href', '')
        ]
        todos_links.extend(links)
    todos_links = list(set(todos_links)) # Remove duplicados
    return todos_links


def scrape_websites():
    urls = extrair_urls('artigos')
    links = extract_links_from_pages()
    urls.extend(links)
    arquivo_path = 'web_scrapping/dados_sites.csv'

    if os.path.exists(arquivo_path):
        os.remove(arquivo_path)

    with open(arquivo_path, "w", encoding="utf-8", newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(['url', 'texto'])
        for url in urls:
            print(url)
            texto = extract_visible_text(url)
            texto_limpo = texto.strip()
            texto_quebrado = texto_limpo.replace('\n', '\n\n')
            writer.writerow([url, texto_quebrado])


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
           'AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/75.0.3770.80 Safari/537.36'}

scrape_websites()

# Costume-Trends-Scraper


# 1. Objetivo de Negócio:
Nós somos uma empresa de aluguel de roupas e fantasias que está se preparando para o próximo grande evento , as festas juninas. Como parte da equipe de marketing, estamos conduzindo um estudo abrangente sobre esse tema. Para isso, estamos empregando técnicas de web scraping para identificar as palavras-chave mais relevantes associadas ao nosso negócio.

Com base nessa análise, nossa intenção é selecionar cuidadosamente 20 sites nos quais podemos anunciar nossos produtos. Para determinar sua adequação, consideraremos o conteúdo desses websites. Se o conteúdo estiver relacionado às palavras-chave relevantes para nossos produtos, consideraremos esses sites como parceiros ideais para nossos anúncios.

Essa abordagem nos permitirá direcionar nossa publicidade de forma estratégica, alcançando um público engajado e interessado em nossos produtos de aluguel de roupas e fantasias para as festas juninas.

![transferir](https://github.com/Thiag0car/Costume-Trends-Scraper/assets/88406808/791277c4-2f1e-4cce-b215-63c20906b7d0)

# 2. Estrutura do Projeto

![estrutura](https://github.com/Thiag0car/Costume-Trends-Scraper/assets/88406808/9a525eff-4530-4ac8-ac6b-a0fe727ecb6e)

(1) A primeira etapa do nosso projeto consiste em identificar comunidades relacionadas aos nossos produtos. Para alcançar esse objetivo, utilizamos as redes sociais como uma ferramenta fundamental. Nesse sentido, optamos por utilizar a plataforma Brand24, que nos permite coletar e centralizar publicações de diversas redes sociais, baseando-se em hashtags e palavras-chave relevantes para o nosso negócio. Com o auxílio do Brand24, conseguimos obter um amplo panorama das discussões e interações relacionadas aos nossos produtos nas redes sociais mais populares, como TikTok, Twitter, YouTube, entre outros sites relevantes.

(2) Definimos uma quantidade de palavras relacionadas às festas juninas com base na frequência com que essas palavras aparecem nas Redes Sociais, o que serviu para validar os sites escolhidos mais para frente.

(3) Nessa etapa, os integrantes do grupo selecionam cuidadosamente os sites que podem estar relacionados ao nosso produto. As palavras selecionadas das redes sociais desempenham um papel importante na validação desses sites, analisando a semelhança entre as palavras encontradas nos sites e aquelas extraídas das redes sociais. Essa comparação nos permite determinar se um site é adequado para receber a estratégia de marketing do nosso produto, levando em consideração a relevância e a conexão entre as palavras-chave utilizadas nos sites e aquelas identificadas nas redes sociais.

(4) Após essa validação, o grupo seleciona os 10 sites mais relacionados com nosso produto para fazer os anúncios.

(5) (Desafio - 7) A análise de sentimento é utilizada para identificar quais palavras são citadas em contextos negativos. O Brand24 disponibiliza ferramentas que ajudam nessa análise.

(6) (Desafio - 6) A análise de bigramas básicamente serve para visualizar quais palavras aparecem frequentemente juntas, sendo assim revelando combinações comuns de palavras (ou palavras compostas) e fornece insights sobre a estrutura do texto e o contexto das palavras

# 3. Scraping das Redes Sociais

<img align="right" src="img/redes.png" width="50%" >
Para realizar o scraping, utilizamos o site Brand24, No entanto, é importante mencionar que o site nos permite utilizar apenas 10 palavras-chave para iniciar a busca:

* #festajunina
* festa junina
* camisa xadrez
* pamonha
* curau de milho
* quentão
* dança de quadrilha
* #saojoao
* sao joao

O site centraliza publicações de várias redes sociais e sites com base em hashtags e palavras-chave. Essa plataforma nos possibilitou coletar postagens do TikTok, Twitter, YouTube e outros sites relevantes.

https://brand24.com/?adgr=txt-brand-iv-test&keyword-ext=brand24&placement&location=1001773&gclid=CjwKCAjwscGjBhAXEiwAswQqNBPItdcSr7XQ-DUsb5mc4mPX5cLbRrXg0XrBNKEjvaHYvf9VXVKcaxoCfz0QAvD_BwE

Essas palavras-chave nos ajudarão a identificar o conteúdo mais relevante relacionado com nosso produto, e com isso usaremos as palavras coletadas das redes sociais para validar quais sites são apropriados para nossos anúncios

## 3.1 Análise de citações no Mês de junho e fim de maio

<img align="left" src="img/frequencia_citações.png" width="50%" >

A análise de frequência por dia nos permite visualizar quando as citações começam a aumentar e, portanto, em que época do ano devemos começar a investir em marketing do nosso produto. Isso é especialmente importante, uma vez que nosso produto é sazonal, e investir nas horas erradas pode causar prejuízos.

Através de análises feitas nosso grupo concluiu que dia 20/5 é um bom dia para começar investimentos, visto que é quando as cirações começam a aumentar de forma mais consideravel. Não esta ilustrado, mas nosso grupo também coletou uma amostra de dados entre dia 17/5 até dia 26/5 o que ajudou nessa conclusão


## 3.2 Resultado WordCloud das redes:
<img align="Center" src="img/wordcloud_redes.png" width="100%" >

As palavras que foram escolhidas para validar estão nessa tabela a esquerda, nós escolhemos a dedo qual delas nos iriamos utilizar.



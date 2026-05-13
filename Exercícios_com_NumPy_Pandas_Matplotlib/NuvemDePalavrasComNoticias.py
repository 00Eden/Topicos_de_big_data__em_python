import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# URL da notícia
url = "https://g1.globo.com/"

# Pegando conteúdo da página
resposta = requests.get(url)

# Fazendo parse do HTML
soup = BeautifulSoup(resposta.text, "html.parser")

# Extraindo textos
textos = soup.get_text()

# Limpando texto
textos = textos.lower()

textos = re.sub(r'\d+', '', textos)
textos = re.sub(r'[^\w\s]', '', textos)

# Stopwords simples
stopwords = {
    'de', 'da', 'do', 'das', 'dos',
    'a', 'o', 'e', 'para', 'com',
    'em', 'um', 'uma', 'no', 'na',
    'os', 'as', 'que'
}

palavras = textos.split()

palavras_filtradas = [
    palavra for palavra in palavras
    if palavra not in stopwords
]

texto_final = " ".join(palavras_filtradas)

# Criando nuvem de palavras
nuvem = WordCloud(
    width=800,
    height=400,
    background_color='white'
).generate(texto_final)

# Exibindo
plt.figure(figsize=(12, 6))
plt.imshow(nuvem, interpolation='bilinear')
plt.axis('off')
plt.title('Nuvem de Palavras das Notícias')
plt.show()

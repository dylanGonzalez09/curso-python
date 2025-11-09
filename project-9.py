# web scrapping

import bs4
import requests

content = requests.get('https://escueladirecta-blog.blogspot.com/2024/07/copia-o-referencia.html')

sopa = bs4.BeautifulSoup(content.text, 'lxml')
resultado_texto = sopa.select('h3')[3].getText()
imagen = sopa.select('img')[0]['src']
imagen_content = requests.get(imagen) # imagen en binario
f = open('mi_imagen.jpg', 'wb')
f.write(imagen_content.content)
f.close()
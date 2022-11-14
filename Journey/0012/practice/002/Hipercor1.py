import requests
from bs4 import BeautifulSoup as bs


url = ('https://www.hipercor.es/supermercado/buscar/1/?term=pollo&search=text')
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = bs(page.content, 'html.parser')

containers = soup.find_all('div',class_="grid-item")
len(containers)

containers[1].find_all('a',class_='link event js-product-link')[0].text
containers[1].find_all('div',class_='prices-price _current')[0].text
containers[1].find_all('div',class_='prices-price _pum')[0].text

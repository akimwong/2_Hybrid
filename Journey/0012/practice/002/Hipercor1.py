import requests
from bs4 import BeautifulSoup as bs

url = ('https://www.hipercor.es/supermercado/buscar/1/?term=pollo&search=text')
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = bs(page.content, 'html.parser')

'''
container variable is used because not all products have loaded the information in the 3 values
'''
containers = soup.find_all('div',class_="grid-item")
len(containers)
# 24
containers[1].find_all('a',class_='link event js-product-link')[0].text
#'GRAN CUK pollo Gran Cuk criado con alimentación vegetal pechuga entera bandeja 450 g peso aproximado '
containers[1].find_all('div',class_='prices-price _current')[0].text
#'5,69 €'
'''
It is not developed yet the code to create the dataset because ''prices-price _pum' does not exist for all products
'''
containers[1].find_all('div',class_='prices-price _pum')[0].text
#'(12,65 € / Kg)'

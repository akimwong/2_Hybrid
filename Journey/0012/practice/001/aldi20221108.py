import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import re

url = 'https://www.aldi.es/ofertas.html#2022-11-02'
page = requests.get(url)
soup = bs(page.content, 'html.parser')

containers = soup.find_all('div',class_="mod-article-tile")

ProdName = []
UnitPrice = []
PcUnit = []
brand = []
priceBase = []

for x in range(len(containers)):
    ProdName.append(containers[x].find_all('a')[0].text)      # 'Seta cardo'
    for m in containers[x].find_all('span',class_='price__wrapper'):
        UnitPrice.append(re.sub('[\n\t]','',m.contents[0]))
    for n in containers[x].find_all('span',class_='price__unit'):
        PcUnit.append(re.sub('[\n\t]','',n.contents[0]))
    for o in containers[x].find_all('span',class_='mod-article-tile__brand'):
        brand.append(re.sub('[\n\t]','',o.contents[0]))           
    if containers[x].find_all('span',class_='price__base') == []:
        priceBase.append(None)
    else:
        for p in containers[x].find_all('span',class_='price__base'):
                priceBase.append(p.contents[0] if not None else 0)

df = pd.DataFrame({'Products':ProdName,'Brand':brand,
                   'Qty/Unit':PcUnit,'UnitPrice': UnitPrice,
                   'PriceBase':priceBase}, 
                  index = list(range(1,len(ProdName)+1)))

df.to_excel(r'C:\Users\Carlos\0_Hybrid\food\aldiSavings20221108.xlsx', index = False)

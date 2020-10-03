import pandas as pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.flipkart.com/search?q=poco%20x2&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
products = []
price = []
for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'})
    rate = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    products.append(name.text)
    price.append(rate.text)

df = pd.DataFrame({'Product Name': products, 'Price': price})
df.to_csv('products.csv', index=False, encoding='utf-8')

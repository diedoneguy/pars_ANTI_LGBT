import re
from tkinter import HORIZONTAL
import requests
from bs4 import BeautifulSoup

HOST = 'https://ostore.kg/'
URL = 'https://ostore.kg/phones/xiaomi/'

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
def get_html(url,params=''):
    r = requests.get(url,headers=HEADERS,params=params,verify=False)
    return r
def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_="item product sku")
    apar = []
    for item in items:
        apar.append({
            'title':item.find('span',class_="middle").get_text(strip=True),
            'price':item.find('a',class_="price").get_text(strip=True),
            'image':item.find('div',class_="tabloid").find('img').get('src')
        })
    return apar

html = get_html(URL)
file = open('Ostore.csv','a')
file.write(f'{get_content(html.text)}\n')
print(get_content(html.text))
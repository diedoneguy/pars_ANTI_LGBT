import requests
from bs4 import BeautifulSoup

HOST = 'https://www.sulpak.kg/'
URL = 'https://www.sulpak.kg/f/smartfoniy'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
def get_html(url,params=''):
    r = requests.get(url,headers=HEADERS,params=params,verify=False)
    return r
def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    telephons = soup.find_all('div',class_="goods-tiles")
    mobiles = []
    for telephon in telephons:
        mobiles.append({
            'title':telephon.find('div',class_="product-container-right-side").find('a').get_text(strip=True),
            'price':telephon.find('div',class_="price").get_text(strip=True)  
        })
    return mobiles
html = get_html(URL)
file = open('mobile.txt','a')
file.write(f'{get_content(html.text)}\n')
print(get_content(html.text))

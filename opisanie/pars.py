import requests
from bs4 import BeautifulSoup
HOST = 'https://www.sulpak.kg/'
URL = 'https://www.sulpak.kg/f/planshetiy'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
def get_html(url,params=''):
    r = requests.get(url,headers=HEADERS,params=params,verify=False)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_="goods-tiles")
    camera = []

    for item in items:
        camera.append({
                'title':item.find('div',class_="product-container-right-side").find('h3').get_text(strip=True),
                'price':item.find('div',class_="price").get_text(strip=True)
        })
    return camera

html = get_html(URL)
file = open('planshet.csv','a')
file.write(str(f'{get_content(html.text)}'))
print(get_content(html.text))





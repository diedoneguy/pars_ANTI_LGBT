import requests
from bs4 import BeautifulSoup

HOST = 'https://lalafo.kg/'
URL = 'https://lalafo.kg/krasnaya-rechka/ads/mercedes-benz-320-32-l-1995-g-263290-km-id-101395702?with_offset=true'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
def get_html(url,params=''):
    r = requests.get(url,headers=HEADERS,params=params,verify=False)
    return r

def get_content(html):
    while True:
        soup = BeautifulSoup(html,'html.parser')
        items = soup.find_all('article',class_="adTile-wrap")
        base = []
        for item in items:
            base.append({
                'title':item.find('div',class_="adTile-title__wrap").get_text(strip=True),
               
        })
        return base
html = get_html(URL)
file = open('lalafo.csv','a')
file.write(f'{get_content(html.text)}\n')
print(get_content(html.text))

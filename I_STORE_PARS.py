from email.header import Header
import requests
from bs4 import BeautifulSoup

HEADERS = 'https://www.istore.kg/'
URL = 'https://www.istore.kg/catalog/mac/pro-16'

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
def get_html(url,params=''):
    r = requests.get(url,headers=HEADERS,params=params,verify=False)
    return r
def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_="col-lg-3 col-md-4 col-sm-6 col-12 mt-lg-4 mt-2 recommend-card d-flex flex-column p-4")
    nouts = []
    for item in items:
        nouts.append({
            'name':item.find('div',class_="card-body bg-none text-center h-auto").find('h5').get_text(strip=True),
            'info':item.find('div',class_="short-description").get_text(strip=True)
        })
    return nouts
html = get_html(URL)
file = open('istore.csv','a')
file.write(f'{get_content(html.text)}\n')
print(get_content(html.text))


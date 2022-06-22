import requests
from bs4 import BeautifulSoup

HOST='https://ostore.kg/'
URL='https://ostore.kg/phones/tecno/'

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
    fol = []
    for item in items:
        fol.append({
            'folowers':item.find('span',class_="middle").get_text(strip=True),
            'price':item.find('a',class_="price").get_text(strip=True),
            'image':item.find('div',class_="tabloid").find('img').get('src')
        })
    return fol
def save(items, path):
    """ Сохранение данных """
    with open(path, 'w') as file:
        for num, item in enumerate(items,1):
            file.write(f"№ {num} - Название {item['title']}\n")
            file.write(f"№ {num} - Ссылка на фото {item['image']}\n")

html = get_html(URL)
file = open('folowers.csv','a')
file.write(f'{get_content(html.text)}\n')
print(get_content(html.text))

##############################################

def get_content(html):
    """ Сортировка полученных данных """
    soup = BeautifulSoup(html, 'html.parser')
    """ soup нам дает все div классы с заданным названием """
    items = soup.find_all('div', class_='item product_listbox oh')
    new_list = []
    for item in items:
        new_list.append({
            'title': item.find('div', class_='product_text pull-left').find('div', class_='listbox_title oh').find('a').get_text(strip=True),
            'image': HOST + item.find('div', class_='listbox_img pull-left').find('img').get('src')
        }) 
    return new_list


def save(items, path):
    """ Сохранение данных """
    with open(path, 'w') as file:
        for num, item in enumerate(items,1):
            file.write(f"№ {num} - Название {item['title']}\n")
            file.write(f"№ {num} - Ссылка на фото {item['image']}\n")


def parser():
    page = int(input("Введите количество страниц: "))
    html = get_html(URL)
    
    if html.status_code == 200:
        new_list = []
        for pg in range(1, page+1):
            html = get_html(URL, params={'page': pg})

            new_list.extend(get_content(html.text))
            print(f'Страница {pg} готово!')

        save(new_list, 'kivano_noutbuki.txt')
        print('Парсинг прошел успешно')
    else:
        print('Не удалось достучатся до сайта')


parser()
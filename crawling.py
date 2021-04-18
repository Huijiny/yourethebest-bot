import requests
from bs4 import BeautifulSoup

queries = ['자신감', '도전', '희망', '노력', '인생', '성공', '공부']
sayings_file = open("sayings.txt", 'w') 

for query in queries:
    url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}+명언'
    response = requests.get(url).text

    data = BeautifulSoup(response, "html.parser")

    fm_sayings = data.select('div.api_cs_wrap._famous_saying > div.cnt_box > ul > li > div > div > p.lngkr')
    fm_people= data.select('div.api_cs_wrap._famous_saying > div.cnt_box > ul > li > div > dl > dt > a')

    for i in range(10):
        saying = f'{fm_people[i].get_text()} -{fm_sayings[i].get_text()}\n'
        sayings_file.write(saying)

sayings_file.close()
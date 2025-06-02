import csv
from bs4 import *
import requests


# a=requests.get('https://rostov.rbc.ru/')
# print(a) 200

def get_html(url):
    row = requests.get(url)
    return row.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('span', class_='main__feed__title-wrap')
    for el in elements:
        link = el.find('span',class_='main__feed__title').text.strip().split(',')
        data = {
            'lnk': link,
        }
        write_data(data)


def write_data(data):
    with open('datanews.csv', 'a', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\r')
        writer.writerow(data['lnk'])


def runner():
    url = 'https://rostov.rbc.ru/'
    get_data(get_html(url))

if __name__=='__main__':
    runner()
# import csv
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     row = requests.get(url)
#     return row.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("li", class_="wp-block-post")
#     for el in elements:
#         name = el.find("h3").text
#         url = el.find("h3").find("a").get("href")
#         snippet = el.find("div", class_="entry-excerpt").text.strip()
#         active = el.find("span", class_="active-installs").text.strip()
#         tested = el.find("span", class_="tested-with").text.strip()
#         test = refine_cy(tested)
#         data = {
#             "name": name,
#             "url": url,
#             "snippet": snippet,
#             "active": active,
#             "test": test
#         }
#         write_csv(data)
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a", encoding="utf-8-sig") as f:
#         writer = csv.writer(f, delimiter=",", lineterminator="\r")
#         writer.writerow((data["name"], data["url"], data["snippet"], data["active"], data["test"]))
#
#
# def main():
#     for i in range(3, 23):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

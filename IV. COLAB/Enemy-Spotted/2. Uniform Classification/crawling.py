from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as BS
from selenium import webdriver
import os
# reference: https://sf-jam.tistory.com/85


def crawling(keyword):
    i_URL = f'https://www.google.com/search?q={quote_plus(keyword)}&sxsrf=ALeKk00OQamJ34t56QSInnMzwcC5gC344w:1594968011157&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjXs-7t1tPqAhVF7GEKHfM4DqsQ_AUoAXoECBoQAw&biw=1536&bih=754'

    driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver.get(i_URL)

    html = driver.page_source
    soup = BS(html, features="html.parser")

    img = soup.select('img')

    i_list = []
    count = 1

    for i in img:
        try:
            i_list.append(i.attrs["src"])
        except KeyError:
            i_list.append(i.attrs["data-src"])

    for i in i_list:
        dir_name = 'data/' + keyword.split()[0]
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
        urlretrieve(i, dir_name + '/' + keyword + str(count) + '.jpg')
        count += 1

    driver.close()


def main():
    crawling('nwu pattern uniform')
    crawling('acu pattern uniform')
    crawling('aor1 pattern uniform')
    crawling('aor2 pattern uniform')
    crawling('multicam pattern uniform')


if __name__ == "__main__":
    main()

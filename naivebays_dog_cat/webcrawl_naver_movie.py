from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

context = './data/'
driver = webdriver.Chrome(context+'chromedriver')
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)
all_divs = soup.find_all('div',attrs={'class','tit3'})
products = [div.a.string for div in all_divs]
for product in products
    print(product)


from selenium import webdriver
from bs4 import BeautifulSoup

# 내장 라이브러리이므로 설치할 필요가 없습니다.
import time

# 셀레니움을 실행하는데 필요한 크롬드라이버 파일을 가져옵니다.
driver = webdriver.Chrome('chromedriver')

# 네이버 주식페이지 url을 입력합니다.
url = 'https://m.stock.naver.com/item/main.nhn#/stocks/005930/total'
# 크롬을 통해 네이버 주식페이지에 접속합니다.
driver.get(url)

# 크롬을 종료합니다.
driver.quit()
# 이수안컴퓨터연구소 Selenium CGV 영화 리뷰 스크래핑를 유튜브 영상 클론코딩

# 영상에서 댓글이 72개가 나오지 않는 것을 고침
# 영상 가장 마지막 셸의 코드가 영상에서는 오류가 안 났지만 제가 돌렸을 때는 
# StaleElementReferenceException : Message : stale element reference : element is not attached to the page document 
# 라는 오류가 떴던 것을 고침

!pip install Selenium
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

import sys
sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome('chromedriver', options=chrome_options)

import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

def get_movie_reviews(url, page_num=10):

  wd.get(url)

  writer_list=[]
  review_list = []
  date_list = []

  for page_no in range(1, page_num+1):
    try:
      page_ul = wd.find_element('id', 'paging_point')
      page_a = page_ul.find_element('link text', str(page_no))
      page_a.click()
      time.sleep(1)

      writers = wd.find_elements('class name', 'writer-name')
      writer_list += [writer.text for writer in writers]
      reviews = wd.find_elements('class name', 'box-comment')
      review_list += [review.text for review in reviews]
      dates = wd.find_elements('class name', 'day')
      date_list += [date.text for date in dates]

      if page_no % 10 ==0:
        next_button = page_ul.find_element('css selector', '#paging_point > li > button')   # 영상에서 댓글이 모두 나오지 않는 것을 고치기 위해 css selector로 수정
        next_button.click()
        time.sleep(1)
    except NoSuchElementException:
      break

  movie_review_df = pd.DataFrame({'Writer' : writer_list,
                                    'Review' : review_list,
                                    'Date' : date_list})
  return movie_review_df

#-------------------------------------------------------------------------------------------------

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=1'
wd = webdriver.Chrome('chromedriver', options=chrome_options)
wd.get(url)

movie_chart = wd.find_element('class name', 'sect-movie-chart')
contents = movie_chart.find_elements('class name', 'box-contents')

  #StaleElementReferenceException 오류를 고치기 위해 매반복마다 content에 다음 content를 입력해줌.
  #---------------------------------------------------------------
for i in range(len(contents)):
  url = 'http://www.cgv.co.kr/movies/?lt=1&ft=1'
  wd = webdriver.Chrome('chromedriver', options=chrome_options)
  wd.get(url)
  
  movie_chart = wd.find_element('class name', 'sect-movie-chart')
  contents = movie_chart.find_elements('class name', 'box-contents')
  content=contents[i]
  #---------------------------------------------------------------------
  link = content.find_element('tag name', 'a').get_attribute('href')
  title = content.find_element('class name', 'title').text
  percent = content.find_element('class name', 'percent').text
  info = content.find_element('class name', 'txt-info').text
  print(title, percent, info, link)
  print(get_movie_reviews(link, 2))

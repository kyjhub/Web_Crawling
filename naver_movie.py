from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from urllib.parse import quote

def get_movie_reviews(mcode, page_num=10):

  movie_review_df = pd.DataFrame(columns=("Title", "Score", "Review"))
  url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=" + str(mcode) + "&target=after"
  idx = 0

  for _ in range(0, page_num):
    movie_page = urllib.request.urlopen(url).read()
    movie_page_soup = BeautifulSoup(movie_page, 'html.parser')

    review_list = movie_page_soup.find_all('td', {'class':'title'})
    for review in review_list:
      title = review.find('a', {'class':'movie color_b'}).get_text()
      score = review.find('em').get_text()
      review_text = review.find_all("a")[1]['onclick']
      review_text = review_text.replace("report(", "").split("', '")[2]
      movie_review_df.loc[idx] = [title, score, review_text]
      idx += 1
      print("#", end="")
    try:
      url = "https://movie.naver.com" + movie_page_soup.find('a', {'class':'pg_next'}).get('href')
    except:
      break
  return movie_review_df
  

movie_review_df = get_movie_reviews(73372, 1)
movie_review_df

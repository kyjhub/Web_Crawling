# 코랩에서 작성
# 이수안컴퓨터연구소 네이버 웹툰 스크래핑 유튜브 영상을 기반으로 작성


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

wd.get("https://comic.naver.com/index")

import time

genre_ul = wd.find_element(By.CLASS_NAME, 'tab_gr')
genre_list = genre_ul.find_elements('tag name', 'a')

for genre in genre_list:
  genre.click()
  time.sleep(1)
  print("[", genre.text, "]")
  
  genre_rec_list = wd.find_elements('class name', 'genreRecomInfo2')
  for genre_rec in genre_rec_list:
    title_class = genre_rec.find_element('class name', 'title')
    title = title_class.find_element('tag name', 'a').text
    user = genre_rec.find_element('class name', 'user').text
    print("\t", title, "-", user)

#   예시 출력

#     [ 에피소드 ]
# 	 독립일기 - 자까
# 	 만물의 영장 - 보민
# 	 오빠세끼 - 올리브유
# 	 배트맨: 웨인 패밀리 어드벤처 - CRC Payne / StarBite
# 	 나쁜사람 - 둠스
# 	 언덕 위의 제임스 - 쿠당탕
# [ 옴니버스 ]
# 	 조조코믹스 - 이동건
# 	 기묘한 만화 - 몬킬
# 	 먹는 인생 - 홍끼
# 	 뉴심:교체인생 - 지인
# 	 애옹식당 - 정다정
# 	 미물 - 외눈박이 / 김도연
# [ 스토리 ]
# 	 안개무덤 - 김태영
# 	 정글쥬스 - 형은 / 쥬더
# 	 혼모노트 - 민수상
# 	 쿠베라 - 카레곰
# 	 하드캐리 - 조양
# 	 최강전설 강해효 - 최병열
# [ 일상 ]
# 	 독립일기 - 자까
# 	 오빠세끼 - 올리브유
# 	 배트맨: 웨인 패밀리 어드벤처 - CRC Payne / StarBite
# 	 범이올시다! - 해
# 	 먹는 인생 - 홍끼
# 	 윌유메리미 - 마인드C
# [ 개그 ]
# 	 만물의 영장 - 보민
# 	 폭탄주먹 변대장 - 엄재경 / 지야프
# 	 죄송한데 주인공이세요? - 조석
# 	 나쁜사람 - 둠스
# 	 언덕 위의 제임스 - 쿠당탕
# 	 마루는 강쥐 - 모죠
# [ 판타지 ]
# 	 혼모노트 - 민수상
# 	 쿠베라 - 카레곰
# 	 갓트 - 서패스 / 아거주누
# 	 트롤트랩 - 유비
# 	 가상&RPG - 주다현
# 	 던전 씹어먹는 아티팩트 - 엄키 / 제로워터
# [ 액션 ]
# 	 정글쥬스 - 형은 / 쥬더
# 	 최강전설 강해효 - 최병열
# 	 현실퀘스트 - 이주운 / 태성
# 	 천재의 게임방송 - 지금 / 하이엔드
# 	 들개 - 홍원찬 / 최감자
# 	 옥타곤의 제왕 - GOPUBI / 필립
# [ 드라마 ]
# 	 하드캐리 - 조양
# 	 온실 속 화초 - 옛사람
# 	 킬더킹 - 마사토끼 / joana
# 	 특수청소 - 한(恨)
# 	 아빠같은 남자 - 이수민
# 	 자취방 신선들 - 마로
# [ 순정 ]
# 	 불편한 관계 - 잔스
# 	 시에라 - 문아 / Rana
# 	 방과후 레시피 - 혜루
# 	 환상연가 - 반지운
# 	 모어 라이프 - 이아영
# 	 가족같은 XX - 서우현
# [ 감성 ]
# 	 연우의 순정 - 이솔
# 	 북경신보 - 산하 / 김대영
# 	 슈퍼스타 천대리 - 박경원 / 이재국 / Do8
# 	 6월의 라벤더 - 밤희 / 게살
# 	 굿닥터 - 곰작가 / 썬파인
# 	 다시 또 봄 - 이힝
# [ 스릴러 ]
# 	 안개무덤 - 김태영
# 	 온에어 - 심복일
# 	 침묵의 밤 - 한동우 / Q-Ha
# 	 베니루 BAENIRU - 우지금
# 	 아인슈페너 - 한끼룩
# 	 따개비 - 뜰새 / delete / 레고밟았어
# [ 무협/사극 ]
# 	 무사만리행 - 운 / 배민기
# 	 천마육성 - 광휘 / 조형근
# 	 나노마신 - 현절무 / 금강불괴 / 한중월야
# 	 화산귀환 - LICO / 비가
# 	 사상최강 - 이단아 / 황규영
# 	 칼에 취한 밤을 걷다 - JP / 송민 / 유진성
# [ 스포츠 ]
# 	 빌드업 - 911
# 	 해일로의 아침 - 박장고 / 이우
# 	 빅맨 - 하하영
# 	 윈드브레이커 - 조용석
# 	 위닝샷! - 강견 / 시바견
# 	 탑코너 - 윤성 / 라군

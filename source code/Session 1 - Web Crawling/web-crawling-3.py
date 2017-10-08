#!usr/bin/env python
# File name....: web-crawling-3.py
# Module name..: 3 - Web Crawling
# Author.......: Buomsoo Kim, Jinsoo Park
'''
This program demonstrates how to navigate simple HTML tree structure using 
urllib and beautifulsoup4. It will print all the reviews up to 5 review pages.

This file is provided for educational purposed and can be distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.
'''

# 웹 크롤링에 필요한 모듈 불러오기
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 리뷰 내용을 담기 위한 리스트 생성
review_list = []

# try ~ except 문을 통해 혹시나 있을지 모르는 에러 핸들링
try:
	# 임의로 5번째 페이지까지 크롤링함
	for n in range(5):
		# 불러오려는 url 입력하기(다음 영화 리뷰 - 라라랜드)
		url = 'http://movie.daum.net/moviedb/grade?movieId=95306&type=netizen&page={}'.format(n + 1)

		# urlopen 메소드를 통해 web 객체 생성
		webpage = urlopen(url)

		# html 파싱을 위한 BeautifulSoup 객체 생성
		#source = BeautifulSoup(webpage, 'html.parser')
		source = BeautifulSoup(webpage, 'html5lib')

		# find_all(name, attrs, recursive, string, limit, **kwargs)메소드를 통해 모든 리뷰 추출
		reviews = source.find_all('p', {'class': 'desc_review'})

		# for 문을 통해 해당 페이지의 리뷰 추출 후 리스트에 반환
		for review in reviews:
			review_list.append(review.get_text().strip())
			# 혹시 위 코드가 작동 안하면 아래 코드로 시도해 볼 것 
			# 리뷰를 텍스트로 받아와 탭, 엔터 등 화이트스페이스를 없애고 반환
			#review_list.append(review.get_text().strip().replace('\n', '').replace('\t', '').replace('\r',''))
except:
	print('Could not crawl review data')

# txt 파일로 리뷰 내용 출력하기
file = open('data.txt', 'w', encoding = 'utf-8')
for review in review_list:
	file.write(review + '\n') # 각 리뷰를 줄 단위로 txt 파일에 저장
file.close()

# ///// END OF web-crawling-3 /////////////////////////////////////////////////
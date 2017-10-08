#!usr/bin/env python
# File name....: web-crawling-2.py
# Module name..: 3 - Web Crawling
# Author.......: Buomsoo Kim, Jinsoo Park
'''
This program demonstrates how to navigate simple HTML tree structure using urllib
and beautifulsoup4.It will print all the reviews in the first review page.

This file is provided for educational purposed and can be distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.
'''

# 웹 크롤링에 필요한 모듈 불러오기
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 불러오려는 url 입력하기(다음 영화 리뷰 - 라라랜드)
url = 'http://movie.daum.net/moviedb/grade?movieId=95306&type=netizen&page=1'

# urlopen 메소드를 통해 web 객체 생성
webpage = urlopen(url)

# html 파싱을 위한 BeautifulSoup 객체 생성
#source = BeautifulSoup(webpage, 'html.parser')
source = BeautifulSoup(webpage, 'html5lib')

# find_all(name, attrs, recursive, string, limit, **kwargs)메소드를 통해 모든 리뷰 추출
reviews = source.find_all('p', {'class': 'desc_review'})

# for문을 통해 해당 페이지의 리뷰 모두 추출하기
for review in reviews:
	print(review.get_text().strip())

# ///// END OF web-crawling-2 /////////////////////////////////////////////////
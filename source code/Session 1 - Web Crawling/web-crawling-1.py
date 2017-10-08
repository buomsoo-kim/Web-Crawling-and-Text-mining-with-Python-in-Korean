#!usr/bin/env python
# File name....: web-crawling-1.py
# Module name..: 3 - Web Crawling
# Author.......: Buomsoo Kim, Jinsoo Park
'''This program demonstrates how to navigate simple HTML tree structure using 
urllib and beautifulsoup4. It will print the first review.

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

# find(name, attrs, recursive, string, **kwargs)메소드를 통해 첫 번째 리뷰 추출
review = source.find('p', {'class': 'desc_review'})

# 리뷰 내용 보여주기
print(review.get_text().strip())

# ///// END OF web-crawling-1 /////////////////////////////////////////////////
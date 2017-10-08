#!usr/bin/env python
# File name....: web-crawling-4-sing.py
# Module name..: 3 - Web Crawling
# Author.......: Buomsoo Kim, Jinsoo Park
'''
This program demonstrates how to navigate simple HTML tree structure using 
urllib and beautifulsoup4. It will print all the reviews for the target movie.

This file is provided for educational purposed and can be distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.
'''

# 웹 크롤링에 필요한 모듈 불러오기
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 영화 <씽> 리뷰 첫 번째 페이지에서 총 페이지 개수 계산하기
url = 'http://movie.daum.net/moviedb/grade?movieId=99056&type=netizen&page=1'
webpage = urlopen(url)
#source = BeautifulSoup(webpage, 'html.parser')
source = BeautifulSoup(webpage, 'html5lib')
# find(name, attrs, recursive, string, **kwargs)메소드를 통해 평점 준 사람 수 추출
review = source.find('span', {'class': 'num_review'})

# 총 리뷰 개수를 10으로 나누어 페이지 개수를 계산할 수 있음
t = review.get_text().strip() # 평가를 한 네티즌 인원 수를 받아들여 공백을 지움
t = t[:-1].replace(',', '') # 앞에서 받은 숫자에 있는 콤마를 제거해야 integer 전환시 에러가 없음
                            # 이 웹사이트의 경우 평가한 네티즌 총 인원 수(네티즌 평점 아래 있는 수), 
                            # 즉 예를 들어 (1,091)에서 양 괄로를 지워야 하는데 우선 오른쪽 괄호만 
                            # 지우기 위해 t[:-1]로 처리함
page_no = int(int(t[10:])/10) # t[10:]를 하는 이유는 네티즌 인원 수 앞에 왼쪽 괄호 포함해서 숫자 앞에
                              # '(평점 준 사람 수'의 불필요한 string 10개를 제거 하기 위함이다.
                              # 총 평점 개수를 10으로 나누고 정수로 변환해 총 페이지 개수를 계산
                              # 10으로 나누는 이유는 한 페이지당 평점이 10개씩 있어서 그렇다

review_list = []
for n in range(page_no):
	# 불러오려는 url 입력하기
	url = 'http://movie.daum.net/moviedb/grade?movieId=99056&type=netizen&page={}'.format(n + 1)

	# urlopen 메소드를 통해 web 객체 생성
	webpage = urlopen(url)

	# html 파싱을 위한 BeautifulSoup 객체 생성
	#source = BeautifulSoup(webpage, 'html.parser')
	source = BeautifulSoup(webpage, 'html5lib')

	# find_all(name, attrs, recursive, string, limit, **kwargs)메소드를 통해 모든 리뷰 추출
	reviews = source.find_all('p', {'class': 'desc_review'})

	# for 문을 통해 해당 페이지의 리뷰 추출 후 리스트에 반환
	for review in reviews:
		review_list.append(review.get_text().strip().replace('\n', '').replace('\t', '').replace('\r',''))

# txt 파일로 리뷰 내용 출력하기
file = open('data2.txt', 'w', encoding = 'utf-8')
for review in review_list:
	file.write(review + '\n') # 각 리뷰를 줄 단위로 txt 파일에 저장합니다
file.close()

# ///// END OF web-crawling-4-sing ////////////////////////////////////////////
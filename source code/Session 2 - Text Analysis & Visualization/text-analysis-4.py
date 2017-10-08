#!usr/bin/env python
# File name....: text-analysis-4.py
# Module name..: 4 - Text Analysis & Visualization
# Author.......: Buomsoo Kim, Jinsoo Park
'''
This program demonstrates how to visualize text using pytagcloud package.

This file is provided for educational purposed and can be distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.
'''

import pytagcloud, random, webbrowser	# pytagcloud 모듈 사용
from konlpy.tag import Twitter 			# 트위트 형태소 분석기 사용
from collections import Counter 		# collections 패키지에서 Counter 불러옴

#---------------  wordcloud 생성에 필요한 함수 정의 ------------------------------------#
def get_tags(text, ntags = 100, multiplier = 1):
	'''워드클라우드를 그리기 위한 태그와 그 빈도수, 그리고 색깔 생성

	text.......: list나 tuple 형태의 텍스트 데이터
	ntags......: 태그의 개수로 설정한 기본값은 100
	multiplier.: 상대적인 크기를 사용자가 상수로 정한 변수로 기본값은 1
	Return.....: [색, 태그, 사이즈]로 이루어진 list
	'''
	t = Twitter()						# 트위트 형태소 분석기 변수 생성
	nouns = []							# 트위트 분석 결과 명사만 담을 list 생성
	for sentence in text:				# 텍스트는 list 혹은 tuple 형태로 입력
		for noun in t.nouns(sentence):	# list의 각 요소(sentence)를 for 문을 이용해 꺼낸 후에 형태소 분석한 후 명사만 추려내
			nouns.append(noun)			# 다시 for 문을 통해 그 명사들을 nouns list에 append함
#			if noun == '영화':			# '영화' 단어가 너문 자주 나올 것을 예상하고 이 단어 제외 할 때 사용하는 코드
#				pass
#			else:
#				nouns.append(noun)		# 다시 for 문을 통해 그 명사들을 nouns list에 append함
	count = Counter(nouns)				# Counter()를 통해 nouns 리스트에 있는 서로 다른 명사의 개수 구함 

	# n = 태그(워드클라우드에 포함되는 단어의 개수)
	# c = 각 태그의 발생 빈도 수
	# c랑 multiplier가 곱해져서 size가 결정딤 
	return [{'color':color(), 'tag':n, 'size': c * multiplier } \
					for n, c in count.most_common(ntags)]

def draw_cloud(tags, filename, fontname = 'Noto Sans CJK', size = (1000, 600)):
	''' pytagcloud의 워드클라우드 이미지를 그리는 함수를 받아 이미지를 생성하고 이를 오픈
		
	tags.....: get_tags()를 통해 생성된 [색, 총 태그 개수, 사이즈]로 이루어진 리스트
	filename.: 워드클라우드 이미지 파일을 저장하는 이름
	fontname.: 사용할 폰트 이름. 한국어를 사용하기 위한 fontname 'Noto Sans CJK' 활용.
			   폰트 설정 관련해서는 강의노트 Seession 4 <한국어 폰트 추가하기 랙 Windows> 참조
	size.....: 이미지 사이즈로 디폴트는 (1000, 600)
	Return...: NONE
	'''
	# pytagcloud 모듈의 함수로 워드클라우드 이미지를 생성한다(png 형식)
	pytagcloud.create_tag_image(tags, filename, fontname = fontname, size = size)
	
	# webrowser 모듈의 open 함수를 통해 저장된 파일을 연다
	webbrowser.open(filename)

	# Mac OS X의 경우 만약 위의 코드로 웹브라우스를 열지 못하면 다음 코드로 구글 크롬을 오픈하면 된다
	#chrome_path = 'open -a /Applications/Google\ Chrome.app %s' 
	#webbrowser.get(chrome_path).open(filename)

r = lambda: random.randint(0, 255)	# 람다식(r)을 통해 0부터 254 사이의 임이의 정수 추출
color = lambda: (r(), r(), r())		# 람다식 3개(r)를 합쳐 RGB로 색을 정의하기 위한 새로운 람다식(color) 정의

#--------------- 분석에 앞서, 크롤링했던 영화 리뷰 데이터 불러오기 --------------------------------#
file = open('data-full.txt', 'r', encoding = 'utf-8') # 크롤링해서 수집한 영화 리뷰 파일 열기
lines = file.readlines() # readlines()를 통해 영화 리뷰 파일의 모든 라인 읽어오기
file.close() # 파일 닫기

#--------------- 추출한 명사 태그 워드클라우드로 작성하기 --------------------------------------#
# 위에서 정의한 get_tags() 이용해 태그(명사) 추출
tags = get_tags(lines)					

# 위에서 정의한 draw_cloud()를 이용해 워드클라우드로 저장 후 웹브라우즈로 열기
draw_cloud(tags, 'wordcloud.png')	# 'wordcloud.png' 이름으로 파일 저장

# ///// END OF text-analysis-4 ////////////////////////////////////////////////
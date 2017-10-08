#!usr/bin/env python
# File name....: text-analysis-3.py
# Module name..: 4 - Text Analysis & Visualization
# Author.......: Buomsoo Kim, Jinsoo Park
'''
This program demonstrates how to analyze text. It uses Twitter in konlpy module,
and handles the moview review full data collected during Module 3.

This file is provided for educational purposed and can be distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.
'''

# 한국어 텍스트 분석에 필요한 모듈 불러오기(konlpy)
from konlpy.tag import Twitter # 트위터 형태소 분석기 불러오기

# collections 패키지에서 Counter(등장 횟수를 세주는 역할)를 불러옴
from collections import Counter	

#--------------- 분석에 앞서, 크롤링했던 영화 리뷰 데이터 불러오기 --------------------------------#
file = open('data-full.txt', 'r', encoding = 'utf-8') # 영화 리뷰 파일 열기
lines = file.readlines() # readlines()를 통해 영화 리뷰 파일의 모든 라인 읽어오기
file.close() # 파일 닫기

#print(lines)

#--------------- 전체 텍스트를 형태소 분석하기(데이터 구조가 리스트로 되어있다는 것을 기억하자) ----------------#
twitter = Twitter() # 트위터 변수 생성
sentences_tag = []
for sentence in lines:							# lines 데이터 형태가 list로 되어 있으므로 for 문을 통해 하나씩 꺼냄
	sentences_tag.append(twitter.pos(sentence))	# 각 리뷰 데이터를 twitter 형태소 분석기로 분석해 그 결과를 
												# sentences_tag list에 append 함
												# 형태소 분석 결과는 ('단어', '태그')의 tuple로 반환
												# 결과적으로, sentences_tag list는 tuple로 이루어진 list가 됨
#print(sentences_tag)
#print('-' * 30)
#print(len(sentences_tag))

#--------------- 전체 텍스트에서 명사와 형용사만 걸러내기 --------------------------------------#
noun_adj_list = []										
for sentence in sentences_tag:				# sentences_tag list에 있는 (단어, 태그) tuple을 for 문을 통해 하나씩 꺼냄
	for word, tag in sentence:				# 각 tuple의 단어(word)와 태그(tag)를 for 문을 통해 각각 꺼냄
		if tag in ['Noun', 'Adjective']:	# 만약에 특정 단어의 태그가 명사(Noun)이거나 형용사(Adjective)일 경우,
			noun_adj_list.append(word)  	# noun_adj_list 리스트에 그 단어를 append 함

#--------------- 전체 텍스트에서 가장 많이 사용된 명사와 형용사만 출력하기 ----------------------------#
# Counter에 noun_adj_list list를 넣어 서로 다른 명사와 형용사가 얼마나 많이 쓰였는지를 셈
counts = Counter(noun_adj_list)	

# most_common() 메소드를 통해 10개의 가장 많이 사용된 단어를 추출
# most_common() 메소드 내에 들어가는 파라미터는 정수로 몇개의 가장 빈번히 등장하는 원소를 반환할 것인지를 결정함
print(counts.most_common(10)) 	
								
# ///// END OF text-analysis-3 ////////////////////////////////////////////////

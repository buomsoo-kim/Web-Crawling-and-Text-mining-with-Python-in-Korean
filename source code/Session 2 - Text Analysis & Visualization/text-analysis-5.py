#!usr/bin/env python
# File name....: text-analysis-5.py
# Module name..: 4 - Text Analysis & Visualization
# Author.......: Buomsoo Kim, Jinsoo Park
'''
This program demonstrates how to compute similarity between movie reviews.

This file is provided for educational purposed and can be distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.
'''

# sklearn 패키지에서 TfidfVectorizer 불러오기
from sklearn.feature_extraction.text import TfidfVectorizer	
# sklearn 패키지에서 cosine_similarity() 불러오기 (코사인 유사도 계산)
from sklearn.metrics.pairwise import cosine_similarity

#--------------- 분석에 앞서, 크롤링했던 영화 리뷰 데이터 불러오기 --------------------------------#
doc1 = '' 											# 리뷰 데이터를 담기 위한 스트링 변수 생성
file = open('data1.txt', 'r', encoding = 'utf-8') 	# 영화 리뷰 파일 <라라랜드> 열기
lines = file.readlines() 							# readlines()를 통해 영화 리뷰 파일의 모든 라인 읽어오기
for line in lines:									# for 문을 통해 lines에 있는 모든 텍스트를 
	doc1 += line 									# doc1에 이어 붙임
file.close() 										# 파일 닫기

doc2 = '' 											# 리뷰 데이터를 담기 위한 스트링 변수 생성
file = open('data2.txt', 'r', encoding = 'utf-8') 	# 영화 리뷰 파일 <씽(Sing)> 열기
lines = file.readlines() 							# readlines()를 통해 영화 리뷰 파일의 모든 라인 읽어오기
for line in lines:									# for 문을 통해 lines에 있는 모든 텍스트를		
	doc2 += line            						# doc2에 이어 붙임	
file.close() 										# 파일 닫기

doc3 = '' 											# 리뷰 데이터를 담기 위한 스트링 변수 생성
file = open('data3.txt', 'r', encoding = 'utf-8') 	# 영화 리뷰 파일 <더 킹> 열기
lines = file.readlines() 							# readlines()를 통해 영화 리뷰 파일의 모든 라인 읽어오기
for line in lines:									# for 문을 통해 lines에 있는 모든 텍스트를
	doc3 += line 									# doc3에 이어 붙임
file.close() 										# 파일 닫기

corpus = [doc1, doc2, doc3]				# doc1, doc2, doc3를 합쳐 corpus list로 만듦
vectorizer = TfidfVectorizer()			# TfidfVectorizer() 변수 생성
X = vectorizer.fit_transform(corpus)	# fit_transform()를 통해 corpus의 텍스트 데이터를 벡터화해 X에 저장
X = X.todense()							# X를 dense한 matrix로 변환

#--------------- 영화 간의 cosine similarity 계산 ----------------------------------#
print("Similarity between 'LaLa Land' and 'Sing': ", cosine_similarity(X[0], X[1]))
print("Similarity between 'LaLa Land' and 'The King': ", cosine_similarity(X[0], X[2]))
print("Similarity between 'Sing' and 'The King': ", cosine_similarity(X[1], X[2]))

# ///// END OF text-analysis-5 ////////////////////////////////////////////////
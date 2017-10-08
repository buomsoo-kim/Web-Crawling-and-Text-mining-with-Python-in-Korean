#!usr/bin/env python
# File name....: text-analysis-2.py
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

# 분석에 앞서, 크롤링했던 영화 리뷰 데이터 불러오기
file = open('data-full.txt', 'r', encoding = 'utf-8') # 영화 리뷰 파일 열기
lines = file.readlines() # readlines()를 통해 영화 리뷰 파일의 모든 라인 읽어오기
file.close() # 파일 닫기

#print(lines)

# 트위터 변수 생성
twitter = Twitter()

# 문장을 형태소 분석하기
tokens = twitter.morphs(lines[1]) # 첫번째 문장의 형태소 분석
print(tokens) # 형태소 분석 결과 출력하기

# ///// END OF text-analysis-2 ////////////////////////////////////////////////
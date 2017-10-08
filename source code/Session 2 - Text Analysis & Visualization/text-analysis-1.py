#!usr/bin/env python
# File name....: text-analysis-1.py
# Module name..: 4 - Text Analysis & Visualization
# Author.......: Buomsoo Kim, Jinsoo Park
'''
This program demonstrates how to analyze text. It uses Kkma in konlpy module.

This file is provided for educational purposed and can be distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.
'''

# 한국어 텍스트 분석에 필요한 모듈 불러오기(konlpy)
from konlpy.tag import Kkma # 꼬꼬마 형태소 분석기 사용

# 꼬꼬마 인스턴스 생성
kkma = Kkma() 

# 분석하려는 텍스트
text = '오늘 날씨가 따뜻합니다. 내일은 눈이 온다고 합니다. 모레는 오늘보다 춥습니다.' 

# 텍스트를 문장으로 슬라이싱
sentences = kkma.sentences(text) 

# 문장을 리스트 형태로 출력
print(sentences) 

# 문장에서 명사만 추출하기
nouns = kkma.nouns(text) 
print(nouns)

# 문장에서 형태소 출력하기
morphs = kkma.morphs(text) 
print(morphs)

# 문장의 구성 요소(pos) 태깅하기
tags = kkma.pos(text) 
print(tags)

# ///// END OF text-analysis-1 ////////////////////////////////////////////////
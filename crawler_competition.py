import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time
from tqdm import tqdm

import pandas as pd

#한번열어보기
url = 'https://www.cheongwon.go.kr/portal/petition/open/view'
response = requests.get(url)
#print(response)

#웹페이지를 분해할 bs4 객체 생성
#파싱 = 어떤 정보 덩어리에서 원하는 정보를 추출하는것
soup = BeautifulSoup(response.text,'html.parser')
#print(response.text)

#soup 라는 파싱 객체가, 'span' 이라는 양식의 class를 찾아서
#class = 'category'라고 적힌 내용을 'category'라는 변수 이름에 저장
category = soup.find_all('span',class_='category') #누구에게 건의하나, 부서들 적혀있음
subject = soup.find_all('span',class_='subject') #제목 같은 느낌
petition = soup.find_all('span',class_='text') #본문
#print(category,subject,petition)


#######################################
# #크롤링한 결과물을 보기 쉬운 형태로 변환
# corpus = []
# corpus_c = []
# corpus_s = []
# corpus_t = []
# for i in range(len(category)):
#     corpus_c.append(category[i].text)
#     corpus_s.append(subject[i].text)
#     corpus_t.append(petition[i].text)
# # time.sleep(2) #2초정도 정지
#######################################

#크롤링한 결과물을 보기 쉬운 형태로 변환
corpus = []
for c,s,t in zip(category,subject,petition):
    corpus.append([c.text,s.text,t.text])
time.sleep(2) #2초정도 정지

df=pd.DataFrame(corpus,columns=['카테고리','제목','청원내용'])
df.head()
print(df.head())

df.to_csv('./crawling_sampl.csv',index=False,encoding='utf-8-sig')



# 디버깅: 각 리스트의 개수와 내용물 확인
print(f"카테고리 개수: {len(category)}")
print(f"제목 개수: {len(subject)}")
print(f"청원내용 개수: {len(petition)}")
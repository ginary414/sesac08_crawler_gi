import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time
from tqdm import tqdm

import pandas as pd

max_pages = int(input('몇 페이지까지 크롤링할까요?\n'))
all_corpus = [] #1,2,3 max_pages 까지의 크롤링 내역을 한꺼번에 저장 list

#tqdm이 전체 실행시간 대비, 현재 진행 상황을 알려줌 (지금 진행상황을 알려줌)
for page in tqdm(range(1,max_pages+1),desc='크롤링 진행중....'):
    url = f'https://www.cheongwon.go.kr/portal/petition/open/view?pageIndex={page}'
    response = requests.get(url)


#한번열어보기
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

    all_corpus.extend(corpus)
    time.sleep(2) #2초정도 정지



#corpus 자연어 데이터의 말뭉치를 부르는 명칭
df=pd.DataFrame(all_corpus,columns=['카테고리','제목','청원내용'])
df.head()
print(df.head())

df.to_csv('./crawling_multiple_sampl.csv',index=False,encoding='utf-8-sig')



# 디버깅: 각 리스트의 개수와 내용물 확인
print(f"카테고리 개수: {len(category)}")
print(f"제목 개수: {len(subject)}")
print(f"청원내용 개수: {len(petition)}")
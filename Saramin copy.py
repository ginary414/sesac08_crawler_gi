import requests
from bs4 import BeautifulSoup
import pandas as pd
import re   #정규표현식
from html import unescape


def clean_text(text):
    #빈 텍스트를 넣어 clean_text 실행했다면
    if not text:
        return " "
    
    #text가 있다면 (빈 값이 아니라면 ) 정제
    text = unescape(text)

    #re(정규표현식) : 텍스트를 특정한 패턴으로 찾아서, 변형
    #text = re.sub(패턴, 바꿀 문자, 문장) -> 문장에서 '패턴'을 찾아서 '바꿀문자'로 변형
    #a-zA-Z 영문자 전체, ㄱ-ㅎ가-힣 한글전체
    #\ (공백) \s+ (한칸 이상의 모든 공백)
    #\s 공백 한칸을 의미 +는 여러칸
    text = re.sub(r'\s+',' ',text)
    return text.strip()



def crawling_data(search_word):
    #'헤더' -> 브라우저가 서버에 무언가 요청할떄
    #나 이런 브라우저에요 라는 내용

    # 요청하는 브라우저의 종류
    # 요청하는 언어의 종류·
    base_url ='https://www.saramin.co.kr/zf_user/search?'
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/126.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "ko-KR,ko;q=0.9,en;q=0.8",
    }

    #리퀘스트를 보냄
    #headers :브라우저에 대한 내용
    #params : 이런 정보를 요청합니다 검색어 검색조건
    #timeout : 회신이 올떄까지 기다리는 시간 최대치

    response=requests.get(base_url,headers=headers,
                        params={'searchword':search_word},
                        timeout=10) #여기에 헤더 붙임

    #만약 response가 <200>이라면 정상
    soup = BeautifulSoup(response.text,'html.parser')
    #print(response.text)

    #검색결과선별
    rows = []
    #soup.select(구분자):'구분자'가 들어가는 모든 내용을 select{선택}
    #soup.find_all('div',class_ = 'item_recruit'_)
    for item in soup.select('div.item_recruit'):
            
        #1.회사명
        #select_one(구분자) : 구분자 이름을 갖는 딱 하나만 가져와!
        corp_name = item.select_one('div.area_corp')
        
        
        ###########################################
        # corp_name = corp_name.get_text(strip=True) if corp_name else ""
        # full_text = item.select_one('div.area_corp').get_text(strip=True)
        # corp_name = full_text.split('관심기업')[0].strip()
        ###########################################

        #2.채용 정보
        job_area = item.select_one('div.area_job')

        #3.공고 제목
        #<div>로 시작하지 않음! .job_tit /div가 아니어도 괜찮아!
        #job_title이라는 녀석을 찾아서 one 한개만 가져와!
        job_title = job_area.select_one('.job_tit')
        
        ##########################################
        #job_title = job_title.get_text(strip=True) if job_title else ""
        ##########################################

        #4.조건
        conditions=job_area.select_one('.job_condition')
        location = ''
        condition1 = ''

        if conditions :
            span = conditions.select('span')
            #조건1개 이상 있다면
            if len(span) >0:
                #첫번쨰 조건은 무조건 지역이다.
                location = span[0].get_text(strip=True)

            if len(span) >1:
                condition1 = span[1].get_text(strip=True)
        #5.직무 분야
        job_sector=job_area.select_one('.job_sector')
        job_sector=( job_sector.get_text(strip=True) if job_sector else "")

        #clean_text로 정제하기
        job_title = clean_text(job_title)
        location = clean_text(location)
        condition1 = clean_text(condition1)
        job_sector = clean_text(job_sector)
        corp_name = clean_text(corp_name)

        rows.append({
            '공고 이름' : job_title,
            '회사 위치' : location,
            '조건 1' : condition1,
            '조건 2' : job_sector,
            '회사 이름' : corp_name
        })

    df = pd.DataFrame(rows)
    print(df)

crawling_data('AI')
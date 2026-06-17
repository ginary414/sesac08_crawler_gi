import requests
from bs4 import BeautifulSoup

#웹브라우저 통신
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#시간,판다스
import time
from tqdm import tqdm
import pandas as pd

#브라우저의 옵션 (크롬 브라우져의 옵션)
#동적으로 selenium을 기반으로 작업할 떄 아래와 같은 규칙 적용할께
option = Options()
option.add_argument('--no-sandbox') #샌드박스 비활성화
option.add_argument('--disable-dev-shm-usage') #공유메모리 꺼
option.add_argument('--disable-gpu') #gpu 꺼
option.add_argument('--enable-unsafe-swiftshader') #gpu 안쓰니까 이거사용해

driver = webdriver.Chrome(options=option)
base_url ='https://www.musinsa.com/categories/item/001'

driver.get(base_url)
time.sleep(2)
#로딩시간 고려

#윈도우 스크롤 내리는 스크립트 추가
driver.execute_script('window.scrollTo(0,2000)')
time.sleep(2)

#창에 보이는 아이템 가져오기
#정적인거는 bs4 동적인거는 selenium 로 구분자 가져옴
#html => 웹페이지 '내용' 담당, CSS => 웹페이지 '디자인' 담당
items = driver.find_elements(By.CSS_SELECTOR,".sc-bSFBcf.iEkOIH")
item_list = []
#.sc-bSFBcf.iEkOIH
#.sc-jxOwhs.heXIMD

for item in items:
    #아래의 코드를 실행해봐
    try:
        #개별 상품에 대한 정보를 get
        #find_element( CSS를 기준으로 찾아줘 a['이름']):이름을 가지고 있는 블럭
        #a태그가 뭍은 ['이름']을 가진것
        a_tag = item.find_element(By.CSS_SELECTOR,"a[data-original-price]")
        #상품이름
        name = a_tag.get_attribute("aria-label")

        #예외처리
        #str(name) name에 뭐가 들어오건 str
        #replace 제거할 데이터
        # strip 양쪽 공백 제거
        name = (str(name).replace("상품 상세로 이동","").strip() if name else "이름없음")


        #브랜드이름
        brand = a_tag.get_attribute("data-item-brand")

        #가격
        price = a_tag.get_attribute("data-price")

        #상세페이지
        link = a_tag.get_attribute("href")
        print(f"name :{name},brand:{brand},price:{price},link:{link}")

        item_list.append({
            '상품명': name,
            '브랜드': brand,
            '가격': price,
            '상품링크': link
        })

    #실행하다가 '에러'가 발생하면 이렇게 해 (예외처리)
    except Exception as e:
        print(f"에러가 발생했습니다.:{e}")

driver.quit()

df=pd.DataFrame(item_list,columns=["상품명","브랜드","가격","상품링크"])
df.to_csv('./musinsa_result.csv',index=False,encoding='utf-8-sig')
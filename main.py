import streamlit as st

# st.title('스트림릿 타이틀')
# st.header('이것은 헤더입니다')
# st.subheader('서브헤더입니다')

# #텍스트를 입력하는 방법
# # 1.text 단순한 문자열 포메팅 없음 고정된 형식
# # st.text('이런식으로 그냥 텍스트 표시')
# # 2.write 유연한 표현 입력 데이터에 따라 자동으로
# # 적절한 형식을 지정해 줘야할때
# # 데이터 프레임도 표시 가능 문자열 리스트
# # color = 'red'
# # st.write(color)

# #3.마크다운(.md) 코렙 README 등 사용하는 구조
# st.markdown("https://www.naver.com/")
# st.markdown('[naver](https://www.naver.com/)')


# #이건 html 
# html_page = """
# <div style="background-color:blue;padding:50px">
# 	<p style="color:yellow;font-size:5'px">Enjoy Streamlit!</p>
# </div>
# """
# #마크다운에서다 html 코드를 직접삽입, unsafe _allow 를 적용
# st.markdown(html_page,unsafe_allow_html=True)




# #반응
# ####
# st.success("성공")
# st.warning("성공")
# st.error("성공")
# st.info("성공")


# #미디어 연결
# #PIL 이미지 오디오 유튜브 연결
# from PIL import Image

# #그림
# img = Image.open("./apple.jpg")
# st.image(img,width=300,caption='hi!')

# #open 미디어의 위치, 이 미디어로 무슨작업
# # video_file=open ("",'rb')
# # st.write(video_file)
# # video_binary = video_file.read()
# # st.video(video_binary)

# #유튜브 영상주소
# st.video("https://www.youtube.com/watch?v=apCoxLBiHog")

# #오디오 파일 연결
# audio_file= open ('경로','rb')
# audio_binary=audio_file.read()
# st.audio(audio_binary)





# #상호작용
# if st.button("눌러줘요"):
#     st.balloons()

# #체크박스
# if st.checkbox("체크해주세요"):
#     st.info("동의합니다.") #info 메세지가 실행

# #라디오박스
# radio_button = st.radio("선택하세요",['쉬기','공부하기'])
# if radio_button == '쉬기':
#     st.success("쉬세요")
# else:
#     st.warning("정말로?")
#     st.button("버튼을 다시한번")

# # 셀렉트 박스
# city = st.selectbox("거주지를 고르세요",
#                     ["영등포구","강서구","구로구"])

# #멀티 셀렉트
# job = st.multiselect("희망 직무를 선택하세요",
#                      ['데이터 분석','머신러닝','ax자동화'])

# #텍스트 입력
# #1.text_inpit : 한줄 입력 이름 이메일 주소 짧은 입력
# email= st.text_input("메일주소를 입력하세요",
#                      placeholder='sample@주소.com')

# if st.button('입력'):
#     st.write(email)
# #이런식으로 입력을 받은뒤 확인

# number = st.number_input("숫자를 입력",
#                          min_value=0,
#                          max_value=100,
#                          step=5)



# #슬라이더
# val = st.slider ("값을 선택하시오",0,10)
# st.write(val)

# #시간표시
# import datetime
# import time

# #datetime.datetime.now() 현재시각표시 함수
# today = st.date_input('Today is',datetime.datetime.now())
# st.write(today)

# #시간입력
# hour = st.time_input('the time is',datetime.datetime.now())

import pandas as pd
import matplotlib as plt
import seaborn as sns

df=pd.read_csv('./gapminder.tsv',sep='\t')
st.dataframe(df)

#sns,plt 그림을 그린 뒤 변수 저장
bar = sns.barplot(df,x="country",y='pop')
#plt.show () 역할을 st.pyplot()
st.pyplot()


st.bar_chart(df,x='country',y='pop')

#######################################################
#JSON
data= {'name':"john","surname":"wick"}
st.json(data)

codes = """
import os

path = os.path.join(origin,'train.csv')
"""
st.code(codes,language='python')

#progress bar(UI/UX) -> tqdm
import time
my_bar = st.progress(0)
for v in range(10):
    time.sleep(1)
    my_bar.progress(v+1)

with st.spinner("기다려주세요"):
    time.sleep(10)
st.success('완료되었습니다')
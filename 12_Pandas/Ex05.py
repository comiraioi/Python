'''
Created on 2023. 7. 19.

@author: Comi
'''

import pandas as pd
import numpy as np

col = ('이름','나이')
mydata = [('박세리',50),('강호동',30)]

df = pd.DataFrame(mydata,columns=col)
print(df)
'''
    이름  나이
0  박세리  50
1  강호동  30
'''
print('-------------------------')

filename = 'result01.csv'

''' 파일 작성하기
df.to_csv(파일명): 실행 파일과 같은 위치에 생성됨

encoding='euc-kr': 한글 처리
mode='w': 파일이 없으면 생성, 있으면 덮어쓰기 (default)
mode='a': 파일이 없으면 생성, 있으면 추가로 작성하기
index=False: 인덱스 숨기기
'''
df.to_csv(filename,encoding='euc-kr',mode='w',index=False)
print(filename+"에 저장")

print('-------------------------')

print(filename,"읽어오기\n")

''' 파일 읽어오기
pd.read_csv(파일명): 실행 파일과 같은 위치에 있는 파일 읽어오기
index_col=n: n번째 칼럼을 인덱스로 설정
'''
df2 = pd.read_csv(filename,encoding='euc-kr')
print(df2)

print('-------------------------')

#파일 작성
data = [[40,50,50],[70,50,20],[20,20,20],[11,22,33]]
col = ['국어','영어','수학']
idx = ['박보검','홍길동','아이유','김연아']
df = pd.DataFrame(data,idx,col)

filename = 'result02.csv'
df.to_csv(filename,encoding='euc-kr')

#파일 출력
print(pd.read_csv(filename,encoding='euc-kr',index_col=0))







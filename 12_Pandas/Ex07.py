'''
Created on 2023. 7. 20.

@author: user
'''

import pandas as pd
import numpy as np

d1 = {'고객번호' : [1001,1002,1003,1004,1005],
      '이름' : ['윤아','수영','서현','효연','써니']}

df1 = pd.DataFrame(d1)

d2 = {'고객번호':[1001,1007,1003,1004,1002,1001],
     '금액':[10000,20000,15000,5000,100000,30000]}
df2 = pd.DataFrame(d2)

print('df1:\n',df1)
print()
print('df2:\n',df2)
print()

print('-------merge-------')
print(pd.merge(df1,df2))
print()

print(pd.merge(df1,df2,how="inner"))
print()

print(pd.merge(df1,df2,how="outer"))
print()

print(pd.merge(df1,df2,how="left"))
print()

print(pd.merge(df1,df2,how="right"))
print()

print('------------------')

# df1:
#    고객명     날짜    데이터
# 0  춘향  2023-01-01  100
# 1  춘향  2023-01-02  200
# 2  몽룡  2023-01-03  300
#
# df2:
#    고객명 데이터  주소
# 0  춘향  여자  경기
# 1  몽룡  남자  서울
# 2  향단  여자  부산

d1 = {'고객명' : ['춘향','춘향','몽룡'],
      '날짜' : ['2023-01-01','2023-01-02','2023-01-03'],
      '데이터' : [100,200,300]}
d2 = {'고객명' : ['춘향','몽룡','향단'],
      '데이터' : ['여자','남자','여자'],
      '주소' : ['경기','서울','부산']}

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

print("df1:\n",df1)
print()
print("df2:\n",df2)
print()


# print(pd.merge(df1,df2))
print(pd.merge(df1,df2,how='inner',on=['고객명'],suffixes=['_1','_2']))
print()


print(pd.merge(df1,df2,how='outer',on='고객명',suffixes=['_1','_2']))
print()

print('-----------------------------------')
# df1:
#     이름  성적
# 0  영희   1
# 1  철수   2
# 2  하니   3
#
# df2:
#     성명  성적2
# 0  영희    4
# 1  하니    5
# 2  윤아    6

d1 = {'이름' : ['영희','철수','하니'],
      '성적' : [1,2,3]}
d2 = {'성명' : ['영희','하니','윤아'],
      '성적2' : [4,5,6]}

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

print("df1:\n",df1)
print("df2:\n",df2)
print()

# print(pd.merge(df1,df2))
print(pd.merge(df1,df2,left_on='이름',right_on='성명'))
print()


print(pd.merge(df1,df2,left_on='이름',right_on='성명').drop('성명',axis=1))
print()

m = pd.merge(df1,df2,left_on='이름',right_on='성명')
print(m[['이름','성적','성적2']])
print()








'''
Created on 2023. 7. 18.

@author: Comi
'''

import pandas as pd
import numpy as np

'''
DataFrame: 2차원 배열 구조
- 행과 열로 이루어짐
- 열 1개가 1개의 Series
'''

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(type(arr))
print(arr.ndim, arr.shape)
print(arr[1][2])

print('-------------------------')

df = pd.DataFrame(arr)
print(type(df))     #pandas.core.frame.DataFrame
print('=== df ===')
print(df)
'''
=== df ===
   0  1  2    #가로: 열 번호
0  1  2  3    #세로: 행 번호
1  4  5  6
'''
print()
print(df.ndim, df.shape)        #2차원 배열, 2행 3열
print('df[2][1]:',df[2][1])     #df[열][행]

print('-------------------------')

d = {'a':[1,3],'b':[1,2],'c':[2,4]}
df2 = pd.DataFrame(d)

print('=== df2 ===')
print(df2)
'''
=== df2 ===
   a  b  c
0  1  1  2
1  3  2  4
'''
print()
print(df2.ndim, df2.shape)        #2차원 배열, 2행 3열

print('-------------------------')

#data: value / index: 행 / columns: 열
df3 = pd.DataFrame(data=[[4,5,6,7],[1,2,3,4]],index=range(0,2),columns=['A','B','C','D'])
print('=== df3 ===')
print(df3)
'''
=== df3 ===
   A  B  C  D
0  4  5  6  7
1  1  2  3  4
'''
print()
print(df3.ndim, df3.shape)        #2차원 배열, 2행 4열

print('-------------------------')

s1 = pd.Series([10,20,30,40])
print('=== s1 ===')
print(s1)
print()

s2 = pd.Series(['A','B','C','D'])
print('=== s2 ===')
print(s2)
print()

df4 = pd.DataFrame([s1,s2])
print('=== df4 ===')
print(df4)
'''
=== df4 ===
    0   1   2   3
0  10  20  30  40    #가로줄 한줄이 하나의 시리즈
1   A   B   C   D
'''
print()
print(df4.ndim, df4.shape)  #2차원 배열, 2행 4열

print('-------------------------')

'''
                Korea        China     Singapore     Vietnam
capital           서울        베이징        싱가포르        하노이
population   51821669   1444216102      5896684     98168829
'''
#방법1
df5 = pd.DataFrame(data=[['서울','베이징','싱가포르','하노이'],
                         [51821669,1444216102,5896684,98168829]],
                   index=['capital','population'],
                   columns=['Korea','China','Singapore','Vietnam'])

#방법2
d = {'Korea':['서울',51821669],'China':['베이징',1444216102],'Singapore':['싱가포르',5896684],'Vietnam':['하노이',98168829]}
df5 = pd.DataFrame(d,index=['capital','population'])

#방법3
d = {'Korea':{'capital':'서울','population':51821669},
     'China':{'capital':'베이징','population':1444216102},
     'Singapore':{'capital':'싱가포르','population':5896684},
     'Vietnam':{'capital':'하노이','population':98168829}}
df5 = pd.DataFrame(d)

print(df5)









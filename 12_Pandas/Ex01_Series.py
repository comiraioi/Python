'''
Created on 2023. 7. 18.

@author: Comi
'''

import pandas as pd
import numpy as np

arr = np.array([10,40,30,20])
print(arr)
print(type(arr))    #numpy.ndarray
print(arr.ndim)
print('-------------------------')

#Series: 1차원 배열 구조로 index와 value로 이루어짐
s1 = pd.Series([10,40,30,20])
print('=== s1 ===')
print(s1)
print()

print(type(s1))             #pandas.core.series.Series
print(s1.ndim, s1.shape)    #1차원 배열, 요소 4개
print(s1.index)             #RangeIndex(start=0, stop=4, step=1): 1~4
print(s1.values)            #[10,40,30,20]
print(s1[1])                #40

print('-------------------------')

#'index=' 생략 가능하나 반드시 values 뒤에 작성
s2 = pd.Series([10,40,30,20],index=['윤아','슬기','조이','웬디'])   #index와 value의 개수가 반드시 일치해야함
print('=== s2 ===')
print(s2)
print()

#values 찾을때 인덱스와 위치번호 모두 사용 가능
print('슬기:',s2['슬기'])     #value 출력
print('1:',s2[1])           #value 출력
print('[1]:',s2[[1]])         #index, value 함께 출력
print()

s2['서현']=70
s2['슬기']=50
print(s2)
print()

#print(s2['슬기','웬디'])    에러 발생
#index 또는 위치번호 여러개로 values를 찾을때는 대괄호로 한번 더 묶어야 함
print(s2[['슬기','웬디']])
print()

print(s2[[1,3]])
print()

print(s2.values)
print(s2.values < 50)       #요소마다 조건별 bool 출력
print()

#조건을 만족하는 index, value 출력
print(s2[s2.values < 50])   
print()

print(s2[s2.index == '웬디'])
print()

print(s2 * 2)   #value 값에 *2
print()

print('서현' in s2)
print('현아' in s2)

print('-------------------------')

d = {'서울':2000, '부산':3000, '울산':4000, '광주':5000}
print(type(d))  #dict
print()

s3 = pd.Series(d)       #딕셔너리의 key와 value가 시리즈의 index와 value가 됨
print('=== s3 ====')
print(s3)
print()

city = ['부산','울산','목포','서울']
s4 = pd.Series(d,city)      #value: d / index: city (인덱스 기준으로 value 설정)      
print('=== s4 ===')
print(s4)
'''
부산    3000.0
울산    4000.0
목포       NaN
서울    2000.0
'''
print()

#NaN이면 True
print(pd.isna(s4))  #isna = isnull
'''
부산    False
울산    False
목포     True
서울    False
'''
print()

#value가 NaN인 index, value 출력
print(s4[pd.isna(s4)])
print(s4[pd.isnull(s4)])
print(s4[pd.notnull(s4) == False])
print()

#NaN이 아니면 True
print(pd.notnull(s4))   #notnull = notna
'''
부산     True
울산     True
목포    False
서울     True
'''
print()

#value가 NaN이 아닌 index, value 출력
print(s4[pd.notna(s4)])
print()
print(s4[pd.isnull(s4) == False])

print('-------------------------')

print('=== s4 ===')
print(s4)
'''
부산    3000.0
울산    4000.0
목포       NaN
서울    2000.0
'''
print()

city = ['부산','대구','울산','목포','서울']
s5 = pd.Series([5,6,np.NaN,1,2],city)    #그냥 NaN을 넣으면 변수로 인식해 에러 발생
print('=== s5 ===')
print(s5)
'''
부산    5.0
대구    6.0
울산    NaN
목포    1.0
서울    2.0
'''
print()

print(s4+s5)    #s4와 s5의 index가 일치하는것끼리 value 더하기
'''
대구       NaN    #s4에 대구가 없으므로 NaN
목포       NaN    #s4의 목포가 NaN이므로 NaN
부산    3005.0
서울    2002.0
울산       NaN    #s5의 울산이 NaN이므로 NaN
'''

print('-------------------------')

'''
=== s2 ===
윤아    10
슬기    50
조이    30
웬디    20
서현    70
'''
s6 = s2.drop(['슬기','서현'])   #s2는 변화 없음
print('=== s6 ===')
print(s6)
print()

s7 = s2[1:4]    #1~3번째
print('=== s7 ===')
print(s7)
print()

s7 = s2[4:1:-1]    #4~2번째
print('=== s7 ===')
print(s7)
print()

s8 = s2['슬기':'웬디']    #슬기~웬디
print('=== s8 ===')
print(s8)
print()

s8 = s2['웬디':'슬기':-1]    #웬디~슬기
print('=== s8 ===')
print(s8)
print()

print('-------------------------')

'''
=== s2 ===
윤아    10
슬기    50
조이    30
웬디    20
서현    70
'''

print('np.max(s2):',np.max(s2))     #values 중 최대값
print('np.min(s2):',np.min(s2))     #values 중 최소값
print('np.sum(s2):',np.sum(s2))     #values의 합
print()

s9 = s2.sort_index()    #오름차순: ascending=True
print('=== s9 ===')
print(s9)
print()

s9 = s2.sort_values(ascending=False)    #내림차순: ascending=False
print('=== s9 ===')
print(s9)


print('-------------------------')

'''
=== s4 ===
부산    3000.0
울산    4000.0
목포       NaN
서울    2000.0
'''
print('=== s4.dropna() ===')
print(s4.dropna())  #value가 NaN인 요소 drop







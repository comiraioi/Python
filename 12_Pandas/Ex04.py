'''
Created on 2023. 7. 19.

@author: Comi
'''

import pandas as pd
import numpy as np

data = [-40,50,50,70,-50,20,20,20,20]
col = ['국어','영어','수학']
idx = ['박보검','홍길동','아이유']
df = pd.DataFrame(np.reshape(data,[3,3]),idx,col)
print(df)
'''
     국어  영어  수학
박보검 -40  50  50
홍길동  70 -50  20
아이유  20  20  20
'''
print()

df = np.abs(df)
print(df)   #음수 양수로 만들기

print('-------------------------')

''' 칼럼별 합
국어    130
영어    120
수학    90
'''
print('sum\n',np.sum(df))   
print()

print(df.apply(np.sum,axis=0)) 
print()

print(df.apply(np.sum,axis='index'))
print()

''' 인덱스별 합
박보검    140
홍길동    140
아이유     60
'''
print(df.apply(np.sum,axis=1))
print()

print(df.apply(np.sum,axis='columns'))

print('-------------------------')

''' 칼럼별 최대값
국어    70
영어    50
수학    50
'''
print(df.apply(np.max))
print()

''' 인덱스별 최소값
박보검    40
홍길동    20
아이유    20
'''
print(df.apply(np.min,axis=1))

print('-------------------------')

 #함수 직접 만들기
 
''' 칼럼별 최대값-최소값
국어    50    #70-20
영어    30    #50-20
수학    30    #50-20
'''
print(df.apply(lambda x : x.max() - x.min()))  
print()

''' 인덱스별 최대값-최소값
박보검    10    #50-40
홍길동    50    #70-20
아이유     0    #20-20
'''
print(df.apply(lambda x : x.max() - x.min(),axis=1))  

print('-------------------------')

df.loc['김연아'] = [11,22,33]  #인덱스(열) 추가
print(df)
'''
     국어  영어  수학
박보검  40  50  50
홍길동  70  50  20
아이유  20  20  20
김연아  11  22  33
'''
print()

#인덱스명 기준 오름차순 정렬
print(df.sort_index())  
print()

#칼럼명 기준 오름차순 정렬
print(df.sort_index(axis='columns'))
print()

#칼럼명 기준 내림차순 정렬
print(df.sort_index(axis=1,ascending=False))

print('-------------------------')

#영어 value 기준 내림차순 정렬
print(df.sort_values(by='영어',ascending=False))  
print()

#영어 value 기준 오름차순 정렬, 영어에 같은 점수가 있으면 수학 기준 오름차순 정렬
print(df.sort_values(by=['영어','수학']))  
print()

#영어 value 기준 오름차순 정렬, 영어에 같은 점수가 있으면 수학 기준 내림차순 정렬
print(df.sort_values(by=['영어','수학'],ascending=[True,False]))  






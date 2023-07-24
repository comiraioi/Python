'''
Created on 2023. 7. 19.

@author: Comi
'''

import pandas as pd
import numpy as np

d = {'도시':['서울','서울','서울','부산','부산'],
     'year':[2000,2001,2002,2001,2002],
     'pop':[1.5,1.7,3.6,2.4,2.9]}

df = pd.DataFrame(d)
print('=== df ===')
print(df)
'''
=== df ===
   도시  year  pop
0  서울  2000  1.5
1  서울  2001  1.7
2  서울  2002  3.6
3  부산  2001  2.4
4  부산  2002  2.9
'''
print()

print("df['pop'][2]:",df['pop'][2])     #3.6
print(df.columns)   #['도시', 'year', 'pop']
print(df.index)     #RangeIndex(start=0, stop=5, step=1)
print(df.values)    #출력할때는 data가 아닌 values로

print('-------------------------')

mycolumn = ['도시','year','pop','income']
myindex = ['one','two','three','four','five']

df2 = pd.DataFrame(data=d,index=myindex,columns=mycolumn)
print('=== df2 ===')
print(df2)

'''
=== df2 ===
       도시  year  pop income
one    서울  2000  1.5    NaN
two    서울  2001  1.7    NaN
three  서울  2002  3.6    NaN
four   부산  2001  2.4    NaN
five   부산  2002  2.9    NaN
'''
print()

print(df2['도시'])    #인덱스와 도시 칼럼 출력 (시리즈)
print()

print(df2.year)     #인덱스와 year 칼럼 출력 (시리즈)
print()

print(df2[['도시','year']])   #인덱스와 도시,year 칼럼 출력 (데이터프레임)
'''
       도시  year
one    서울  2000
two    서울  2001
three  서울  2002
four   부산  2001
five   부산  2002
'''
print()

df2['income'] = [11,12,23,44,59]    #income 칼럼에 data 삽입
print('=== df2 ===')
print(df2)
print()

s = pd.Series([100,200,300],index=['two','four','five'])
print('=== s ===')
print(s)
print()

df2['income'] = s       #index가 일치하는 income 칼럼에 data 삽입
print('=== df2 ===')
print(df2)
'''
=== df2 ===
       도시  year  pop  income
one    서울  2000  1.5     NaN
two    서울  2001  1.7   100.0
three  서울  2002  3.6     NaN
four   부산  2001  2.4   200.0
five   부산  2002  2.9   300.0
'''
print('-------------------------')

print(df2.T)    #행과 열을 바꾸기 (전치)
print()

print(df2.transpose())
print()

print(np.transpose(df2))
'''
         one    two    three    four    five
도시      서울    서울     서울     부산      부산
year    2000   2001    2002    2001     2002
pop      1.5    1.7    3.6      2.4     2.9
income   NaN  100.0    NaN    200.0    300.0
'''

print('-------------------------')

idx = ['one','two','three','four']
col = ['서울','부산','광주','대구']
arr = np.arange(16).reshape([4,4])  #0~15까지 데이터 차례대로 넣기

df = pd.DataFrame(data=arr,index=idx,columns=col)
print('=== df ===')
print(df)
'''
=== df ===
       서울  부산  광주  대구
one      0    1    2    3
two      4    5    6    7
three    8    9   10   11
four    12   13   14   15
'''
print()

#특정 컬럼 출력
print(df[['서울','대구']])  
print()

print(df.reindex(columns=['서울','대구']))   
print()

#특정 인덱스 출력
print(df.reindex(['two','four']))   #'index=' 써도 되고 안써도 됨
print()

#특정 컬럼과 인덱스 출력
print(df.reindex(index=['one','three'],columns=['부산','광주']))

print('-------------------------')

'''
- axis=0은 각 열의 모든 행에 대해서 동작
- axis=1은 각 행의 모든 열에 대해서 동작
'''

#특정 인덱스 삭제
df2 = df.drop(['two','four'])   #'index=','axis=0' 써도 되고 안써도 됨
print('=== df2 ===')
print(df2)
print()

#특정 칼럼 삭제
df2 = df.drop(columns=['부산','대구'],axis=1)   
print('=== df2 ===')
print(df2)
print()

#특정 컬럼과 인덱스 삭제해서 출력
print(df.drop(['two','four']).drop(['서울','대구'],axis=1))

print('-------------------------')

s = pd.Series(['A','B','C','D','E','F','G'],index=[49,48,47,46,2,3,4])
print('=== s ===')
print(s)
'''
=== s ===
49    A
48    B
47    C
46    D
2     E
3     F
4     G
'''
print()

#loc[n]: index의 값이 n인 데이터
print('s[3]:',s[3])
print('s.loc[3]:',s.loc[3])
print('s.loc[:3]\n',s.loc[:3])  #index의 값이 3인 데이터까지

#iloc[n]: n번째 데이터
print('s.iloc[3]:',s.iloc[3])   
print('s.iloc[:3]\n',s.iloc[:3])   #3번째 데이터까지

print('-------------------------')

'''
=== df ===
       서울  부산  광주  대구
one      0    1    2    3
two      4    5    6    7
three    8    9   10   11
four    12   13   14   15
'''

#특정 인덱스 출력
print(df.loc[['two']])  #DataFrame
'''
    서울  부산  광주  대구
two   4   5   6   7
'''
print()

print(df.loc[['two','four']])
print(df.iloc[[1,3]])
'''
      서울  부산  광주  대구
two    4   5   6   7
four  12  13  14  15
'''
print()

#특정 인덱스와 칼럼 출력
print(df.loc[['two','three'],['서울','광주']])
'''
       서울  광주
two     4   6
three   8  10
'''

print('-------------------------')

print(df['부산'] > 5)     #부산 칼럼의 값을 조건 비교하여 bool로 출력
print()

print(df[df['부산'] > 5]) #true 값을 가진 인덱스 전체 출력


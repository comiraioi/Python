'''
Created on 2023. 7. 18.

@author: Comi
'''

import numpy as np

a = np.arange(1,7).reshape([3,2]) 
print(a)
print()

a = np.reshape(np.array(range(1,7)),[3,2])
print(a)
print()

print(a[0][0], a[1][1], a[2][0])
print(a[[0,1,2],[0,1,0]])   #위와 결과 같음

print('---------------------------')

result = a>2
print('result:\n',result)
print()

print(a[a>2])   #True에 해당하는 요소(2보다 큰 요소)만 출력하기

print('---------------------------')

a = np.arange(1,13).reshape([4,3])
print(a)
print()
result = a[1:3]   #1~2행
print('result:\n',result)
print()

result = a[1:3][0]   #1~2행의 0행
print('result:\n',result)
print()

result = a[1:3][0:2]   #1~2행의 0~1행
print('result:\n',result)
print()

result = a[1:3,0]   #1~2행 사이에서 0열에 있는 요소
print('result:\n',result)
print()

result = a[1:3,0:2]   #1~2행 사이에서 0~1열에 있는 요소
print('result:\n',result)

print('---------------------------')

result[1][1] = 100
print('a:\n',a)    #원본도 변화함

acopy = a[1:3,0:2].copy()   
print('acopy:\n',acopy)
acopy[1][1] = 77    #복사본을 바꿔도 원본이 바뀌지 않음
print()

print('acopy:\n',acopy)
print('a:\n',a)






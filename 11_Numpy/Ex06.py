'''
Created on 2023. 7. 18.

@author: Comi
'''

import numpy as np

#repeat
num = 2
rep_cnt = 5
result = np.repeat(num, rep_cnt)    #num을 rep_cnt번 반복해서 numpy.ndarray 생성
print(result)
print(type(result))

print('----------------------------')

arr1 = np.array([1,2])
arr2 = np.array([3,4])
result = arr1 + arr2    #list는 연결 / array는 연산
print(result)
print()

#concatenate: array 연결
result = np.concatenate((arr1,arr2))
print(result)

print('----------------------------')

arr = np.array([1.57,2.48,3.93,4.12])
print(np.ceil(arr))      #올림
print(np.floor(arr))     #버림
print(np.round(arr))     #반올림
print(np.round(arr,1))   #소수점 n번째까지 반올림

print('----------------------------')

arr = np.array([12,33,57,1])
t = np.sum(arr), np.average(arr), np.mean(arr), np.min(arr), np.max(arr)
print(type(t))   #튜플
print(t)
print('t[0]:',t[0])

print('----------------------------')

arr1 = np.array([1.57,2.48,3.93,48.12])
arr2 = np.array([1.57,12.48,3.97,4.12])
print(np.maximum(arr1,arr2))    #maximum: 두 array에서 같은 위치의 요소끼리 비교해 더 큰 값 출력
print(np.minimum(arr1,arr2))    #minimum: 두 array를 같은 위치의 요소끼리 비교해 더 작은 요소 출력








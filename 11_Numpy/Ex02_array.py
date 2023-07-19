'''
Created on 2023. 7. 18.

@author: Comi
'''

import numpy as np

a = np.array([-1,3,2,-6])
b = np.array([3,6,1,2])
c = np.array([1,2,3,6])

L1 = [1,2,3]
L2 = [4,5,6]
print('L1+L2:',L1+L2)   #리스트 연결
print('a+b:',a+b)       #요소끼리 계산됨
print('a*b:',a*b)
ab = np.matmul(a,b) #행렬곱
print('ab:',ab)
print('-------------------')

#배열 차원 바꾸기
A = np.reshape(a,[2,2]) #2행 2열로 배열 형태 변경
print('A:',A)
print(A.shape)
print(A.ndim)
print()

B = b.reshape([2,2])
print('B:',B)
print(B.shape)
print(B.ndim)
print('-------------------')

#배열끼리 연산
print('A+B:\n',A+B)
print('A*B:\n',A*B)
print('-------------------')

#전치 (행과 열의 위치를 바꿈)
B = B.T
print('B:',B)

B = np.transpose(B)
print('B:',B)

print('-------------------')

#a = np.array([-1,3,2,-6])
#2차원으로 형태 변경
a = np.reshape(a,[1,4]) 
print('a:',a)
print(a.shape)
print(a.ndim)
print()

#전치
a = a.T
print('a:',a)
print(a.shape)
print(a.ndim)
print()

#1차원으로 형태 변경
a = np.reshape(a,4) 
print('a:',a)
print(a.shape)
print(a.ndim)




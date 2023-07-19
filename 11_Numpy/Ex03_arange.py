'''
Created on 2023. 7. 18.

@author: Comi
'''

import numpy as np

a = range(5)
print('type:',type(a))
print('a:',a)   #range(0, 5)
for i in a:
    print(i,end=' ')
print()

print('------------------------')

b = np.arange(5)
print('type:',type(b))
print('b:',b)   #[0 1 2 3 4]
for i in b:
    print(i,end=' ')
print()

print('------------------------')

arr = np.arange(3,10)
print('arr:',arr)

arr = np.arange(3,10,2)
print('arr:',arr)

print('------------------------')

c = np.arange(6).reshape([2,3]) #0~5까지 2행 3열 배열로
print(c.ndim,'차원')
print('c:',c)

print('------------------------')

arr1 = [1,2,3,4]
arr2 = [4,3,2,1]
x = np.array(arr1)
y = np.array(arr2)
print('x+y:',x+y)   #[5 5 5 5]

#arange는 범위이므로 안에 배열 객체를 넣을 수는 없음
L1 = np.arange(3)       #[0,1,2]
L2 = np.arange(10,13)   #[10,11,12]
print('L1+L2:',L1+L2)   #[10 12 14]






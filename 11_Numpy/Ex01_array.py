'''
Created on 2023. 7. 18.

@author: Comi
'''

import numpy as np    #수식과 관련된 함수 제공

a=100
print('a:',a)
print('type:',type(a))
print()

arr1 = [1,2,3,4]
print('arr1:',arr1)
print('type:',type(arr1))
print('len:',len(arr1))
print()

arr2 = [[1,2,3,4],[5,6,7,8]]
print('arr2:',arr2)
print('type:',type(arr2))
print('row len:',len(arr2))
print('col len:',len(arr2[0]))
print()

print('-----------------------------------')

np_a = np.array(a)     #a=100

print('np_a:',np_a)
print('type:',type(np_a))  #class 'numpy.ndarray'
print(np_a.ndim,'차원')   #0차원
print(np_a.shape)
print()

np_arr1 = np.array(arr1)  #arr1 = [1,2,3,4]
print('np_arr1:',np_arr1)
print('type:',type(np_arr1))  #class 'numpy.ndarray'
print(np_arr1.ndim,'차원')   #1차원
print(np_arr1.shape)        #요소 개수
print()

np_arr = np.array([[1,2,3,4]])
print('np_arr:',np_arr)
print('type:',type(np_arr))  #class 'numpy.ndarray'
print(np_arr.ndim,'차원')   #2차원
print(np_arr.shape)        #(1행,4열)
print()

np_arr2 = np.array(arr2)  #arr2 = [[1,2,3,4],[5,6,7,8]]
print('np_arr2:',np_arr2)
print('type:',type(np_arr2))  #class 'numpy.ndarray'
print(np_arr2.ndim,'차원')     #2차원
print(np_arr2.shape)          #(2행,4열)
print(np_arr2.shape[0],np_arr2.shape[1])    #2행 4열

for i in range(np_arr2.shape[0]):
    for j in range(np_arr2.shape[1]):
        print(np_arr2[i][j],end=' ')
    print()
print()






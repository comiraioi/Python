'''
Created on 2023. 7. 18.

@author: Comi
'''

import numpy as np

list1 = [0,1,2,3,4,5,6,7,8,9]
arr1 = np.array(list1)
arange1 = np.arange(10)

print('list1:',list1)
print('arr1:',arr1)
print('arange1:',arange1)
print()

print('list1[5]:',list1[5])
print('arr1[5]:',arr1[5])
print('arange1[5]:',arange1[5])
print()

print('list1[5:8]:',list1[5:8])
print('arr1[5:8]:',arr1[5:8])
print('arange1[5:8]:',arange1[5:8])
print()

print('list1[3:-2]:',list1[3:-2])
print('arr1[3:-2]:',arr1[3:-2])
print('arange1[3:-2]:',arange1[3:-2])
print()

print('list1[3::2]:',list1[3::2])
print('arr1[3::2]:',arr1[3::2])
print('arange1[3::2]:',arange1[3::2])
print()

print('list1[::2]:',list1[::2])
print('arr1[::2]:',arr1[::2])
print('arange1[::2]:',arange1[::2])

print('----------------------------------------')

#위치를 지정할때는 넣고 싶은 요소의 형태로
list1[5] = [12]     #리스트 행태로 삽입됨
print(list1)        #[0, 1, 2, 3, 4, [12], 6, 7, 8, 9]

list1[5] = 12       #[0, 1, 2, 3, 4, 12, 6, 7, 8, 9]
print(list1)

list1[5:8] = [33]   #범위를 지정할때는 리스트 형태로 (대괄호로 반드시 묶어야 함)
print(list1)        #[0, 1, 2, 3, 4, 33, 8, 9]

print('----------------------------------------')

arr1[5] = 12    #배열 형태로 넣을 수 없음(에러 발생)
print(arr1)     #[ 0  1  2  3  4 12  6  7  8  9]

arr1[5:8] = [33]    #대괄호 상관없음
print(arr1)         #[ 0  1  2  3  4 33 33 33  8  9]

print('----------------------------------------')

arange1[5] = 12    #배열 형태로 넣을 수 없음(에러 발생)
print(arange1)     #[ 0  1  2  3  4 12  6  7  8  9]

arange1[5:8] = 33   #대괄호 상관없음
print(arange1)      #[ 0  1  2  3  4 33 33 33  8  9]

print('----------------------------------------')

list1 = [0,1,2,3,4,5,6,7,8,9]
arr1 = np.array(list1)
arange1 = np.arange(10)
print(list1)
print(arr1)
print(arange1)
print()

list1_slice = list1[5:8]
arr1_slice = arr1[5:8]
arange1_slice = arange1[5:8]
print(list1_slice)
print(arr1_slice)
print(arange1_slice)
print()

list1_slice[1] = 100
print(list1_slice)
print(list1)    #원본 리스트는 바뀌지 않음
print()

arr1_slice[1] = 100
print(arr1_slice)
print(arr1)     #원본 리스트도 바뀜
print()

arange1_slice[1] = 100
print(arange1_slice)
print(arange1)  #원본 리스트도 바뀜
print()



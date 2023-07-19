'''
Created on 2023. 7. 14.

@author: Comi
'''

'''
별 찍기
*
**
***
****
*****
'''
#방법1
for i in range(6):
    for j in range(i):
        if j <= i:
            print('*',end='')
    print()
print()

#방법2
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*',end='')
    print()
    
#방법3
for i in range(6):
    print('*'*i)    #문자열 반복 활용
print()

print('----------------')

#구구단 세로 출력
for i in range(2,10):
    print('***',i,'단','***')
    for j in range(1,10):
        print(i,'*',j,'=',(i*j))
        
print('----------------')    

#구구단 가로 출력
for j in range(1,10):
    for i in range(2,10):
        print(i,'*',j,'=',(i*j),end='\t')
    print()
    
    
    
    
'''
Created on 2023. 7. 18.

@author: Comi
'''

import numpy as np

#random: 난수 발생 
rd = np.random.random()
print(rd)               # 0<= x < 1 (실수 난수)
print(rd*10)            # 0<= x < 10 (실수 난수)

#0~9 정수 난수
#print(int(np.floor(rd*10)))
print(int(rd*10))      

#int(rd*(끝수-시작수+1))+시작수
#3~9 정수 난수 
print(int(rd*10)+3)     

#10~57 정수 난수
print(int(rd*48)+10)  

print('-----------------------------------')

#permutation: 정수 난수 n개 리스트 형태로 중복 없이 발생
a = np.random.permutation(10)       #0~9
print(a)

b = np.random.permutation(10)+3     #3~12
print(b)

print('-----------------------------------')

import random
c = random.randrange(1,10,2)    #1,3,5,7,9 중 난수 1개 발생
print(c)

print('-----------------------------------')

'''
lottoNum = 1~45 정수 난수 중복안되게 6개 발생
my = 내가 6번 입력 [32,32] 

1~45사이의 수 입력:32
1~45사이의 수 입력:32
이미 입력한 수입니다.
1~45사이의 수 입력:89
1~45사이의 수 입력해야합니다.
1~45사이의 수 입력:2
1~45사이의 수 입력:1
1~45사이의 수 입력:r
숫자로 입력하세요
1~45사이의 수 입력:11
1~45사이의 수 입력:24
1~45사이의 수 입력:31
'''

#<class 'int'>

print('=== 로또 맞추기 ===')
myList = []
lottoList = []
check = 0
'''
방법1: randint
for i in range(6):
    lottoNum = random.randint(1,45)
    while lottoNum in lottoList:
        lottoNum = random.randint(1,45)
    lottoList += [lottoNum]
    
방법2: sample
for i in range(6):
    lottoNum = random.sample(range(1,45),6)
    lottoList += [lottoNum]
'''
#방법3: randrange
while len(lottoList) != 6:
    lottoNum = random.randrange(1,46)
    if lottoNum not in lottoList:
        lottoList.append(lottoNum)
print("로또 번호:",lottoList)

while True:
    if len(myList)==6:
        break
    else:
        try:
            myNum = int(input('1~45 사이의 수 입력: '))
            if(myNum < 1 or myNum > 45):
               raise TypeError
            if myNum in myList:
                raise NameError
        except ValueError :
            print('숫자를 입력하세요.')
        except TypeError :
             print('1~45 사이의 수를 입력해야합니다.')
        except NameError :
              print('이미 입력한 수 입니다.')
        else:
            myList += [myNum]
print("입력한 수:",myList)

'''
방법1
for i in range(len(myList)):
    if myList[i] in lottoList:
        check += 1
'''
#방법2
for i in lottoList:
    for j in myList:
        if i == j:
            check += 1
            break

if check == 6:
    print('1등')
elif check == 5:
    print('2등')
elif check == 4:
    print('3등')
else:
    print('꽝')











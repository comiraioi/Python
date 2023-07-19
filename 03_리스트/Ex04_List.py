'''
Created on 2023. 7. 14.

@author: Comi
'''

from dask.array.ma import average

#리스트 전체 요소 출력하기
kor = [70,80,90]
#방법1
for i in range(len(kor)):
    print(kor[i],end='점 ')
print()

#방법2
for i in kor:
    print(i,end='점 ')
print()

print('----------------------------------')

#2차원 리스트
L = [['a','b'],[1,2,3]]
print('L:',L)
print('L[0]:',L[0])
print('L[1]:',L[1])
print('L[0][0]:',L[0][0])
print('L[1][2]:',L[1][2])
print('len(L):',len(L))

print('---------------')

#2차원 리스트 출력하기(행,열)
#방법1
for i in L:
    for j in i:
        print(j,end=' ')
    print()
print()

#방법2
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j],end=' ')
    print()
    
print('-------------------------------------')
    
#직사각형 2차원 리스트 언패킹
L = [[10, 20], [30, 40], [50, 60]]
for x, y in L:  #리스트의 가로 한 줄(안쪽 리스트)에서 요소 두 개를 꺼냄
 print(x,y)

print('-------------------------------------')

#리스트에 리스트 삽입하기
s = [1,2,3]
t = ['begin','end']
t[1:1] = s      #1차원 리스트
print('t:',t)

s = [1,2,3]
t = ['begin',s,'end']   #2차원 리스트
print('t:',t)
print('t[0]:',t[0])
print('t[0][0]:',t[0][0])   #문자열도 리스트처럼 인식

s = [1,2,3]
t = ['begin','end']
t.insert(1,s)
print('t:',t)

print('---------------------------------------------')

#3차원 리스트(면,행,열)
L = [1,
        ['a',
            ['x','y','z'],
        'b','c'],
    7]
print('L:',L)
print('L[0]:',L[0])
print('L[1]:',L[1])
print('L[2]:',L[2])
print('L[1][1]:',L[1][1])
print('L[1][1][1]:',L[1][1][1])

print('---------------------------------------------')

L1 = []
for i in range(10):
    L1.append(i**2)
print('L1:',L1)

L2 = [i**2 for i in range(10)]

print('L2:',L2)

print('---------------------------------------------')

L1 = [1,2,3]
L2 = ['a','b']

for x in L1:
    for y in L2:
        print(x,y,end=' ')
    print()
print()

#2차원 리스트 생성하기
L3 = [[x,y] for x in L1 for y in L2 ]
print('L3:',L3)

print('---------------------------------------------')
        
jumsu = [89,32,12,43,99]
print('합:',sum(jumsu))
print('최대:',max(jumsu))
print('최소:',min(jumsu))
print('평균:',sum(jumsu)/len(jumsu))
print('평균:',average)

for a,b in enumerate(jumsu) :
    print(a,'/',b)

#튜플로 결과가 나옴
for a in enumerate(jumsu) :
    print(a)
print()



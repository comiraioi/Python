'''
Created on 2023. 7. 14.

@author: Comi
'''

#1~10까지 정수를 담는 리스트 생성 후 모든 요소 출력하기
#방법1
l = list(range(1,11))
for i in range(len(l)):
    print(l[i],end=' ')
print()

#특정 위치에 요소 추가하기
#3과 4 사이에 11 추가하기
l[3:3] = [11]
print(l)
#l[2] 위치에 15 추가하기
l.insert(2,15)  #insert(인덱스,요소)
print(l)
#4를 지우고 그 자리에 12 추가하기
l[4:5] = [12]
print(l)
#마지막에 요소 추가하기
#방법1
l[len(l):len(l)] = [13]
print(l)
#방법2
l.append(13)
print(l)

#요소 삭제하기
l.pop(2)    #pop(인덱스)
print(l)

l.remove(13) #remove(요소값): 같은 요소가 여러개면 가장 앞의 요소만 삭제됨
print(l)

print('------------------------------------------------')

#정수 5개를 입력받아 리스트에 넣기
#방법1: insert
x = []
for i in range(5):
    x.insert(i,int(input('숫자 입력: ')))
print(x)
#방법2: append
y = []
for i in range(5):
    y.append(int(input('숫자 입력: ')))
print(y)
#방법3: +로 리스트 연결
z = []
for i in range(5):
    z += [int(input('숫자 입력: '))]
print(z)
    


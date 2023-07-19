'''
Created on 2023. 7. 14.

@author: Comi
'''

L = [10,20,30,40,10]
#index(value): 요소의 위치
print('L.index(10):',L.index(10))
print('L.index(20):',L.index(20))
#count(value): 요소의 개수
print('L.count(10):',L.count(10))
#리스트.reverse(): 리스트의 요소 역순 정렬
L.reverse()
print(L)
#리스트.sort(): 리스트의 요소 오름차순 정렬
L.sort()
print(L)
#리스트.sort(reverse=True): 내림차순 정렬
L.sort(reverse=True)
print(L)
#리스트 = sorted(리스트): 정렬한 값을 리스트에 넣어주어야 함
L = sorted(L)
print(L)

print('------------------------------------------------')

#문자열 정렬: 알파벳순
fruit = ['orange','apple','grape','banana']
fruit.reverse()
print('fruit:',fruit)
fruit.sort()
print('fruit:',fruit)

print('------------------------------------------------')

#숫자 형식의 문자열 정렬: 큰 자리 수 기준 정렬
num = ['172','34','269','1345']
num.sort()
print('num:',num)
#int형처럼 정렬하기
num.sort(key=int,reverse=True)
print('num:',num)
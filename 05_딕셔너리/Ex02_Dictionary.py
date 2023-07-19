'''
Created on 2023. 7. 14.

@author: Comi
'''

p1 = {'kim':33, 'park':44, 'choi':55}
print(p1)

#key로 value 가져오기
print('park:',p1['park'])
#print('jung:',p1['jung'])    => 해당 key가 없으므로 에러 발생

print('park:',p1.get('park'))
print('jung:',p1.get('jung'))   #None

p2 = {'kim':77, 'lee':88, 'hong':99}
p1.update(p2)   #일치하는 키가 있으면 값 변경/일치하는 키가 없으면 삽입/그 외 기존 요소 유지
print('p1:',p1)

p2.clear()  #요소 전부 지우기
print('p2:',p2)
del p2  #딕셔너리 객체를 지우기

del p1['park']  #키로 요소 지우기
print('p1:',p1)

print('-----------------------------------------')

#key만 출력하기
#방법1
for i in p1:
    print(i,end=' ')
print()
#방법2
print(p1.keys())

print('-----------------------------------------')

#value만 출력하기
#방법1
for i in p1.values():
    print(i,end=' ')
print()
#방법2
print(p1.values())

print('-----------------------------------------')

#딕셔너리 반복문으로 출력하기
for i in p1.items():
    print(i[0],':',i[1], i)

print('-----------------------------------------')

#단어에 엔터 입력할떄까지 단어, 뜻을 입력받고 딕셔너리에서 단어 검색하기
d = dict()
while True:
    word = input('단어: ')
    if word == '':
        break
    mean = input('뜻: ')
    d[word] = mean
print()
while True:
    flag = False
    search = input('단어 찾기(중지는 stop 입력): ')
    if search.lower() == 'stop':
        print('단어 검색을 마쳤습니다.')
        break
    for key in d:
        if key.lower() == search.lower():
            print('찾는 단어의 뜻은',d.get(key),'입니다.')
            flag = True
            break
    if flag == False :
        print('찾는 단어가 없습니다.')
            
            
        
    
    
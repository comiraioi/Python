'''
Created on 2023. 7. 14.

@author: Comi
'''

'''
딕셔너리: 딕셔너리 = {키1:값1, 키2:값2, ..., 키n:값n}    => 자바의 map과 유사함
    - 값의 순서는 없음
    - key와 value는 항상 1:1로 지정함
    - 딕셔너리의 key와 value에 자료형을 섞어서 사용할 수 있음
    - 단, 리스트와 딕셔너리는 수정이 가능하기 때문에 key로 사용할 수 없음
'''

d = {'one':'하나','two':'둘','three':'셋'}
print(type(d))
print(d)

#key로 value 찾기
print('two:',d['two'])

d['one'] = 1    #존재하는 키면 값이 수정됨
print(d)
d['four']='넷'   #없는 키면 값이 추가됨
print(d)

print('len:',len(d))
print("len(d['four']):",len(d['four'])) #value의 길이 = 문자열 길이

print('one' in d)   #True (키 존재)
print('둘' in d)     #False (값은 있지만 키로 존재하지 않음)

print(d.keys())
print(d.values())
print('둘' in d.values())

print(d.items())    #key와 value를 튜플로 묶고 전체를 리스트로 출력하기

print("------------------------------")

d={}
w1 = "hello"
w2 = "world~"
d[w1] = len(w1)
d[w2] = len(w2)
print(d)

print("------------------------------")

d = dict(one=1,two=2)
print(d)

d = dict([['one',1],['two',2]])
print(d)

print("------------------------------")

#이름에 엔터 입력할떄까지 이름, 점수를 입력받아 딕셔너리와 점수의 합 출력
d = dict()
while True:
    name = input('이름: ')
    if name == '':
        break
    score = int(input('점수: '))
    d[name] = score
print(d)
print('합계:',sum(d.values()))

print(d.items())
for i,j in d.items():
    print('이름:',i,'점수:',j)




'''
Created on 2023. 7. 14.

@author: Comi
'''

'''
#튜플: 튜플 = ()
    - 순서가 있는 데이터의 나열
    - 서로 다른 종료의 데이터 타입도 하나로 묶을 수 있음
    - 내부 요소의 값을 변경할 수 없음
'''

t = (1,2,3,4,5)
print(type(t))
print('t:',t)
print('t[-1]:',t[-1])
print('len(t):',len(t))
print(3 in t)
print(t[0:2])
print(t[::2])

for i in range(len(t)):
    print(t[i],end=' ')
print()

for i in t:
    print(i,end=' ')
print()

print("--------------------------")

#튜플
t1 = ()
t2 = (1,2,3)
t3 = 1,2,3
t4 = (1,)
t5 = 1,
#int
t6 = (1)
t7 = (1)

print(t1,type(t1))
print(t2,type(t2))
print(t3,type(t3))
print(t4,type(t4))
print(t5,type(t5))
print(t6,type(t6))
print(t7,type(t7))

print("---------------------------------")

#튜플에 튜플 연결하기
t1 = (1,2,3)
t2 = t1 + ('kim','park')    #1차원 튜플
print('t2:',t2)

t1 = (1,2,3)
t2 = t1,('kim','park')  #2차원 튜플
print('t2:',t2)
print('t2[0]:',t2[0])
print('t2[1][1]:',t2[1][1])
print('kim' in t2)

print("----------------")

x,y,z = 1,2,3
print(x,y,z)

x,y = y,x
print(x,y)

t = (1,2,'hi') #패킹
print('t:',t)

x,y,z = t   #언패킹
print(x,y,z)

print("-----------------------")

#튜플의 요소를 변경하기 위해서는 리스트로 변환해야함
t = (1,2,3)
t = list(t)
t[1]=100
tuple(t)
print('t:',t)

print("-----------------------")

#서식문자의 데이터는 튜플로 묶는다
print('id: %s / pw: %s' % ('kim','1234'))

print("-----------------------")

#함수 정의하기
'''
자바
funcion abc(){

}
'''
def calc(a,b):
    return a+b,a-b,a*b  #파이썬은 여러 개 반환 가능

plus,minus,multi = calc(10,20)
print('plus:',plus)
print('minus:',minus)
print('multi:',multi)

result = calc(10,20)    #튜플 형식으로 담김
print('result:',result)


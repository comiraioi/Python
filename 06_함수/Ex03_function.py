'''
Created on 2023. 7. 14.

@author: Comi
'''

#전역변수
x=10    
def func1():
    #지역변수: 함수 외부에서는 사용 불가능
    x=20
    x=x+3
    y=30
    print('x:',x,'/ y:',y)
    
func1() #전역변수와 지역변수명이 동일할경우 지역변수 우선
print('x:',x)   #전역변수 출력됨

print('---------------------')

def func2():
    global x    #global: 전역변수를 사용할때
    x=x+3
    y=30
    print('x:',x,'/ y:',y)
    
func2()
print('x:',x)   #함수의 x값 출력됨

print('---------------------')

def func3(x):
    return x ** 2;
print(func3(8))

#lambda 함수: 간단한 함수 정의 시 사용함 => lambda 매개변수:반환값
a = lambda x : x**2
print(a(8))
print(type(a))

print('---------------------')

b = lambda x,y : x+y
print(b(2,4))




'''
Created on 2023. 7. 14.

@author: Comi
'''

def minus(a,b):
    return a-b
print(minus(20,7))
print(minus(b=20,a=7))  #매개변수 변수명 지정 가능

print('---------------------')

def func1(x=1,y=2,z=3):     #넘어온 매개변수가 없으면 준비된 값 사용, 있으면 보낸 값 사용
    return x+y+z

print('func1():',func1())
print('func1(1):',func1(1))
print('func1(1,2):',func1(1,2))
print('func1(1,2,3):',func1(1,2,3))

print('---------------------')

def func2(*v):     #변수 앞에 *을 붙이면 모든 매개변수 형식을 받음
    #print(v,type(v))    #튜플 형식으로 출력하기
    for i in v:
        print(i,end=' ')    #전달 인자만 출력하기
    print()

#모두 퓨플 형태임
func2()
func2(1,2)
func2(1,2,3,4,5)
func2([1,2,3],(4,5,6))
func2("apple","banana","orange")

print('---------------------')

def func3(a, *v):     
    for i in v:
        print(i,end=' ')    
    print()

#func2()    #a에 매개변수가 들어오지 않아 오류 발생
func3(1,2)
func3(1,2,3,4,5)
func3([1,2,3],(4,5,6))
func3("apple","banana","orange")

print('---------------------')

tp = 10,20,30
a,b,c = tp
print(a,b,c)

def func4(x,y,z):
    print(x,y,z)

#func4(tp) 튜플의 요소가 각각 매개변수에 들어가지 않고 튜플 객체가 x에 들어가 오류 발생
func4(*tp)

print('---------------------')

d = {'a':1,'b':2,'c':3}
def func5(a,b,c):
    print(a,b,c)

#func5(d) 딕셔너리의 요소가 각각 매개변수에 들어가지 않고 딕셔너리 객체가 x에 들어가 오류 발생
func5(*d) #매개변수에 딕셔너리의 key가 넘어감
func5(**d) #딕셔너리의 키와 매개변수명이 동일하면 매개변수에 딕셔너리의 value가 넘어감 (변수명이 동일하지 않으면 오류 발생)

print('---------------------')

#재귀호출
def recursive(x):
    if x == 1:
        return 1
    return x + recursive(x-1)
        
print(recursive(10))    #10+9+...+2+1









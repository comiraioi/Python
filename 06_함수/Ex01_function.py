'''
Created on 2023. 7. 14.

@author: Comi
'''

#함수 정의
def abc():
    print('하하하')
    print('호호호')
    #return : void면 안써도 됨

#함수 호출
abc()
print('--------------')
print('abc():',abc())   #void 형식이면 None

print('---------------------')

def add(a,b):
    return a+b

print('add():',add(10,20))

result = add(1.1, 2.2)
print('result:',result)

print([10,11]+[20,21])  
print(add([10,11],[20,21]))     #리스트 연결

print('---------------------')

#함수를 정의할 때 비워두고 싶으면 반드시 pass 작성해야함
def simple() :
    pass

print('simple():',simple()) #None

print('---------------------')

def myabs(x):
    if x < 0:
        x = -x
    return x

def addabs(a,b):
    c = add(a,b)
    return myabs(c)     #return에 다른 함수 호출 가능

print('addabs(-5,-7):',addabs(-5,-7))

print('---------------------')

def calc(x,y):
    return x+y,x-y,x*y,x/y  #여러 개 반환 가능 => 튜플형태로 출력됨

result = calc(13,5)
print('result:',result)
print('result[0]:',result[0])

plus,minus,multi,divide = calc(13,5)
print('plus:',plus)

print('---------------------')

'''
자바
switch(변수, 수식){
    case :
    default :
}
'''
def func(x):
    return{
        'a':1,  #매개변수가 'a'면 1 return
        'b':2,  #매개변수가 'b'면 2 return
    }.get(x,9)  #그 외는 9 return
    
print("func('a'):",func('a'))
print("func('b'):",func('b'))
print("func('c'):",func('c'))

print('---------------------')










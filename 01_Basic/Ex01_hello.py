'''
Created on 2023. 7. 14.

@author: Comi
'''

# 큰 따옴표, 작은 따욤표 구분하지 않음
print('오늘은'+'즐거운'+'수요일')
print("오늘은 "+"즐거운 "+"수요일",sep="~")

# 구분자는 쉼표(공백)로 연결한 곳에만 들어감
print('오늘은','즐거운','수요일\n',sep="~")

print("12"+"34")
print(12+34)
print(12+int("34"))     #int(): str을 int로
print(str(12)+"34\n")     #str(): 숫자 타입을 str로

#문자열 반복 출력
print("*!#" * 3)
print("\n")

print(15/6)             #정수 나누기 정수 => 소수점 이하도 출력됨 (자바는 정수만 출력)
print(15//6)            #정수만 출력
print(15%6)             #나머지 출력
print(divmod(15,6))     #튜플 형태로 출력
print("\n")

#서식 문자
print("%d / %d = %d" % (10,3,10/3))     #%d는 정수로 결과 출력
print("%d / %d = %f" % (10,3,10/3))     #%f는 소수점 이하도 출력
print("%d / %d = %.2f" % (10,3,10/3))
print("\n")

a=10
b=3
c="abc"

print(type(a))
print(type(b))

a += 1      #파이썬은 a++ 불가능
print("a: ",a)
a = 10
a = a ** b;     #a의 b제곱
print("a: ",a,"\n")

print( (a>0) and (b>0) )
print( (a>0) and (b<0) )
print( (a>0) or (b<0) )
print( not((a>0) or (b<0)) )    #not 연산자 (자바의 !)



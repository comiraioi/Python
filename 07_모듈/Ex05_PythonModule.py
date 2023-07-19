'''
Created on 2023. 7. 14.

@author: Comi
'''

#내장 함수 
print(max(50,99,13,100,87)) #최대값
print(min(50,99,13,100,87)) #최소값
print(abs(-3))  #절대값
print(pow(2,3)) #a의 b승
print(round(2.5))   #반올림
print(round(2.7))
print(round(3.14567,3)) #반올림해서 소수점 3번째 자리까지 출력
print(round(98513.14568,-3)) #1의 자리(=-1),10의 자리(=-2),... 해당 자리에서 반올림

print('----------------------------')

#파이썬 표준 라이브러리: https://docs.python.org/ko/3/library/

#math 모듈
import math
print(math.pi)
print(math.factorial(5))

from math import factorial as f
print(f(5))

from math import *
print(factorial(5))

print('----------------------------')

#datetime 모듈: 모듈 안에 datetime 클래스가 있고 그 안에 함수가 내장되어 있음
import datetime
print(datetime.datetime.now())    #모듈명.클래스명.함수명

from datetime import *  
print(datetime.now())   #클래스명.함수명

now = datetime.now()
#어트리뷰트
print('연:',now.year)
print('월:',now.month)
print('일:',now.day)
print('시:',now.hour)
print('분:',now.minute)
print('초:',now.second)
print('%d-%d-%d' % (now.year,now.month,now.day))

#정수 반환 (월:0, 화:1, 수:2, ... , 토:7)
print('요일:',datetime.weekday(datetime.now()))
print('요일:',now.weekday())

def yoil(date):
    l = ['월','화','수','목','금','토','일']
    for i in range(7):
        if datetime.weekday(date) ==  i:
            return l[i]
        
print(yoil(datetime.now()))

def func(x):
    return{
        0:'월요일',
        1:'화요일',
        2:'수요일',
        3:'목요일',
        4:'금요일',
        5:'토요일',
        # 6:'일요일'
        }.get(x, '잘못된 숫자')
now2 = datetime.weekday(date(now.year,now.month,now.day))
print(func(now2))
    
print(func(now.today().weekday()))









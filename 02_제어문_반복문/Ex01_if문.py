'''
Created on 2023. 7. 14.

@author: Comi
'''

print('su 입력:',end=' ')
su = int(input())

if su % 2 == 0 :
    pass
print('su='+str(su))

if su % 2 == 0 : 
    print('짝수입니다.')
else :
    print('홀수입니다.')
print('하하하')

print('------------------')

score = int(input('점수를 입력하세요: '))
if(score>=90) :
    print('A학점')
elif(score>=80) :    #elif는 80<=score<90로 쓰지 않아도 됨
    print('B학점')
elif(score>=70) :
    print('C학점')
elif(score>=60) :
    print('D학점')
else :
    print('F학점')
    
print('------------------')

season = 'suMmEr'
print(season)
print(season.upper())       #전부 대문자
print(season.lower())       #전부 소문자
print(season.capitalize())  #첫글자만 대문자, 나머지는 소문자
print(season.isupper())

season = season.lower()
if season == 'summer' :     #문자열 비교 == / 자바는 .equals()
    a = 10
elif season == 'winter' :
    a = 20
else :
    a = 30
print('a:',a)



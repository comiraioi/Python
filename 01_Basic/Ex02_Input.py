'''
Created on 2023. 7. 14.

@author: Comi
'''

print('a의 값을 입력하세요:',end=' ')
a = input()
print('b의 값을 입력하세요:',end=' ')
b = input()

#input한 값의 타입은 문자열 => a+b는 연산이 아니라 문자열 연결이 됨
print(a,"더하기",b+"은",str(int(a)+int(b))+"입니다.")
print("%d 더하기 %d은 %d입니다." % (int(a),int(b),int(a)+int(b)))  #서식문자 %d는 숫자만 받음
#format
print("{} 더하기 {}은 {}입니다.".format(a,b,int(a)+int(b)))
print("{1} 더하기 {0}은 {2}입니다.\n".format(a,b,int(a)+int(b)))     #{}안에 위치 작성 (0부터 시작)

print('x 입력:',end='')
x = int(input())
print('y 입력:',end='')
y = int(input())
print(str(x)+'+'+str(y)+'='+str(x+y))   #'+'는 같은 타입끼리만 사용 가능
print(x,'+',y,'=',(x+y))                #','는 타입이 달라도 사용 가능

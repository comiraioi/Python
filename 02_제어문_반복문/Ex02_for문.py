'''
Created on 2023. 7. 14.

@author: Comi
'''

for i in range(1,10,3):
    print(i,end=' ')
print()
    
for i in range(1,5):    #증가폭 설정 안하면 1씩 증가
    print(i,end=' ')
print()
    
for i in range(5):    #시작 설정 안하면 0부터
    print(i,end=' ')
    
print('\n-----------------------')

#1~10까지 합 출력
total = 0
for i in range(11):
    total += i
print('total:',total)
print('1부터 10까지의 합: %d' % (total))
print('1부터 10까지의 합: {}'.format(total))

print('-----------------------')

#5부터 1까지 출력
for i in range(5,0,-1):
    print(i,end=' ')
    
print('\n-----------------------')

#10부터 1까지 1씩 감소하면서 짝수,홀수 합 구하기
even = 0
odd = 0
for i in range(10,0,-1):
    if i % 2 == 0 :
        even += i
    else :
        odd += i
print('짝수의 합:',even)
print('홀수의 합:',odd)

print('-----------------------')

for i in range(5):
    if(i > 2):
        break
    print(i,end=' ')
print('\nfor문 밖')


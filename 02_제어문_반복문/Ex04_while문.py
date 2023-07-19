'''
Created on 2023. 7. 14.

@author: Comi
'''

total = 0
i = 1
while i < 11:
    total += i
    i += 1
print('total:',total)

#단을 입력받아 구구단 출력하기
dan = int(input('단 입력: '))
i = 1
while i <= 9:
    print(f"{dan} * {i} = {dan * i}")   #print('{}*{}={}'.format(dan,i,dan*i))
    i += 1
    
print('----------------') 
    
#세로로 구구단 출력
i = 2
while i <= 9:
    j = 1
    print('***',i,'단','***')
    while j <=9:
        print(i,'*',j,'=',(i*j))
        j += 1
    i += 1
    
print('----------------')

i=1
total=0
while True:         #파이썬의 boolean 첫글자는 대문자로 작성
    total += i
    i += 1
    if total>30 :
        break;
print('i:',i)
print('total:',total)

print('----------------')

#음수를 입력할 때까지 점수를 입력받아 합계, 평균 구하고 평균의 십의 자리수만큼 별 찍기
i=0
sum = 0
while True:
    score = int(input('점수 입력: '))
    if score < 0:
        break
    sum += score
    i += 1
avg = sum/i
print('반복 횟수:',i)
print('합계:{}'.format(sum))
print('평균: %.2f'% avg)
print('평균: {:.2f}'.format(avg))
print('*' * int(avg/10))
    
    
    
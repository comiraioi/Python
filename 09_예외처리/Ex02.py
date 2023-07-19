'''
Created on 2023. 7. 17.

@author: user
'''
# 숫자1 : 32 
# 숫자2 : 11
#
# 숫자대신 문자를 입력하면 값이 적절하지 않습니다 출력
#
# 덧셈 : 43

try :
    su1 = int(input('숫자1 : '))
    su2 = int(input('숫자2 : '))
    # print('덧셈 :',su1+su2)
except ValueError :
    print('값이 적절하지 않습니다.')

else :
    total = su1 + su2
    print('덧셈 :',str(total))
    
print('--------------------------')    
    
    
# 없으면 파일 없음 출력
# 있으면 파일내용 읽어서 출력
try:    
    f = open('test.txt','r')
except FileNotFoundError as err:
    print('파일 없음:',err)
else :
    print(f.read())          
    f.close()    
finally:
    print('finally')
    
print('--------------------------') 

try :
    su1 = int(input('숫자1 : '))
    su2 = int(input('숫자2 : '))  
    
    if su1<0 or su2<0 :
        raise ArithmeticError('음수 입력함')

except ArithmeticError as err :
    print('예외발생:',err)
else :
    print('두 수 모두 양수입력됨')      
    
    
    
    
    
    
    

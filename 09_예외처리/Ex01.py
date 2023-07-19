'''
Created on 2023. 7. 17.

@author: user
'''

x=4
y=2
L = [1,2,3]
try:
    print(x/y)
    print(L[4])
    
except ZeroDivisionError as err:
    print('ZeroDivisionError 발생 :' ,err)

except IndexError  as err :
    print('IndexError 발생 :' ,err)

except :
    print('except')    
else:
    print('else는 try에 아무 문제 없음')  
finally :
    print('finally')    
          
print('예외처리 공부중')


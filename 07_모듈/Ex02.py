'''
Created on 2023. 7. 14.

@author: Comi
'''

#Ex02.py
def display():
    for i in range(5):
        print(i,end=' ')
    print()
    
#모듈 호출 시 출력 조건 설정
if __name__ == '__main__' :  #직접 실행하는 곳(Ex02)에서만 출력
    print('모듈 공부중')
    display()
    print('모듈 공부중2')
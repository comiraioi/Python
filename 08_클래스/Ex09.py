'''
Created on 2023. 7. 17.

@author: user
'''
class NumBox :
    def __init__(self,num):
        self.num = num
    
    def __add__(self,num):
        self.num += num
        return '__add__ : ' + str(self.num)
    
    def __radd__(self,num):
        self.num += num
        return '__radd__ : ' + str(self.num)
    
    def __sub__(self,num):
        self.num -= num
        return '__sub__ : ' + str(self.num)
        
print(1+2)    
print("ab"+"cd")    
print(str(12)+"ab")    
print(12+int("34"))    
print()
su1 = NumBox(40)
print(su1.num)
print(su1.num+11)
print(11+su1.num)
print(su1 + 20) # 참조변수+숫자 연산자 오버로딩
print(20 + su1) # 숫자+참조변수

print(su1.num-50)
print(su1-50)


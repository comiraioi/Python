'''
Created on 2023. 7. 17.

@author: user
'''
class Student :
    name = "철수"
    
    def __init__(self,num): # 생성자
        print('Student 생성자:',num)
        self.num = num
        
    def info(self):
        print('self.name',self.name,self.num)
        
# Student s1 = new Student(10,20,30)        
s1 = Student(10)        
s2 = Student(20)   

s1.info()
s2.info()
     
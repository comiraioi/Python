'''
Created on 2023. 7. 17.

@author: user
'''
class Person :
    def __init__(self,name,age=90):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Person %s %d' % (self.name,self.age)

class Employee(Person):
    def __init__(self, name, age, position, salary):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        self.position = position
        self.salary = salary
    
    def __str__(self):
        # return '사원명: %s / 나이: %d / 직급: %s / 급여: %d' % (self.name,self.age,self.position,self.salary)
        return '사원명, 나이 : %s  / Employee 직급: %s / 급여: %d' % (super().__str__(),self.position,self.salary)     
p1 = Person('홍길동',30)
p2 = Person('아이유')

print(p1.name) # 홍길동
print(p1.age) # 30
print('p1:',p1.__str__())

print(p2.name) # 아이유
print(p2.age) # 90
print('p2:',p2)
print('---------------------------')


e1 = Employee('태연',40,'대리',200)
e2 = Employee('효연',50,'과장',300)
print(e1.name)
print(e1.age)
print(e1.position)
print(e1.salary)
print('e1:',e1)
print('e2:',e2)









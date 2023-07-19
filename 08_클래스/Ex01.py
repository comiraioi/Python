'''
Created on 2023. 7. 17.

@author: user
'''

def abc(x):
    print('abc()')
    
class Person :
    lastname = '김'
    
    def setname(self,name):
        print('self:',self) 
        self.fullname = self.lastname + name
        return self.fullname
        
# Person p1 = new Person()
p1 = Person()         
p2 = Person()  
print('p1:',p1)       
print('p2:',p2)    

print(p1.lastname)
print(p2.lastname)
print(Person.lastname)
fn1 = p1.setname('연아')
fn2 = p2.setname('보검')

print('fn1:',fn1)
print('fn2:',fn2)
# print(Person.fullname)


L = [p1,p2]
print(L[0])
print(L[1])
for i in L :
    print(i.fullname)
    













   
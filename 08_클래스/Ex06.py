'''
Created on 2023. 7. 17.

@author: user
'''
class Parent:
    def __init__(self):
        print('Parent 생성자')
    def show(self):
        print('Parent show함수')

class Child1:
    def __init__(self):
        print('Child 생성자')
        Parent.__init__(self)
        
    def show(self):
        print('Child show함수')      
        Parent.show(self)

class Child2(Parent): 
    def __init__(self):
        print('Child2 생성자')
        # Parent.__init__(self)
        # super().__init__()
        
    def show(self):
        print('Child2 show함수')
        # Parent.show(self)
        super().show()
        
        
p = Parent()
c1 = Child1()
p.show()
c1.show()
print('----------------')

c2 = Child2()
c2.show()





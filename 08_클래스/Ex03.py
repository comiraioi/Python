'''
Created on 2023. 7. 17.

@author: user
'''
class Bank :
    rate = 0.3
    
    def __init__(self, money):
        self.money = money
        
    def save(self):
        self.money = self.money*(1+self.rate) 
    
    def show(self):
        print('금액 : ' + str(int(self.money)))

b1 = Bank(10000)
b2 = Bank(20000)

b1.save()
b2.save()

b1.show()
b2.show()





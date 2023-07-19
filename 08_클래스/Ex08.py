'''
Created on 2023. 7. 17.

@author: user
'''
class Tiger:
    def jump(self):
        print('호랑이 jump')
    
    def cry(self):
        print('호랑이 어흥~')

class Lion:
    def bite(self):
        print('사자 bite')
    def cry(self):
        print('사자 으르렁~')

class Liger(Lion,Tiger):
    def play(self):
        print('라이거와 놀기')
        
l = Liger()
l.play()
l.jump()
l.cry()
l.bite()
        
        
        
        
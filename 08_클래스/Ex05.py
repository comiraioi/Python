'''
Created on 2023. 7. 17.

@author: user
'''

import Ex04_Service
s1 = Ex04_Service.Service('철수')
s1.show()


import Ex04_Service as ex04
s1 = ex04.Service('철수')
s1.show()

from Ex04_Service import Service
s1 = Service('김철수')
s1.show()
        
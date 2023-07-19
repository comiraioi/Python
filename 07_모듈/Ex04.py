'''
Created on 2023. 7. 14.

@author: Comi
'''

import Ex01
Ex01.abc()

print('------------')

import myPkg.Ex01
print(myPkg.Ex01.add(30,17))
print(myPkg.Ex01.sub(30,17))
print('------------')

import myPkg.Ex01 as pkg
print(pkg.add(30,17))
print(pkg.sub(30,17))
print('------------')

from myPkg.Ex01 import add, sub
print(add(30,17))
print(sub(30,17))

print('------------')

from myPkg.Ex01 import *
print(add(30,17))
print(sub(30,17))



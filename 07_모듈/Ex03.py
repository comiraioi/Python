'''
Created on 2023. 7. 14.

@author: Comi
'''

#import를 통해 다른 파일(모듈)의 함수 호출 가능
'''
형식
- import 모듈명
- import 모듈명 as 모듈별칭
- - from 모듈명 import 함수1 as 함수별칭
- from 모듈명 import 함수1,함수2,...
- from 모듈명 import *
'''

#방법1
import Ex01
Ex01.abc()
Ex01.xyz()
print('--------')

#방법2: 별칭 지정 가능
import Ex01 as e1    
e1.abc()
e1.xyz()
print('--------')

#방법3
from Ex01 import abc,xyz
abc()
xyz()
print('--------')

#방법4
from Ex01 import *
abc()
xyz()

print('=====================')

import Ex02     #파일 전체를 가져옴
#Ex02.display()
print('-----------')

import Ex02 as e2
e2.display()
print('-----------')

from Ex02 import display 
display()
print('-----------')

from Ex02 import *
display()




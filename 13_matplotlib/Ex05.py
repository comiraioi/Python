'''
Created on 2023. 7. 24.

@author: Comi
'''
import pandas as pd

from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt
font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family = font_name)


#파이 그래프
slices  = [1,2,3,4] #(1+2+3+4)분의 n 크기
hobby = ['영화감상','운동','게임','독서']
cols = ['c','m','r','b']

plt.pie(slices,labels=hobby,colors=cols,shadow=True,
        startangle=55,          #1번째 데이터 위치 설정
        explode=(0,0.1,0,0),    #2번째 데이터(운동)만 0.1만큼 분리
        autopct='%1.2f%%')      #퍼센트 표시
plt.legend(loc=10)              #파이별 데이터명 표시 위치 (10: 정가운데)

filename = 'hobby.png'
plt.savefig(filename)

plt.show()






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



x_name=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

#1~12월 평균 강수량 정보
y1_value = (21.6, 23.6, 45.8, 77.0, 102.2, 133.3, 327.9, 348.0, 137.6, 49.3, 53.0, 24.9)
#1~12월 평균 기온 정보
y2_value = (1.6, 4.1, 10.2, 17.6, 22.8, 26.9, 28.8, 29.5, 25.6, 19.7, 11.5, 4.2)

plt.xlabel('month(월)')         
plt.title('Weather Chart')

#막대그래프
plt.ylabel('평균 강수량(mm)')
bar_width=0.5
plt.bar(x_name,y1_value,bar_width,alpha=0.5,color='g')

plt.twinx() #x축(month)을 공유하고 y축은 별도로 지정

#꺾은선그래프
plt.ylabel('평균 기온($^oC$)')
plt.plot(x_name,y2_value,'r.-') #'r.-': color='red',marker='.',linestyle='solid'

#경계값 설정
plt.rcParams['axes.unicode_minus'] = False  #마이너스 기호 표시
plt.ylim(-10,30)

plt.show()






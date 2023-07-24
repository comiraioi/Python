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


'''
    국어  영어  수학
웬디  40  50  50
슬기  70  50  20
조이  20  20  20
'''
data = [[40,50,50],[70,50,20],[20,20,20]]
col = ['국어','영어','수학']
idx = ['웬디','슬기','조이']
df = pd.DataFrame(data,idx,col)
print(df)
print()

'''
    웬디  슬기  조이
국어  40  70  20
영어  50  50  20
수학  50  20  20
'''
#칼럼과 인덱스 전치
#df = df.T
df = df.transpose()
print(df)


#기본: 꺾은선그래프
#df.plot()
#plt.show()

#막대그래프
#df.plot(kind='bar')
#df.plot.bar()
df.plot.barh(stacked=True)  #수평 막대그래프 / stacked=True: 누적 합산
plt.xticks(rotation=0)  #축 제목 회전

#그래프 저장
filename = 'score.png'
plt.savefig(filename)

plt.show()






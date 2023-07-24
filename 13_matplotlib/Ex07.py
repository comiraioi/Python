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


filename = 'capital_area.csv'
mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드', \
            'TCS하이패스구분코드', '1종교통량', '2종교통량', \
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량', 'Noname']
df = pd.read_table(filename,sep="|",names=mycolumn)

#영업소 코드별 1~6종교통량 평균 정보 막대 그래프로 표현
mygroup = df.groupby('영업소코드')
data = mygroup[['1종교통량','2종교통량','3종교통량','4종교통량','5종교통량','6종교통량']].mean()
print(data)
 
data.plot.bar()
plt.title('영업소 코드별 n종 교통량 평균')
plt.ylabel('교통량')
plt.xticks(rotation=0)
plt.show()


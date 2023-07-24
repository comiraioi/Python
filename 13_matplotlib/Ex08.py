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

#집계일자별 1~7일 1~3종 교통량 평균 
mygroup = df.groupby('집계일자')
data = df[df['집계일자']<20170208].groupby('집계일자')[['1종교통량','2종교통량','3종교통량']].mean()
#data = mygroup[['1종교통량','2종교통량','3종교통량']].mean().head(7)
#data = mygroup[['1종교통량','2종교통량','3종교통량']].mean()[:7]
#data = data.reindex(index=[20170201,20170202,20170203,20170204,20170205,20170206,20170207])
print(data)
 
data.plot.bar()
plt.title('집계일자별 1~3종 교통량 평균')
plt.ylabel('교통량')
plt.xticks(rotation=0)
plt.legend(loc=3)
plt.show()


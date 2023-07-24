'''
Created on 2023. 7. 20.

@author: user
'''
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt


font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family = font_name)


x1 = [1,2,3,4]
y1 = [3,7,6,4]

x2 = [1,2,3,4]
y2 = [4,6,8,5]

ymax = max(max(y1), max(y2)) + 1 # max(7,8) 8+1=9
ymin = min(min(y1), min(y2)) - 1 # min(3,4) 3-1=2
plt.ylim(ymin,ymax) # 2~9

plt.plot(x1,y1,color='r',label="first line")
plt.plot(x2,y2,color='green',linestyle="dotted",marker='D',label="second line")

plt.xlabel('x축')
plt.ylabel('y축',rotation=0)
plt.title('Ex02 예제')

plt.annotate('annotate',xy=(1.5,5),xytext=(2,4),arrowprops={'color':'blue'})
plt.legend()

filename = 'brokenLine.png'
plt.savefig(filename)
plt.show()






















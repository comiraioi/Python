'''
Created on 2023. 7. 24.

@author: Comi
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

plt.figure(figsize=(5,6))   #그래프 사이즈

plt.subplot(2,1,1)  #2행 1열 / 1번 자리 (좌상부터 시계방향)
plt.plot(x1,y1,'yo--')  #선 색: y(yellow), ㅇ: 큰 점, --:점선
plt.xlabel('x1축')
plt.ylabel('y1축')

plt.subplot(2,1,2)
plt.plot(x2,y2, 'r.--') #선 색: r(red), .: 작은 점, --:점선
plt.xlabel('x2축')
plt.ylabel('y2축')

plt.show()












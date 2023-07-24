'''
Created on 2023. 7. 20.

@author: user
'''
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

fp = open('example.html')

soup = BeautifulSoup(fp,'html.parser')
print('1:',soup.title)
print('2:',soup.title.name)
print('3:',soup.title.string)
print('4:',soup.title.parent.name)
print('5:',soup.p)
print('6:',soup.div)
print('7:',soup.find_all('div'))
print('8:',soup.find_all('p'))
print('9:',soup.find_all('div','ex_class'))
print('10:',soup.find_all('div',id='ex_id'))
print('11:',soup.find_all(id='ex_id'))
print('11:',soup.find_all('a'))

fp.close()
print()

with open('example.html') as fp :

    soup = BeautifulSoup(fp,'html.parser')
    print('1:',soup.title)
    print('2:',soup.title.name)
    print('3:',soup.title.string)
    print('4:',soup.title.parent.name)
    print('5:',soup.p)
    print('6:',soup.div)
    print('7:',soup.find_all('div'))
    print('8:',soup.find_all('p'))
    print('9:',soup.find_all('div','ex_class'))
    print('10:',soup.find_all('div',id='ex_id'))
    print('11:',soup.find_all(id='ex_id'))
    print('11:',soup.find_all('a'))


print('---------------------------')

# https://movie.daum.net/ranking/reservation
soup = BeautifulSoup(urllib.request.urlopen('https://movie.daum.net/ranking/reservation').read(), 'html.parser')
result = soup.find_all('div','thumb_cont')
# print('result:\n',result)
rankList = []
movieTitle = []
scoreList = []
reserveList = []

for n in result :
    find_a = n.find('a')
    # print('find_a:',find_a) # <a class="link_txt" data-tiara-layer="moviename" href="/moviedb/main?movieId=139236">미션 임파서블: 데드 레코닝 PART ONE</a>
    # print(find_a.text)
    movieTitle.append(find_a.text)
    scoreList.append(n.find('span','txt_grade').text)
    reserveList.append(n.find('span','txt_num').text)
    
result2 = soup.find_all('span','rank_num')
print('result2:\n',result2)

rankList = []

for n in result2 : 
    rankList.append(n.text)

print('rankList : \n',rankList)    
print('movieTitle : \n',movieTitle)    
print('scoreList : \n',scoreList)    
print('reserveList : \n',reserveList)    

print('---------------')
for i in range(len(rankList)) : # 0~19
    print(rankList[i] +":" + movieTitle[i]+"/"+scoreList[i]+"/"+reserveList[i])

# 평점/예매율
# 3:밀수/7.3/18.2%
# 4:엘리멘탈
# 5:바비



print('\n\n\n\n\n\n')

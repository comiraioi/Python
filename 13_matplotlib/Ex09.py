'''
Created on 2023. 7. 24.

@author: Comi
'''

'''
folium: 위치 정보를 시각화하기 위한 라이브러리
'''
import folium  #cmd: conda install folium

#Marker:핑 찍기
m = folium.Map(location=[37.552270,126.980079],zoom_start=12) #위도,경도 / 확대
#팝업 아이콘
folium.Marker(location=[37.552270,126.980079],
              popup='용산도서관',icon=folium.Icon(icon='cloud')).add_to(m)
              
m.save('C:/Users/Comi/Python/map/map1.html')    #폴더는 직접 생성해야함
print('용산도서관 지도 생성됨')


#CircleMarker: 원으로 영역 표시 / 핑 찍기 불가능
folium.CircleMarker(location=[37.556738,126.919608], popup='쌍용강북교육센터',
                    radius=30,color='red',fill_color='#39ac21').add_to(m)
m.save('C:/Users/Comi/Python/map/map2.html')
print('쌍용강북교육센터 지도 생성됨')



'''
Created on 2023. 7. 14.

@author: Comi
'''


'''
번호 입력 (1:출력, 2:입력, 3:검색, 4:삭제, 5:수정, 6:종료) => (7 입력시 잘못입력하셨습니다)
입력
이름: kim
점수: 88

출력
이름    점수
kim    88

검색
찾는 이름 없음
'''

flag = False
student = {}
while True:
    print('1:출력 | 2:입력 | 3:검색 | 4:삭제 | 5:수정 | 6:종료')
    case = int(input('번호 입력 => '))
    if case == 1:
        print('=== 출력 ===')
        if len(student) == 0 :
            print('데이터가 없습니다.')
        else :
            print('이름\t점수')
            for i in student:
                print(i,'\t',student[i])
    elif case == 2:
        print('=== 입력 ===')
        name = input('이름: ')
        score = input('점수: ')
        student[name] = score
    elif case == 3:
        print('=== 검색 ===')
        name = input('검색할 이름: ')
        for key in student:
            if key.lower() == name.lower():
                print(name,'의 점수는',student.get(key),'입니다.')
                break
        else :
            print('찾는 이름 없음')
    elif case == 4:
        print('=== 삭제 ===')
        name = input('삭제할 이름: ')
        for key in student:
            if key.lower() == name.lower():
                del student[key]
                print('삭제가 완료되었습니다.')
                flag = True
                break
        if flag == False :
            print('해당 이름 없음')
    elif case == 5:
        print('=== 수정 ===')
        name = input('수정할 이름: ')
        for key in student:
            if key.lower() == name.lower():
                score = input('점수: ')
                student[key] = score
                print('수정이 완료되었습니다.')
                break
        else :
            print('해당 이름 없음')
    elif case == 6:
        print('프로그램을 종료합니다.')
        break
    else:
        print('번호를 잘못 입력하셨습니다.')
    

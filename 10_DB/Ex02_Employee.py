'''
Created on 2023. 7. 18.

@author: Comi
'''

import cx_Oracle
from _sqlite3 import DatabaseError
con = cx_Oracle.connect('jspid/jsppw@localhost:1521/orcl')

# employee 테이블생성(num,id,part,position,salary)
# emplseq 시퀀스 생성
#
# id입력:kim
# part입력:영업부
# position입력:대리
# salary입력:300 문자 입력하면 숫자로 입력하세요 계속 반복(예외처리)
# 계속?y ,n:반복 빠져나가기
#
# insert
# select 

#커서 공간 생성
cur = con.cursor()

#기존 시퀀스 삭제
try:
    dropseq = 'drop sequence emplseq'
    cur.execute(dropseq)
except cx_Oracle.DatabaseError:
    pass

#시퀀스 생성
seq = 'create sequence emplseq'
cur.execute(seq)

#기존 테이블 삭제
try:
    drop = "drop table employee"
    cur.execute(drop)
except cx_Oracle.DatabaseError:
    pass

#테이블 생성
create = ''' create table employee(
            num number primary key,
            id varchar2(15),
            part varchar2(15),
            position varchar2(15),
            salary number
            )
        '''
cur.execute(create)

#insert
while True:
    print('----------------------------------')
    id = input('id 입력: ')
    part = input('part 입력: ')
    position = input('position 입력: ')
    while True:
        try:
            salary = int(input('salary 입력: '))
        except ValueError:
            print('salary는 숫자로 입력하세요')
        else:
            break
    #insert = "insert into employee(num, id, part, position, salary) values (emplseq.nextval,'%s','%s','%s',%d)" %(id,part,position,salary) 
    #cur.execute(insert)
    insert = "insert into employee(num, id, part, position, salary) values (emplseq.nextval,:1,:2,:3,:4)"
    cur.execute(insert,(id,part,position,salary))
    con.commit()
    
    retry = input('계속:y / 종료:n > ')
    if(retry == 'n'):
        cur.execute('select * from employee')
        for row in cur :
            print(row)
        break
    
print('========================================')

update_id = input('수정할 id 입력: ')
update_part = input('수정할 part 입력: ')

#cur.execute("update employee set part='%s' where id='%s'" % (update_part,update_id))
update = "update employee set part= :1 where id =:2"
cur.execute(update,(update_part,update_id))
con.commit()

cur.execute('select * from employee')
for row in cur :
    print(row)
    
print('========================================')

delete_id = input('삭제할 id 입력: ')
cur.execute("delete employee where id='%s'" % (delete_id))
con.commit()

cur.execute('select * from employee')
for row in cur :
    print(row)


cur.close()
con.close()





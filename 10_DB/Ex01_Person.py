'''
Created on 2023. 7. 17.

@author: user
'''
import cx_Oracle    #cmd: conda install cx_Oracle
con = cx_Oracle.connect('jspid/jsppw@localhost:1521/orcl')

cur = con.cursor()

drop = 'drop table person'
cur.execute(drop)

dropseq = 'drop sequence perseq'
cur.execute(dropseq)

seq = 'create sequence perseq'
cur.execute(seq)

create = ''' create table person(
    num number primary key,
    id varchar2(10),
    name varchar2(10),
    addr varchar2(10)
    )
'''
cur.execute(create)

insert = "insert into person values(perseq.nextval,'hong','길동','서울')"
cur.execute(insert)

insert = "insert into person values(perseq.nextval,'kim','연아','부산')"
cur.execute(insert)

insert = "insert into person values(perseq.nextval,'park','지성','제주')"
cur.execute(insert)

con.commit()


cur.execute('select * from person')
for row in cur :
    print(row)

print('------------------------')

update = "update person set name='웬디' where id='kim'"
cur.execute(update)
con.commit()

cur.execute('select * from person')
for row in cur :
    print(row)

print('------------------------')

delete = "delete from person where id='hong'"
cur.execute(delete)
con.commit()

cur.execute('select * from person')
for row in cur :
    print(row)
print()






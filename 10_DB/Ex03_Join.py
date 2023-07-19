'''
Created on 2023. 7. 18.

@author: Comi
'''

import cx_Oracle
from _sqlite3 import DatabaseError
con = cx_Oracle.connect('jspid/jsppw@localhost:1521/orcl')
cur = con.cursor()

print('=== person ===')
cur.execute('select * from person')
for row in cur :
    print(row)
    
print()
print('=== employee ===')
cur.execute('select * from employee')
for row in cur :
    print(row)
    
print()
join = '''select p.id, p.name, e.part, e.salary
         from person p inner join employee e
         on p.id = e.id'''
         
print('=== join ===')
cur.execute(join)
for row in cur :
    print(row)




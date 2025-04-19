import sqlite3

conn=sqlite3.connect('cashflow.db')
c=conn.cursor()

# c.execute('''CREATE TABLE main(
#     user VARCHAR(100) PRIMARY KEY,
#     password VARCHAR(100),
#     total INTEGER,
#     food INTEGER,
#     fuel INTEGER,
#     outing INTEGER,
#     savings INTEGER,
#     misc INTEGER,
#     mandatory INTEGER,
#     spending INTEGER)''')

# c.execute('''drop TABLE main''')

c.execute(''' INSERT INTO main(user,password,food,fuel,outing,savings,misc,mandatory,spending)
            VALUES('Garv','Garv@123',0,0,0,0,0,0,0)
          ''')

conn.commit()
conn.close()

import sqlite3
conn = sqlite3.connect('pet.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE pet(
name VARCHAR(20),
owner VARCHAR(20),
species VARCHAR(20),
sex CHAR(1),
birth DATE,
death DATE
)
''')

query = 'INSERT INTO pet VALUES (?,?,?,?,?,?)'

for line in open('pet'):
    fields = line.split(',')
    vals = fields
    curs.execute(query, vals)

conn.commit()
conn.close()
#hit

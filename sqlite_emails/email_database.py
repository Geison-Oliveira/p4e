import sqlite3

conn = sqlite3.connect('email_db.sqlite')
curs = conn.cursor()

curs.execute('DROP TABLE IF EXISTS Counts')
curs.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

file_name = input('Enter the file name: ')
if len(file_name) < 1:
    file_name = 'mbox.txt'
    hnd_file = open(file_name)

for fll_line in hnd_file:
    if not fll_line.startswith('From:'):
        continue
    words = fll_line.split()
    email = words[1]
    domain = email.split('@')
    org = domain[1]
    curs.execute('''SELECT count 
    FROM Counts WHERE org = ?''',(org,))
    row = curs.fetchone()
    if row is None:
        curs.execute('''INSERT INTO Counts(org, count)
        VALUES(?, 1)''', (org,))
    else:
        curs.execute('''UPDATE Counts 
        SET count = count + 1 WHERE org = ?''', (org,))
conn.commit()

sqlstr = '''SELECT org, count 
FROM Counts ORDER BY count DESC'''
for row in curs.execute(sqlstr):
    print(str(row[0]), row[1])
curs.close()
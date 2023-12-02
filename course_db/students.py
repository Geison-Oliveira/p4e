import sqlite3
import json

connection = sqlite3.connect('course.sqlite')
cursor1 = connection.cursor()

cursor1.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
);
CREATE TABLE Course(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE
);
CREATE TABLE Member(
user_id INTEGER,
course_id INTEGER,
role INTEGER,
PRIMARY KEY(user_id, course_id)
)
''')

file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'roster_data.json'
file_handle = open(file_name)
json_file = file_handle.read()
string_json = json.loads(json_file)

#["Lisa", "si110", 1] json structure

for data in string_json:
    name = data[0]
    course = data[1]
    role = data[2]
    print(name, course, role)
    cursor1.execute('''
INSERT OR IGNORE INTO User(name)
VALUES (?)''', (name, ))
    cursor1.execute('''
SELECT id FROM User WHERE name = ? ''', (name, ))
    user_id = cursor1.fetchone()[0]
    cursor1.execute('''
INSERT OR IGNORE INTO Course(title)
VALUES(?)''', (course, ))
    cursor1.execute('''
SELECT id FROM Course WHERE title = ?''', (course, ))
    course_id = cursor1.fetchone()[0]
    cursor1.execute('''
INSERT OR REPLACE INTO Member(user_id, course_id, role)
VALUES(?, ?, ?)''', (user_id, course_id, role))
connection.commit()
connection.close()
#! /usr/bin/env python

import csv
import mysql.connector
from user import user

names = []
users = []
def get_names():
    with open('names.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            for name in row:
                names.append(name)

print("Starting the car...")

get_names()
for name in names:
    print(f'{name} detected')

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="car"
)

mycursor = mydb.cursor()
for name in names:
    mycursor.execute(f'select * from users where name = \"{name}\"')

    tup = ()
    for x in mycursor:
        tup = x

    mycursor.execute(f'select * from music_history where user_name = \"{name}\"')

    music_history = []

    for x in mycursor:
        hist = {'name' : x[1], 'year' : x[2]}
        music_history.append(hist)
    
    person = user(*tup, music_history)
    users.append(person)

for person in users:
    person.print_user_settings()

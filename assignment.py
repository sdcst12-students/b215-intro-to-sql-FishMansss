#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""
##setup
import sqlite3
file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()
cursor.execute("DROP TABLE vet;")
cursor.execute("CREATE TABLE vet(petName tinytext, petSpecies tinytext, petBreed tinytext, ownerName tinytext, ownerPhone int, email tinytext, ownerBalance tinytext, dateOfVisit tinytext);")

loop = True
while loop==True:
    print('1. Add Record')
    print('2. Retreive Record')
    print('3. Exit')
    x=int(input())
    if x==1:
        print('pet name:')
        pn=str(input())
        print('species:')
        sp=str(input())
        print('pet breed:')
        pb=str(input())
        print('owner name:')
        on=str(input())
        print('owner phone')
        op=int(input())
        print('email:')
        e=str(input())
        print('owner balance:')
        ob=float(input())
        print('date of first visit')
        dov=str(input())
        
        cursor.execute(f"INSERT INTO vet(petName, petSpecies, petBreed, ownerName, ownerPhone, email, ownerBalance, dateOfVisit) VALUES('{pn}','{sp}','{pb}','{on}',{op},'{e}',{ob},'{dov}');")
        
            
    if x==2:
        print('Search by Name')
        name=input()
        cursor.execute(f"select * from vet where PetName is '{name}' ;")
        r = cursor.fetchall()
        print(r)
    if x==3:
        exit()
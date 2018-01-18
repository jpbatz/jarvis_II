#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 23:06:25 2018

@author: jph
"""

#import sqlite3

fin = open('villains.csv')
fin.readline()
fin.readline()

#conn = sqlite3.connect('database01.db')
#
#SQL = '''CREATE TABLE villains  (fname text,
#                                 lname text,
#                                 alias text,
#                                 age integer,
#                                 weapon text)'''
#
#try:
#    conn.execute(SQL)
#except:
#    pass
#
#curr = conn.cursor()

fin.readlines()

for line in fin:
    fname, lname, alias, age, weapon = line.strip().split(',')
    print(lname, fname, alias, age, weapon)

#    insert = '''INSERT INTO villains VALUES (?, ?, ?, ?, ?)'''
#    curr.execute(insert, (fname, lname, alias, age, weapon))

fin.close()

#conn.commit()
#conn.close()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:12:23 2018

@author: jph
"""

import sqlite3

conn = sqlite3.connect('database02.db')


SQL = '''CREATE TABLE villains  (fname text,
                              lname text,
                              alias text,
                              age integer,
                              weapon text)'''

try:
    conn.execute(SQL)
except:
    pass


curr = conn.cursor()

#curr.execute('INSERT INTO villains VALUES (?, ?, ?, ?, ?)', 
#             ('harleen', 'quinzel', 'harley quinn', 42, 'bat'))

insert = '''INSERT INTO villains VALUES (?, ?, ?, ?, ?)'''
curr.execute(insert, ('harleen', 'quinzel', 'harley quinn', 42, 'bat'))


conn.commit()
conn.close()
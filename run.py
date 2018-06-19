#! /usr/bin/env python3
from pack.dict import sqliteDB
# from pack.dict import smartDict
import myparser
# import os.path
from pack.consui import consUI
import mhp

dbname = '.\words.db'
tempName = 'temp.tmp'
sourceName = 'raw_word.txt'
htmlName = 'raw.html'

# sqliteDB.CreateDB(dbname)
# sqliteDB.TestingDB(dbname)

# db = sqliteDB.SQLiteDB(dbname)
# dbc = db.cursor

# raw = myparser.ParseRaw(sourceName, myparser.LineP, 20)
raw = mhp.GetText(htmlName)
myparser.WriteToFile(raw, tempName)

# strconv = (str(i) for i in raw)
# myparser.WriteToFile(strconv, tempName)

# myparser.WriteToDb(raw, db)

# sqliteDB.Select(dbc, 'words')
# db.ExtendLernPull()
# sqliteDB.Select(dbc, 'lern')
# db.Close()

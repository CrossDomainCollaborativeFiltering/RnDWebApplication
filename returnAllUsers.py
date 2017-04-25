#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
class UserDataSet:
    
    def __init__(self):
        self.dummy=-1

    def users(self):
        ALL_USERS_FILENAME="datasets/userids.csv"
        import csv
        # csvFile=open(ALL_USERS_FILENAME, newline="")
        csvFile=codecs.open(ALL_USERS_FILENAME, 'r', encoding='utf-8', errors='ignore')
        reader=csv.reader(csvFile)
        return next(reader)
#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
class MovieDataSet:
    def __init__(self):
        self.dummy=-1

    def movies(self):
        ALL_MOVIES_FILENAME="datasets/allMovies.csv"
        import csv
        # csvFile=open(ALL_MOVIES_FILENAME, newline="")
        csvFile=codecs.open(ALL_MOVIES_FILENAME, 'r', encoding='utf-8', errors='ignore')
        reader=csv.reader(csvFile)
        return next(reader)
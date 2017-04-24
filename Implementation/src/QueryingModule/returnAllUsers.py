def users():
    ALL_USERS_FILENAME="userids.csv"
    import csv
    csvFile=open(ALL_USERS_FILENAME, newline="")
    reader=csv.reader(csvFile)
    return next(reader)
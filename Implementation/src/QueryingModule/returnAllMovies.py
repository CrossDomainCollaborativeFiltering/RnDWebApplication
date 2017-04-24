def movies():
    ALL_MOVIES_FILENAME="allMovies.csv"
    import csv
    csvFile=open(ALL_MOVIES_FILENAME, newline="")
    reader=csv.reader(csvFile)
    return next(reader)
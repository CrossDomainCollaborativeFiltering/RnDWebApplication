MOVIE_FILENAME="../MovieLens/ResultMovieDataSetClone.csv"
ALL_MOVIES_FILENAME="allMovies.csv"
import csv
# this program will store all the movieids in the dataset in one file.
csvfile=open(MOVIE_FILENAME, newline="")
reader=csv.reader(csvfile)
next(reader)
movies=[]
movieFile=open(ALL_MOVIES_FILENAME, 'w', newline="")
for row in reader:
    val=int(row[0])
    movies.append(val)
print ('all movies read')
writer=csv.writer(movieFile)
writer.writerow(movies)    
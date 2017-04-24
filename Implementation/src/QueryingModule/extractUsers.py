"""
This program will be used to extract all users from the csv file and store them in another file

"""
USER_MOVIE_FILENAME="../../../dataSets/movieLens/user_ratedmovies.csv"
ALL_USERS_FILENAME="userids.csv"
import csv
csvFile=open(USER_MOVIE_FILENAME, newline="")
reader=csv.reader(csvFile)
next(reader)
foundUsers=[]
for row in reader:
    val=int(row[0])
    if val not in foundUsers:
        foundUsers.append(val)

print ("alll users taken")

csvFile=open(ALL_USERS_FILENAME, 'w', newline="")
writer=csv.writer(csvFile)
writer.writerow(foundUsers)


    

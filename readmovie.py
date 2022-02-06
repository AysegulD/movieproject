from dbconnect import *

def readmovie():
    cursor.execute("SELECT * FROM tblFilms")
    row =cursor.fetchall()
    for record in row:
        print(record)
# readmovie()
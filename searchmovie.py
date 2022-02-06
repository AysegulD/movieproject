
from dbconnect import *
import time

def searchMovie():
    fieldName = input("Which field you want to search(title,yearReleased,rating,duration,genre)? ")
    searchValue = input("Enter the search value for the field: ")
    print("User Value",searchValue)
    searchValue = "'" + searchValue + "'"
    print("User amended input",searchValue)

    try:
        cursor.execute('SELECT * FROM tblFilms WHERE ' + fieldName + "=" + searchValue)
        conn.commit()
        print("Movie" + searchValue + "searched")
        row = cursor.fetchall()
        for record in row:
         print(record)

    except:
        print("Movie " + searchValue + " Not found")
    finally:
        conn.close()
# searchMovie()
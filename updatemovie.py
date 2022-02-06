from dbconnect import *
import time

def update():
    idOfMovie = input("Please enter the id of the movie you want to update: ")
    fieldName = input("Which field you want to update (title,yearReleased,rating,duration,genre)? :")
    newFieldName = input("Please enter a new value for the field: ")
    print("User Value", newFieldName)
    newFieldName = "'" + newFieldName + "'"
    print("User amended input", newFieldName)

    try:
        sql = """ UPDATE tblFilms SET """ + fieldName + "=" + newFieldName + """WHERE filmID = """ + idOfMovie
        cursor.execute(sql)
        conn.commit()
        print("Movie Record" + idOfMovie + "Updated")

        time.sleep(3)
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Movie " + idOfMovie +  " not updated") 
    finally:
        conn.close()
# update()
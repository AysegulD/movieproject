from dbconnect import *
import time

def deleteMovie():
    idField = input("Enter the id of the movie you want to delete: ")

    try:
        cursor.execute("DELETE FROM tblFilms WHERE filmID = " + idField)
        conn.commit()
        print("Movie " + idField + " Deleted")
        
        time.sleep(3)
        cursor.execute("SELECT *FROM tblFilms")
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Movie " + idField + " not deleted")
    finally:
        conn.close()

# deleteMovie()
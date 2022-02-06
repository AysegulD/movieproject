from dbconnect import *
import time


def addmovie():
    movie = []
    filmID = cursor.lastrowid
    title = input("Enter movie title: ")
    yearReleased = input("Enter the movie release year: ")
    rating = input("Enter the rating: ")
    duration = input("Enter the duration of the movie: ")
    genre = input("Enter the genre of the movie: ")

    movie.append(filmID)
    movie.append(title)
    movie.append(yearReleased)
    movie.append(rating)
    movie.append(duration)
    movie.append(genre)

    try:
        cursor.execute('INSERT INTO tblFilms VALUES(?,?,?,?,?,?)',movie)
        conn.commit()
        print("Movie added")

        time.sleep(3)
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Movie " + title + " not added")
    finally:
        conn.close()

# addmovie()
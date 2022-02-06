
from addmovie import *
from deletemovie import *
from readmovie import *
from updatemovie import *
from searchmovie import *

def movieMenu():
    options = 0

    while options not in ["1","2","3","4","5","6"]:
        print("\nMenu options\n1. Print all movies\n2. Add movie\n3. Update movie\n4. Search movie\n5. Delete movie\n6. Exit")
        options =input("\nEnter one of the options: ")
        if options not in ["1","2","3","4","5","6"]:
            print("Not in the list of options")
        return options

# movieMenu()

mainProgram =True

while mainProgram == True:
    mainmenu = movieMenu()
    if mainmenu == "1":
        readmovie()
    elif mainmenu == "2":
        addmovie()
    elif mainmenu == "3":
        update()
    elif mainmenu == "4":
        searchMovie()
    elif mainmenu == "5":
        deleteMovie()
    else:
        mainProgram = False
input("Press enter exit")
    


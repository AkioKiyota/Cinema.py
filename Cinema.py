import os
import glob

def getMovies():
    movies = glob.glob(r"/Cinema/Berk.txt")
    return movies

def getChairs(mov):
    with open(f"Cinema/{str(mov).strip()}.txt", "r") as db: ###   DEĞİŞTİRİLECEK   ###
        whole_mov = db.read()
        list = whole_mov.split("\n")
        return list
    
movies = getMovies()

def cinema():
    name = input("May i take your name please? \n") 

   
    for x in movies:
        print(f"{x}: {movies[x]}")

    selectedMov = input("Which movie wanna go?[Enter Exact Movie Name]\n")

    chairs = getChairs(selectedMov)

    for x in range(1,41):
        print(f"{x}: {chairs[x]}")
    
    chairNum = input("Which chair do you want? \n")
    if chairs[int(chairNum)] == "empty":
        chairs[int(chairNum)] = name
        os.remove(f"Cinema/{selectedMov}.txt")
        with open(f"Cinema/{selectedMov}.txt", "w+") as db:
            db.write("\n".join(chairs))
        ticket = f"|  Name: {name},\n|  Movie: {selectedMov},\n|  Chair Number: {chairNum}."
        print(ticket)
    elif not chairs[int(chairNum)] == "empty":
        print("That chair is full")
    

def secondTicket():
    another = input("Do you want any other tickets? [Y/N]? \n")
    if another == "Y" or another == "y":
        return print(cinema())
    elif another == "N" or another == "n":
        return print("Thank you for coming")
    else:
        return print(secondTicket())

print(cinema())
print(secondTicket())




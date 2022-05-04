import os

def add(mov):
    with open(f"{mov}.txt", "w") as db:
        db.write(mov + ":\n")
        for x in range(1,41):
            db.write("empty\n")
            
def remove(mov):
    os.remove(f"{mov}.txt")
            

choice = input("Add or remove movie. [Add/Remove]\n")

if choice == "Add" or choice == "add" :
    q = input("Enter the movie name:\n")
    exists = os.path.exists(f"{q.strip}.txt")
    if exists:
        print("This movie already exists!")
    elif  not exists:
        add(q.strip())
elif choice == "Remove" or choice == "remove" :
    w = input("Enter the movie name:\n")
    exists = os.path.exists(f"{w.strip()}.txt")
    if exists:
        remove(w.strip())
    elif not exists:
        print("There is no such a movie!")





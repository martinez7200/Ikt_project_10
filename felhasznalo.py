username = "Martin"
password = "Infó"
while True:
    nev = input("Add meg a felhasználó nevet! ")
    if nev == username:
        print(" A felhasználónév helyes! ")
        break
    else:
        print("A felhasználó helytelen! ")
while True:       
    jelszo = input("Add meg a jelszót! ")
    if jelszo == password:
        print("A jelszó helyes! ")
        break
    else:
        print("A jelszó helytelen! ")


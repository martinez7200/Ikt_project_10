username = "Martin"
password = "Laptop"
while True:
    nev = input("Add meg a felhasználónevet! ")
    jelszo = input("Add meg a jelszót! ")
    if nev == username:
        if password == jelszo:
            print("ok")
        break       

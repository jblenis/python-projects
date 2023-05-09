import string
import random

caracteres= list(string.ascii_letters + string.digits + "!@#$%^&*()~")

def generar_password():
    password_length = int(input("Ingresar el largo de tu contrasena:"))

    random.shuffle(caracteres)

    password = []

    for x in range(password_length):
        password.append(random.choice(caracteres))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Quieres generar una contrasena?(Si/No) ")

if option == "Si":
    generar_password()
elif option =="No":
    print("Programa finalizado. :)")
    quit()
else:
    print("Invalido,Porfavor escribe Si o No")

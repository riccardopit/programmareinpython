#Scrivi un programma che crei un file CSV per memorizzare in un dizionario i dati degli utenti registrati su un sito web.
#I dati richiesti per ogni utente sono: username, password, email e data di registrazione.
#Il programma deve permettere di salvare le informazioni nel file, leggere i dati e stamparli a schermo.

import csv

users = [
    {"username": "Michael", "password": "hisairness23", "e-mail": "michael.jordan@gmail.com", "registration date": "23/08/2023"},
    {"username": "Kobe", "password": "blackmamba24", "e-mail": "kobe.bryant@gmail.com", "registration date": "24/08/2023"},
    {"username": "Stephen", "password": "chefcurry30", "e-mail": "stephen.curry@gmail.com", "registration date":"30/08/2023"},
]

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["username", "password", "e-mail", "registration date"])
    for user in users:
        writer.writerow(user.values())

with open("users.csv", "r") as file:
    reader = csv.reader(file)
    for user in reader:
        print(user)
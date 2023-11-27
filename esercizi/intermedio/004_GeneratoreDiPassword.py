#Scrivi una funzione generatrice di password.

#La funzione deve generare una stringa alfanumerica di 8 caratteri qualora l'utente voglia una password semplice, e di 20 caratteri ASCII qualora desideri una password più complicata.

import random
import string

def psw_generator():
    psw = ""
    while True:
        psw_type = input("Chose a type of password. Easy or difficult? [e/d] ")
        if psw_type == "e":
            for i in range(8):
                psw += random.choice(string.ascii_letters + string.digits)
            break
        elif psw_type == "d":
            for i in range(20):
                psw += random.choice(string.ascii_letters + string.digits + string.punctuation)
            break
        else:
            print("No type selected.")
    return psw

print(psw_generator())
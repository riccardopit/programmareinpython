#Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente.

#Suggerimento: per risolvere questo esercizio potreste dover utilizzare una libreria! ;)

from platform import system, release

def my_sys():
    return system() + " " + release()

print(my_sys())
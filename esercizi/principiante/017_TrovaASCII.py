#Scrivi una funzione che, dato un carattere in ingresso, restituisca in output il codice ASCII associato al carattere passato.

#Anche in questo caso, usare una libreria potrebbe facilitare la risoluzione dell'esercizio!

def ascii_conv():
    val = input("Insert character: ")
    return ord(val)

print(ascii_conv())
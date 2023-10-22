#Scrivi una funzione che prenda una serie di input dall'utente utilizzando un ciclo while e li stampi con la funzione print senza andare a capo. Il ciclo while si deve interrompere quando l'utente preme INVIO senza scrivere nulla.

def printing():
    text = input("Insert text: ")
    while text != "":
        print(text, end=" ")
        text = input("Insert text: ")

printing()
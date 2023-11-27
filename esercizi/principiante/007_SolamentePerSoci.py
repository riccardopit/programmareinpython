#Scrivi un programma che a partire da un elemento e una lista di elementi dica in output se l'elemento passato sia presente o meno nella lista.

#Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo index.

letters = ["a", "b", "c"]

letter = input("Insert a letter: ")

try:
    index = letters.index(letter)
    print(f"Letter '{letter}' is present at index {index}.")
except:
    print(f"Letter '{letter}' is not present.")
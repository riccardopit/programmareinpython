#Scrivi un programma che a partire da un elemento e una lista di elementi dica in output se l'elemento passato sia presente o meno nella lista.

#Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo index.

letter_list = ["a", "b", "c"]

letter = input("Insert a letter: ")

try:
    index = letter_list.index(letter)
    print("Letter is present at index " + str(index) + ".")
except:
    print("Letter is not present.")
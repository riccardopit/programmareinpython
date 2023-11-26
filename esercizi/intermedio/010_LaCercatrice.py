#Scrivi una funzione "cercatrice" che scansioni un dato percorso di sistema alla ricerca di file di tipo pdf tramite il modulo os. La funzione dovrà avere le seguenti caratteristiche:

#Il percorso fornito dovrà essere anzitutto validato, in quanto deve portare a una cartella esistente
#La funzione dovrà fornire un elenco dei file pdf (con/relativo/percorso) man mano che questi vengono trovati
#Infine la funzione dovrà fornire in output il totale dei file .pdf che sono stati trovati durante la scansione.

import os

def pdf_search(path):
    exist = os.path.exists(path)
    count = 0
    if exist:
        for root, dirs, files in os.walk(path):
            for file in files:
                if not file.endswith(".pdf"):
                    continue
                print(os.path.join(root, file))
                count += 1
        print(f"{count} pdf files found.")
    else:
        print(f"Path not found.")

path = input("Insert path: ")
pdf_search(path)
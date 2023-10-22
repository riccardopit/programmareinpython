#Scrivi una funzione che permetta di inserire una canzone e salvarla in un file di testo. Il programma deve chiedere all'utente di inserire il titolo e il testo della canzone, e poi salvare quest'ultimo in un file intitolato titolo_canzone.txt.

#Suggerimento: dovrai utilizzare l'istruzione with.

def song():
    title = input("Insert song title: ")
    text = input("Insert song lyrics: ")
    with open(title + ".txt", 'w') as file:
        file.write(text)

song()
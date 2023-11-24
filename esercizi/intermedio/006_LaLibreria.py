#Scrivi una funzione vendi_libri(), che aiuti nella gestione della vendita di libri in una libreria:

#Controlla se il libro richiesto è presente sugli scaffali della libreria
#Qualora il libro sia presente, ne decrementa il numero di copie (eventualmente rimuovendo il titolo) e ci segnala che la vendita ha avuto successo
#Se il libro non è disponibile, viene messo in un elenco di libri da ordinare e ci viene comunicato che la vendita non ha avuto successo
#La funzione deve restituire valore booleano True o False in base all'esito della vendita.

def sell_books(book, books):
    new_books = []
    if book in books:
        books[book] -= 1
        if books[book] == 0:
            del books[book]
        print("Book sold!")
        return True
    else:
        print("Book not sold!")
        new_books.append(book)
        print("Books ordered:")
        print(new_books)
        return False

books = {"The Jordan Rules": 23, "The Mamba Mentality": 8, "Steve Jobs": 1, "Programming in python": 100}

book = input("Insert book name: ")

sell_books(book, books)

print("Books in library:")
print(books)
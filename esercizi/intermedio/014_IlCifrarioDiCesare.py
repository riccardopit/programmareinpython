#Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare ciascuna lettera di una certa quantità di posti nell'alfabeto.
#Per utilizzarlo, si sceglie una chiave che rappresenta il numero di posti di cui ogni lettera dell'alfabeto verrà spostata:
#ad esempio, se si sceglie una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
#Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero di posti corrispondente alla chiave.

#Scrivi una funzione che riceva come argomento una stringa e un numero e applichi il Cifrario di Cesare alla stringa spostandosi nell'alfabeto di tante posizioni quante dice il numero.

from string import ascii_lowercase as letters

def caesar_cipher(text, key):
    crypted_text = ""
    last_index = len(letters)-1 #25
    for character in text:
        if character.lower() in letters:
            new_letter_index = letters.index(character.lower()) + key
            if new_letter_index > last_index:
                new_letter_index = new_letter_index - last_index - 1
            if character.islower():
                crypted_text += letters[new_letter_index]
            else:
                crypted_text += letters[new_letter_index].upper()
        else:
            crypted_text += character
    return crypted_text

text = input("Insert text: ")
key = int(input("Insert key: "))
print(caesar_cipher(text, key))
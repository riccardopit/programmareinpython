#Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti nell'alfabeto.

#Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.

from string import ascii_uppercase as up
from string import ascii_lowercase as lw

def rot13(text):
    crypted_text = ""
    for letter in text:
        if letter in up:
            letters_list = up
        if letter in lw:
            letters_list = lw
        last_index = len(letters_list)-1
        new_letter_index = letters_list.index(letter) + 13
        if new_letter_index > last_index:
            new_letter_index = new_letter_index - last_index - 1
        crypted_text += letters_list[new_letter_index]
    return crypted_text

print(rot13("AbcDnOPq"))
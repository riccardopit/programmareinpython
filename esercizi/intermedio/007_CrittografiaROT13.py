#Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti nell'alfabeto.

#Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.

from string import ascii_lowercase as letters
import codecs

def rot13(text):
    crypted_text = ""
    last_index = len(letters)-1 #25
    for character in text:
        if character.lower() in letters:
            new_letter_index = letters.index(character.lower()) + 13
            if new_letter_index > last_index:
                new_letter_index = new_letter_index - last_index - 1
            if character.islower():
                crypted_text += letters[new_letter_index]
            else:
                crypted_text += letters[new_letter_index].upper()
        else:
            crypted_text += character
    return crypted_text

def rot13_pro(text):
    return codecs.encode(text, 'rot_13')

text = input("Insert text: ")
print(rot13(text))
print(rot13_pro(text))
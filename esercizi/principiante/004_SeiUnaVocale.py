#Scrivi un programma che chieda all'utente una stringa composta da un solo carattere e dica se si tratta di una vocale oppure no.

vowels = "aeiou"

letter = input("Insert a letter: ")

if letter in vowels:
    print("It's a vowel.")
else:
    print("It's not a vowel.")
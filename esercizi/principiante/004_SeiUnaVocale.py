#Scrivi un programma che chieda all'utente una stringa composta da un solo carattere e dica se si tratta di una vocale oppure no.

vowels = "aeiou"

letter = input("Insert a letter: ")

if letter in vowels:
    print(f"Letter '{letter}' is a vowel.")
else:
    print(f"Letter '{letter}' is not a vowel.")
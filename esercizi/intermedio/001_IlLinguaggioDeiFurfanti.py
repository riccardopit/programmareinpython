#In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto rövarspråket, che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".

#Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in rövarspråket. Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra, e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova parola da parte dell'utente.

def rovarspraket(word):
    new_word = ""
    vocals = "aeiou"
    specials = [" ", ",", ".", "?", "!", '"',"'"]
    for letter in word:
        new_word += letter
        if letter not in vocals and letter not in specials:
            new_word += "o" + letter
    return new_word

while True:
    word = input("Insert a word: ")
    print(rovarspraket(word))
    while True:
        answer = input("Do you want to translate another word? [y/n] ")
        if answer == "y" or answer == "n":
            break
        else:
            print("No answer selected.")
    if answer == "n":
        break
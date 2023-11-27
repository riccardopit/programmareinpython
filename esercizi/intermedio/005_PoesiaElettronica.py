#Scrivi una semplice funzione rimario, a cui viene passato un elenco di parole come parametro e che riceva una parola inserita dall'utente tramite la funzione input.

#La funzione rimario dovrà confrontare la parola inserita dall'utente con quelle presenti nell'elenco passato, alla ricerca di rime, intese come parole le cui ultime 3 lettere siano uguali alla parola inserita dall'utente.

#Le rime dovranno essere quindi mostrate in output utilizzando il metodo join.

words = ["Dormire", "Salutare", "Autostop", "Starnuto",
         "Camminare", "Nuotare", "Sciare", "Spray",
         "Macho", "Volare", "Campana", "Okay",
         "Baciare", "Capelli", "Saluti", "Superman"]

def rhyme(word_list):
    n = 3   #number of letters to detect rhymes
    rhyme_list = []
    my_word = input("Insert a word: ")
    for word in word_list:
        if word[-n:] == my_word[-n:]:
            rhyme_list.append(word)
    if not rhyme_list:
        return "No rhymes found."
    else:
        return ", ".join(rhyme_list)

print(rhyme(words))
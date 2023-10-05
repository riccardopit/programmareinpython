#Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

#Questo esercizio può essere risolto anche usando una list comprehension.

words = ["I", "love", "python", "programming", "language"]

def length_list(word_list):
    len_list = []
    for word in word_list:
        len_list.append(len(word))
    return len_list

def length_list_pro(word_list):
    return [len(word) for word in word_list]

print(length_list(words))
print(length_list_pro(words))
#Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.

#Per fare un esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}

text = "Supercalifragilisticexpialidocious"

def letter_dict(text):
    count_dict = {}
    for letter in text:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    return count_dict

print(letter_dict(text))
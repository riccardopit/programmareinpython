#Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro. In sostanza, seppur presente, provate a scrivere la nostra versione della funzione len!

letters = "abcdefghijklmnopqrstuvwxyz"

def length(str_list):
    count = 0
    for _ in str_list:
        count += 1
    return count

print(length(letters))
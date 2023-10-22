#Scrivi una funzione a cui passerai come parametro una stringa, e che manderà in print una versione inversa (al contrario) della stessa stringa. Ad esempio "abcd" diventerà "dcba".

#Suggerimento: per risolvere questo esercizio in modo compatto potresti usare lo slicing.

def reverser(text):
    reversed_text = text[::-1]
    return reversed_text

text = input("Insert text to be reversed: ")
print(reverser(text))
#Scrivi una funzione a cui passerai come parametro una stringa, e che manderà in print una versione inversa (al contrario) della stessa stringa. Ad esempio "abcd" diventerà "dcba".

#Suggerimento: per risolvere questo esercizio in modo compatto potresti usare lo slicing.

def reverser(text):
    index = len(text)-1
    reversed_text = ""
    while index >= 0:
        reversed_text += text[index]
        index -= 1
    return reversed_text

def reverser_pro(text):
    reversed_text = text[::-1]
    return reversed_text

text = input("Insert text to be reversed: ")
print(reverser(text))
print(reverser_pro(text))
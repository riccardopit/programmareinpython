#Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.

#Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.

num_list = [1, 30, 24, 3, 23]

tot = 0   #initialization
for i in num_list:
    tot += i

print(tot)
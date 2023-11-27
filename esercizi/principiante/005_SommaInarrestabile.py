#Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.

#Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.

nums = [1, 30, 24, 3, 23]

tot = 0   #initialization
for num in nums:
    tot += num

print(tot)
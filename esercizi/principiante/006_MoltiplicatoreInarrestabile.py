#Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.

num_list = [1, 0, 24, 3, 23]

tot = 1   #initialization
for i in num_list:
    tot *= i
    if i == 0:  #condition to avoid unnecessary multiplication
        break

print(tot)
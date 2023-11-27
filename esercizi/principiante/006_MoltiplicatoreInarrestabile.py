#Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.

nums = [1, 30, 24, 3, 23]

tot = 1   #initialization
for num in nums:
    tot *= num
    if num == 0:  #condition to avoid unnecessary multiplication
        break

print(tot)
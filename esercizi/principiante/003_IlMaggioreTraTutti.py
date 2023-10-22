#Scrivi un programma che chieda all'utente una lista di numeri e fornisca in output il maggiore tra tutti.

num_list = [1, 30, 24, 3, 23]

num_max = num_list[0]   #initialization
for i in num_list:
    if i > num_max:
        num_max = i

print(num_max)
#Scrivi un programma che chieda due numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando la funzione print.
#Per quanto Python disponga di una funzione max(), siete invitati ad utilizzare le istruzioni istruzioni if, elif ed else per la scrittura dell'algoritmo.

a = int(input("Insert first number: "))     #int casting in order to work with numbers > 9
b = int(input("Insert second number: "))    #int casting in order to work with numbers > 9

if a == b:
    print("Numbers are equal.")
elif a > b:
    print(a)
else:
    print(b)
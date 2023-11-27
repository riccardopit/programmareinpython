#Nella Successione di Fibonacci, ciascun numero è la somma dei due numeri che lo precedono, ad esempio:

#1, 1, 2, 3, 5, 8, 13 (...)

#Scrivi una funzione ricorsiva che restituisce in output i numeri della successione di Fibonacci, entro una soglia specifica impostata dall'utente.

def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n

n = int(input("How many numbers?: "))

for i in range(1, n+1):
    print(fibonacci(i))
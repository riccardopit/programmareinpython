#Scrivi una funzione ricorsiva che calcola il fattoriale di un numero dato.

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

print(factorial(3))
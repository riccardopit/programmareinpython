#Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori positivi, escluso sé stesso. Scrivi una funzione che verifichi se un numero è perfetto oppure no.


def perfect():
    num = int(input("Insert intiger number: "))
    sum = 0
    for i in range(1, num//2+1):
        if num % i == 0:
            sum += i
    if sum == num:
        return "The number is perfect."
    else:
        return "The number is not perfect."

print(perfect())
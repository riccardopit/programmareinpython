#Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.

a = int(input("Insert first number: "))     #int casting in order to work with numbers > 9
b = int(input("Insert second number: "))    #int casting in order to work with numbers > 9
c = int(input("Insert third number: "))     #int casting in order to work with numbers > 9

if a == b == c:
    print("Numbers are equal.")
elif a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
#Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:
#un cerchio
#un quadrato
#un rettangolo
#un triangolo
#Sentitevi liberi di estendere le potenzialità della funzione quanto meglio credete!

def area():
    print("Chose a shape which you want calculate the area:\na - Circle\nb - Square\nc - Rectangle\nd - Triangle")
    s = input("Insert your choice: ")
    if s == "a" or s == "A":
        r = float(input("Insert radius: "))
        a = r**2 * 3.14
        return "The area of the circle is " + str(a) + "."
    elif s == "b" or s == "B":
        l = float(input("Insert side: "))
        a = l**2
        return "The area of the square is " + str(a) + "."
    elif s == "c" or s == "C":
        b = float(input("Insert base: "))
        h = float(input("Insert height: "))
        a = b * h
        return "The area of the rectangle is " + str(a) + "."
    elif s == "d" or s == "D":
        b = float(input("Insert base: "))
        h = float(input("Insert height: "))
        a = b * h / 2
        return "The area of the triangle is " + str(a) + "."
    else:
        return "No shape found."

print(area())
#Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:
#un cerchio
#un quadrato
#un rettangolo
#un triangolo
#Sentitevi liberi di estendere le potenzialità della funzione quanto meglio credete!

def input_validated(text):
    while True:
        val = input(text)
        if val.isnumeric():
            val = float(val)
            return val
        print("Input not valid.")

def area():
    print(f"Chose a shape which you want calculate the area:\na - Circle\nb - Square\nc - Rectangle\nd - Triangle")
    s = input("Insert your choice: ")
    if s == "a" or s == "A":
        r = input_validated("Insert radius in mm: ")
        a = r**2 * 3.14
        return f"The area of the circle is {a} mm2."
    elif s == "b" or s == "B":
        l = input_validated("Insert side in mm: ")
        a = l**2
        return f"The area of the square is {a} mm2."
    elif s == "c" or s == "C":
        b = input_validated("Insert base in mm: ")
        h = input_validated("Insert height in mm: ")
        a = b * h
        return f"The area of the rectangle is {a} mm2."
    elif s == "d" or s == "D":
        b = input_validated("Insert base in mm: ")
        h = input_validated("Insert height in mm: ")
        a = b * h / 2
        return f"The area of the triangle is {a} mm2."
    else:
        return "No shape found."

print(area())
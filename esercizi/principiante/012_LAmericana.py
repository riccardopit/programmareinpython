#Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici. Come risolverai questo esercizio?

def length_conv(meters):
    miles = meters * 0.000621371
    yards = meters * 1.09361
    feet = meters * 3.28084
    inches = meters * 39.3701
    return str(meters) + " meters correspond to " + str(miles) + " miles, " + str(yards) + " yards, " + str(feet) + " feet, " + str(inches) + " inches."

print(length_conv(1))
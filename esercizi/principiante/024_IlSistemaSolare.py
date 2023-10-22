#Scrivi una funzione che crei una tupla contenente i nomi dei pianeti del sistema solare, la loro tipologia (gassoso o roccioso) e il numero di satelliti naturali conosciuti. Il programma deve quindi stampare a schermo il contenuto della tupla e il numero totale di satelliti.

planets = (
    ("Mercury", "terrestrial", 0),
    ("Venus", "terrestrial", 0),
    ("Earth", "terrestrial", 1),
    ("Mars", "terrestrial", 2),
    ("Jupiter", "gaseous", 95),
    ("Saturn", "gaseous", 83),
    ("Uranus", "gaseous", 27),
    ("Neptune", "gaseous", 14)
)

def planets_info():
    index = 1
    sat = 0
    print("Planets info: ")
    for planet in planets:
        print(str(index) + " - " + planet[0] + ", " + planet[1] + ", " + str(planet[2]) + " satellites")
        sat += planet[2]
        index += 1
    print("Total satellites: " + str(sat))

planets_info()
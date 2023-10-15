#Scrivi una funzione che aggiunga ad una lista 10 colori inseriti dall'utente. Il programma deve poi chiedere all'utente di inserire una lettera e mostrare in output solo i colori nella lista che iniziano con quella lettera.

#Suggerimento: potresti usare la funzione range e il metodo startswith().

def color():
    colors = []
    colors_filter = []
    for i in range(10):
        color = input("Insert color " + str(i+1) + ": ")
        colors.append(color)
    letter = input("Insert a letter: ")
    for color in colors:
        if color.startswith(letter) and color not in colors_filter:
            colors_filter.append(color)
    return colors_filter

print(color())
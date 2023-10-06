#Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione input, in secondi.

def time_conv():
    ds = int(input("Insert days: ")) * 24 * 60 * 60   #from days to seconds
    hs = int(input("Insert hours: ")) * 60 * 60        #from hours to seconds
    ms = int(input("Insert minutes: ")) * 60             #from minutes to seconds
    return str(ds + hs + ms) + " seconds."

print(time_conv())
#Scrivi una funzione che prenda come argomento un set di sport preferiti dall'utente e stampi un messaggio di testo che indica se si tratta di uno sport di squadra o individuale.

#Suggerimento: per valutare la stringa inserita potrebbe essere utile utilizzare il metodo lower.

sports = {
    "basketball": "team",
    "football": "team",
    "tennis": "individual",
    "boxe": "individual",
}

def sport_info(sports):
    sport = input("Insert sport: ").lower()
    if sport in sports.keys():
        return "It's a " + sports[sport] + " sport."
    else:
        return "I don't know this sport."

print(sport_info(sports))
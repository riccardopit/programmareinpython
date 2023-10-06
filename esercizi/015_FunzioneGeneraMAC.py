#Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a un chipset per comunicazioni wireless (es WiFi o Bluetooth), composto da 6 coppie di cifre esadecimali separate da due punti.

#Un esempio di MAC è 02:FF:A5:F2:55:12.

#Scrivi una funzione genera_mac() che generi degli indirizzi MAC pseudo casuali utilizzando il modulo random.

from random import randrange

def genera_mac():
    mac = ""
    for x in range(12):
        mac += f"{randrange(16):X}"
    mac = ":".join(a+b for a,b in zip(mac[::2], mac[1::2]))
    return mac
    
print(genera_mac())
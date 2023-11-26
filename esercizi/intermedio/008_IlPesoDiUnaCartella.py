#Scrivi una funzione che calcoli la somma (espressa in MB) delle dimensioni dei file presenti nella cartella di lavoro utilizzando il modulo os.

import os

def get_size(path="."):
    size = 0
    for file in os.scandir(path):
        size += os.path.getsize(file)
    return f"{(size / 1048576):0.2f} MB"

print(get_size())
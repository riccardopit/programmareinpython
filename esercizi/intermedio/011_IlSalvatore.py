#Scrivi una funzione "file_backup" che sia in grado di effettuare copie di backup di determinati tipi di file, con le seguenti caratteristiche:

#Percorso da scansionare, di backup e tipologia di file da copiare dovranno essere passati dall'utente tramite input
#Il programma dovrà verificare la presenza o meno di una cartella di backup al percorso fornito, e qualora questa non fosse presente dovrà crearla
#La funzione dovrà anche gestire l'eventuale scelta da parte dell'utente, di un percorso da scansionare che non esiste
#Suggerimento: potresti importare i moduli os e shutil.

import os, shutil

def file_backup():
    path_scan = input("Insert path to be scanned: ")
    path_backup = input("Insert backup path: ")
    while path_scan == path_backup:
        print("Path to be scanned and backup path cannot be the same!")
        path_backup = input("Insert backup path: ")
    file_type = input("Insert extention of files you want to backup (e.g. .txt, .pdf etc.): ")
    if os.path.exists(path_scan):
        if not os.path.exists(path_backup):
            os.mkdir(path_backup)
        count = 0
        for root, dirs, files in os.walk(path_scan):
            for file in files:
                if file.endswith(file_type):
                    count += 1
                    file_match = os.path.join(root, file)
                    shutil.copy(file_match, path_backup)
        if count == 0:
            return f"Files to backup not found."
        return f"Backup of {count} files completed successfully!"
    else:
        return f"Path to be scanned not found."

print(file_backup())
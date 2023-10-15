#Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola. Ogni dizionario rappresenta uno studente e contiene nome, cognome, classe e voti. La funzione deve stampare un elenco di tutti gli studenti e calcolare la media dei voti di ciascuno.

students = [
    {"name": "Michael", "surname": "Jordan", "class": "5A", "votes": [8, 9, 7, 7]},
    {"name": "Kobe", "surname": "Bryant", "class": "5B", "votes": [6, 9, 10, 10]},
    {"name": "Stephen", "surname": "Curry", "class": "5C", "votes": [7, 2, 2, 8]},
]

def school(students):
    for student in students:
        avg_votes = sum(student["votes"]) / len(student["votes"])
        student["average"] = avg_votes
    return students

print(school(students))
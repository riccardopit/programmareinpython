#Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.

#Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

#***

#*******

#*********

#*****

num_list = [1, 30, 24, 3, 23]

def isto(num_list):
    text = ""
    for i in num_list:
        text += "*"*i + "\n"
    return text

print(isto(num_list))
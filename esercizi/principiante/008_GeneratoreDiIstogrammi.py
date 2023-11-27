#Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.

#Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

#***

#*******

#*********

#*****

nums = [1, 30, 24, 3, 23]

def isto(num_list):
    text = ""
    n_nums = len(num_list)
    count = 0
    for num in num_list:
        text += "*"*num + "\n" if count < n_nums-1 else "*"*num
        count += 1
    return text

print(isto(nums))
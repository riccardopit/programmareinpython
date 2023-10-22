#Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo (parole che si leggono uguali anche al contrario) oppure no.

def palindrome(text):
    reversed_text = text[::-1]
    if text == reversed_text:
        return "It's a palindrome"
    else:
        return "It's not a palindrome"

text = input("Insert a text: ")
print(palindrome(text))
#Scrivi una funzione "postino" che sia in grado di spedire delle eMail tramite Gmail.

#Suggerimento: puoi usare il modulo smtplib.

import smtplib

def send():
    email_sender = input("Insert your email address: ")
    password_app = input("Insert your app password: ")
    email_receiver = input("Insert the receiver email address: ")
    message = input("Insert your message: ")
    # SMTP server definiton
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # creates SMTP session
    s.ehlo()
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(email_sender, password_app)
    # sending the mail
    s.sendmail(email_sender, email_receiver, message)
    # terminating the session
    s.quit()
    print("Email sent successfully!")

send()
from smtplib import *
import string
import random


class Mailer:

    def verify(self, email: str):
        server = SMTP("smtp.gmail.com", 587)
        server.ehlo()  # Handshake
        server.starttls()

        tb = string.ascii_uppercase + "0123456789"
        verification_code = "".join(random.choices(tb, k=6))
        

        subject = "Subject: Verify your account"
        content = f"Your verification code is: "

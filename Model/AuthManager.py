import mysql.connector
import re

database = mysql.connector.connect(host="remotemysql.com",
                                   database="UyebGlk4V4",
                                   user="UyebGlk4V4",
                                   password="CzQdFyYStO"
                                   )

cursor = database.cursor()


class AuthManager:
    def register(self, username: str, name: str, email: str, password: str):
        valid_mail = re.search(
            r"^[A-Za-z][A-Za-z0-9\.]+@[A-Za-z\.]+$", email
        )

        if valid_mail:
            cursor.execute(
                "INSERT INTO userinfo(email, password, username, name) VALUES('%s', '%s', '%s', '%s');" % (email, password, username, name))
            database.commit()
            print("Account created")

    def login(self, email: str, password: str):
        if email and password:
            valid_mail = re.search(
                r"^[A-Za-z][A-Za-z0-9\.]+@[A-Za-z\.]+$", email)
            if valid_mail:
                cursor.execute(
                    "SELECT * FROM userinfo WHERE email='%s';" % (email)
                )
                account = cursor.fetchone()

                if account:
                    proper_psw = account[1]
                    if password == proper_psw:
                        print('Successfully Logged In')
                    else:
                        print('Wrong password')
                else:
                    # Show error message
                    print('Account with this email id doesn\'t exist!')
            else:
                print("Please enter a valid email id")
        else:
            print('All fields must be filled')

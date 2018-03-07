import string
import random

def password_generator(n):
    symbols = list(string.digits + string.ascii_letters + string.punctuation)
    password = ''
    while 1:
        for i in range(n):
            password += random.choice(symbols)
        yield password

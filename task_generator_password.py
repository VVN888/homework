import string
import random

def password_generator(n):
    while 1:
        password = ''
        for i in range(n):
            password += random.choice(string.digits + string.ascii_letters)
        yield password

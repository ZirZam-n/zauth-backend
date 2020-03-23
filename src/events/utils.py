from random import choice
from string import ascii_uppercase, ascii_lowercase, digits

random_charset = ascii_uppercase + ascii_lowercase + digits


def generate_random_string(length=32):
    return ''.join(choice(random_charset) for _ in range(length))

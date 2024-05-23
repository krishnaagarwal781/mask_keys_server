# generate_keys.py
import random
import string

def generate_random_key(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def generate_keys():
    return {
        "application_key": generate_random_key(),
        "company_key": generate_random_key()
    }

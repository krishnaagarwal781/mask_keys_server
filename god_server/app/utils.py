import random
import string

def generate_key():
    return ''.join(random.choices(string.digits, k=6))

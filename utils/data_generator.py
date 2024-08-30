import random
import string


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_email(domain='burger.com', length=6):
    random_part = generate_random_string(length)
    return f'{random_part}@{domain}'


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


def generate_user_data():
    return {
        'email': generate_random_email(),
        'password': generate_random_password(),
        'name': generate_random_string()
    }

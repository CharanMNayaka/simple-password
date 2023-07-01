import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a random password with default length of 8 characters
random_password = generate_password()
print("Random Password:", random_password)
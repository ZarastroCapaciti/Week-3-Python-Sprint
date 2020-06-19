import random
import string


def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(8):
        password += random.choice(randomSource)

    shuffledPassword = list(password)
    random.SystemRandom().shuffle(shuffledPassword)
    password = ''.join(shuffledPassword)
    return password


print("The Random password is:  ", randomPassword())
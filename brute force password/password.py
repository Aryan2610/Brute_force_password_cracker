import itertools
import string
import time



def guess_passwords(password):
    with open('brute force password\common_passwords.txt', 'r') as passwords:
        data = passwords.read().splitlines()
    for i, match in enumerate(data):
        if match == password:
            return f'The password is: {match}. Found in (Attempt #{i})'
    return 0

def brute_force(password, min_length=4, max_length=10):
    chars = string.ascii_letters + string.digits
    attempts = 0
    for password_length in range(min_length, max_length):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return f'password is {guess}. found in {attempts} guesses.'
            print(guess, attempts)

def get_password(password):
    common = guess_passwords(password)
    return brute_force(password) if common == 0 else common



start_time = time.time()
print(get_password('aabb'))
Total_time = (round(time.time() - start_time, 2))
print(Total_time,'s')
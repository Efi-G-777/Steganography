from sympy import mod_inverse, randprime
from config import *
import random

def generate_rsa_keys():
    p1, p2 = random.choice(prime_list), random.choice(prime_list)
    n = p1 * p2
    t_n = (p1 - 1) * (p2 -1)
    e = random.choice(small_prime_list)
    d = mod_inverse(e, t_n)
    print("Public key: ", (e, n))
    print("Private key: ", (d, n))

# generate_rsa_keys()

# lower_bound = 2**1023  # Smallest 1024-bit number
# upper_bound = 2**1024 - 1  # Largest 1024-bit number
#
# prime = randprime(lower_bound, upper_bound)
# print(prime)

def generate_large_rsa_keys():
    lower_bound = 2 ** 1023
    upper_bound = 2**1024 - 1
    p1, p2 = randprime(lower_bound, upper_bound), randprime(lower_bound, upper_bound)
    n = p1 * p2
    t_n = (p1 - 1) * (p2 - 1)
    e = randprime(2 ** 64, 2 ** 128)
    d = mod_inverse(e, t_n)
    print("Public key: ", (e, n))
    print("Private key: ", (d, n))
generate_large_rsa_keys()
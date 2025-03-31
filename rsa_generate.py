from sympy import mod_inverse
from config import *
import random

def generate_rsa_keys():
    p1 = random.choice(prime_list)
    p2 = random.choice(prime_list)
    n = p1 * p2
    t_n = (p1 - 1) * (p2 -1)
    e = random.choice(small_prime_list)
    d = mod_inverse(e, t_n)
    print("Public key: ", (e, n))
    print("Private key: ", (d, n))

generate_rsa_keys()
def rsa_encrypt(text, key):
    out = ""
    for char in text:
        new_char = pow(ord(char), key[0], key[1])
        out = " ".join([out, str(new_char)])
    return out

def rsa_decrypt(enc_text, key):
    out = ""
    enc_numbers = list(map(int, enc_text.split()))  # Convert space-separated string to integers
    for num in enc_numbers:
        new_char = chr(pow(num, key[0], key[1]))  # Decrypt using modular exponentiation
        out += new_char
    return out

# Example RSA key pairs
prv_key = (8736751, 69336961)
pub_key = (1999, 69336961)

# Encrypt and Decrypt Example
encrypted_text = rsa_encrypt("hello", pub_key)
print("Encrypted:", encrypted_text)

decrypted_text = rsa_decrypt(encrypted_text, prv_key)
print("Decrypted:", decrypted_text)

ps = 30029, 2309
n = 69336961
tn = 69304624

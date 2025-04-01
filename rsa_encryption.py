def get_ord(character):
    char_ord = str(ord(character))
    if len(char_ord) == 2:
        char_ord = "0" + char_ord
    return char_ord

BLOCK_SIZE = 2


def rsa_encrypt(text, key):
    length = len(text)
    pad = ' '
    padding_length = BLOCK_SIZE - length % BLOCK_SIZE if length % BLOCK_SIZE != 0 else 0
    text = text + (pad * padding_length)
    len_message = len(text)
    out = ""
    for i in range(0 , len_message - 1, BLOCK_SIZE):
        block_ord = ""
        for j in range(i, i + BLOCK_SIZE):
            char_ord = get_ord(text[j])
            block_ord += char_ord
        new_char = pow(int(block_ord), key[0], key[1])
        out = " ".join([out, str(new_char)])
    return out

def rsa_decrypt(enc_text, key):
    out = ""
    enc_numbers = list(map(int, enc_text.split()))  # Convert space-separated string to integers
    for num in enc_numbers:
        joined_chars = str(pow(num, key[0], key[1]))
        for i in range(0, len(joined_chars) - 1, 3):
            new_char = chr(int(joined_chars[i:i + 3]))
            out += new_char
    return out

prv_key = (8736751, 69336961)
pub_key = (1999, 69336961)

encrypted_text = rsa_encrypt("hello", pub_key)
print("Encrypted:", encrypted_text)

decrypted_text = rsa_decrypt(encrypted_text, prv_key)
print("Decrypted:", decrypted_text)

# ps = 30029, 2309
# n = 69336961
# tn = 69304624

import pyinputplus as pyip

def get_ord(character):
    char_ord = str(ord(character))
    if len(char_ord) == 2:
        char_ord = "0" + char_ord
    return char_ord

def validate_tuple(text):
    try:
        return tuple(map(int, text.split(',')))  # Convert input to a tuple of integers
    except ValueError:
        raise Exception("Input must be a comma-separated list of integers.")


BLOCK_SIZE = 2


def rsa_encrypt(text):
    key = pyip.inputCustom(validate_tuple, prompt="Enter public key (comma-separated): ")
    length = len(text)
    pad = ' '
    padding_length = BLOCK_SIZE - length % BLOCK_SIZE if length % BLOCK_SIZE != 0 else 0
    text = text + (pad * padding_length)
    len_message = len(text)
    out = []
    for i in range(0 , len_message - 1, BLOCK_SIZE):
        block_ord = ""
        for j in range(i, i + BLOCK_SIZE):
            char_ord = get_ord(text[j])
            block_ord += char_ord
        new_char = str(pow(int(block_ord), key[0], key[1]))
        out.append(new_char)
    out = " ".join(out)
    return out

def rsa_decrypt(enc_text):
    key = pyip.inputCustom(validate_tuple, prompt="Enter private key (comma-separated): ")
    out = ""
    enc_numbers = list(map(int, enc_text.split()))  # Convert space-separated string to integers
    for num in enc_numbers:
        joined_chars = str(pow(num, key[0], key[1]))
        for i in range(0, len(joined_chars) - 1, 3):
            new_char = chr(int(joined_chars[i:i + 3]))
            out += new_char
    return out

# prv_key = (8736751, 69336961)
# pub_key = (1999, 69336961)


Public_key:  (2269, 16065966133721996645003560325471512676136154927011443756306302743208584476807657082808691621756427389744483984246364849804383325342788531704738732387754498688625078195930062132417233453088628991577585208383352296266781660932007959436300783149315849453596527460343958094043181328419891837909814144078663436733554051485875415004172484961150936340484027101887708479152807971143121832578933882106623874548870524876786297050983141679730819091548582654450003731826381121749579085912341501553691171481687294536083637787620856172132168304347696112820015174694889039124528032301052147904442506242158617888986176304348935193393)
Private_key:  (15421628135410537105693148694965603617727873702525749008918081698857777430800827292356690327098060315056626759668833249393542037283646285611688390983045085122884715870751729979905127571981945325542521191652243852476443568757123550309503352004940467214602572414556694900319986308196793487425110271398558380434167970526608622601572129721071360242574474966044032864080827800637603475673214350646096659250679935109128667057313187612671371595707835401630855573401821208182993211205676594895182527116446986440079230572030123705894480255872482764158913825665534222996919861064104870649600321657636934913220421132082998591709, 16065966133721996645003560325471512676136154927011443756306302743208584476807657082808691621756427389744483984246364849804383325342788531704738732387754498688625078195930062132417233453088628991577585208383352296266781660932007959436300783149315849453596527460343958094043181328419891837909814144078663436733554051485875415004172484961150936340484027101887708479152807971143121832578933882106623874548870524876786297050983141679730819091548582654450003731826381121749579085912341501553691171481687294536083637787620856172132168304347696112820015174694889039124528032301052147904442506242158617888986176304348935193393)

encrypted_text = rsa_encrypt("hello")
print("Encrypted:", encrypted_text)

decrypted_text = rsa_decrypt(encrypted_text)
print("Decrypted:", decrypted_text)

# ps = 30029, 2309
# n = 69336961
# tn = 69304624

#subsstitution cipher

alphabet = 'wjkedekjddjkdjedkwsswd!'
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
plaintext = "hello world"

def diskey(alphabet):
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ''.join(alphabet)

def encrypt(plaintext, key, alphabet):
    keykey = dict(zip(alphabet, key))
    return ''.join(keykey.get(c.lower(), c) for c in plaintext)

def decrypt(cipher, key, alphabet):
    keykey = dict(zip(key, alphabet))
    return ''.join(keykey.get(c.lower(), c) for c in cipher)

cipher = encrypt(plaintext, key, alphabet)

print(plaintext)
print(cipher)
print(decrypt(cipher, key, alphabet))






def generate_dicts(plainkey, cipherkey, cipher_to_plain, plain_to_cipher):
    if len(plainkey) != len(cipherkey):
        print('error: plain and cipher keys differ in length')
        exit(1)

    length = len(plainkey)
    curr = 0
    while curr < length:    # load both dictionaries
        plain_to_cipher[plainkey[curr]] = cipherkey[curr]
        cipher_to_plain[cipherkey[curr]] = plainkey[curr]
        curr += 1

    # return plain_to_cipher, cipher_to_plain

def translate(dict, line):
    result = []
    for chr in line:
        result.append(dict[chr])
    return ''.join(result)


cipher_to_plain = {}
plain_to_cipher = {}
generate_dicts('abc', '123', cipher_to_plain, plain_to_cipher)
print('ctp: ' + str(cipher_to_plain))
print('ptc: ' + str(plain_to_cipher))







# d = {}
# d['A'] = '1'
# d['B'] = '2'
# d['C'] = '3'
#
# print(translate(d, 'ABBCB'))

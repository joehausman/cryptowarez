import sys

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

def get_keys(filename):
    lines = []
    try:
        key_file = open(filename, 'r')
        lines = key_file.readlines()
    except IOError:
        print('error: IOError (with key file)')
        exit(1)
    finally:
        key_file.close()

    plainkey = lines[0]
    cipherkey = lines[1]

    return plainkey, cipherkey



# print('ctp: ' + str(cipher_to_plain))
# print('ptc: ' + str(plain_to_cipher))

def user_input():
    while(True):
        stuff = input('>_')
        if stuff.strip() == 'q':
            break

        stuff = stuff.split()
        action = stuff[0]
        text = ' '.join(stuff[1:])
        if action == 'e':     # encrypt
            print('  ' + translate(plain_to_cipher, text))
        elif action == 'd':   # decrypt
            print('  ' + translate(cipher_to_plain, text))

    exit(0)





if len(sys.argv) != 2 and len(sys.argv) != 4:
    print('error: wrong number of command line arguments\n' +
          'usage: python3 sub.py <key_file>\n' +
          '   or  python3 sub.py <key_file> <e/d (encrypt / decrypt)> <cipher_file>')
    exit(1)

cipher_to_plain = {}
plain_to_cipher = {}
plainkey, cipherkey = get_keys(sys.argv[1])
generate_dicts(plainkey, cipherkey, cipher_to_plain, plain_to_cipher)

if len(sys.argv) == 2:
    user_input()
else:   # len(sys.argv) == 4:
    try:
        cipher_file = open(sys.argv[3], 'r')
    except IOError:
        print('error: IOError (with cipher file)')
        exit(1)
    else:
        cipher = cipher_file.read()
        cipher_file.close()
        if sys.argv[2] == 'e':
            print('  ' + translate(plain_to_cipher, cipher))
        elif sys.argv[2] == 'd':
            print('  ' + translate(cipher_to_plain, cipher))
        else:
            # @TODO: print error message
            exit(1)







# d = {}
# d['A'] = '1'
# d['B'] = '2'
# d['C'] = '3'
#
# print(translate(d, 'ABBCB'))

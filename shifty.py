# Joe Hausman

import sys

def shift(cipher, amount):
    c_list = list(cipher)

    i = 0
    while i < len(c_list):
        if ord(c_list[i]) < ord('a') or ord(c_list[i]) > ord('z'):
            i += 1
            continue
        c_list[i] = chr(ord(c_list[i])+amount)
        if ord(c_list[i]) > ord('z'):   # fix positive wrap around
            c_list[i] = chr(ord(c_list[i])-26)
        elif ord(c_list[i]) < ord('a'):   # fix negative wrap around
            c_list[i] = chr(ord(c_list[i])+26)
        i += 1

    return ''.join(c_list)


def bruteforce_shift(cipher):
    amount = 0
    while amount < 26:
        print(str(amount) + '\t' + shift(cipher, amount))
        amount += 1


def user_input():
    print('enter shift amount followed by cipher text')
    print('shift amount defaults to previous amount')
    print('q to exit')
    amount = 0
    while(True):
        stuff = input('>_')
        if stuff.strip() == 'q':
            break
        stuff = stuff.split()
        if stuff[0] == 'brute':
            bruteforce_shift(' '.join(stuff[1:]))
            exit(0)
        try:
            amount = int(stuff[0])
        except ValueError:
            cipher = ' '.join(stuff)
        else:
            cipher = ' '.join(stuff[1:])

        print(shift(cipher, amount))

    exit(0)

if len(sys.argv) == 1:
    user_input()
elif len(sys.argv) == 3:
    try:
        cipher_file = open(sys.argv[2], 'r')
    except IOError:
        print('error: IOError (with cipher file)')
        exit(1)
    else:
        cipher = cipher_file.read()
        cipher_file.close()

    if sys.argv[1] == 'brute':
        bruteforce_shift(cipher)

    try:
        amount = int(sys.argv[1])
    except ValueError:
        print('error: ValueError (with amount)')
        exit(1)

    print(shift(cipher, amount))
else:
    print('error: wrong number of command line arguments\n' +
          'usage: python3 shifty.py\n' +
          '   or  python3 shifty.py <shift_amount> <cipher_file>')
    exit(1)

# urjjb

# Joe Hausman

import sys

def encrypt(num_rails, plaintext):
    # @TODO:    test me
    #           consider modularizing the rail-reading bit
    rails = []
    for x in range(num_rails):
        rails.append([])

    # @TODO: this is the bit that could be modularized
    plain = list(plaintext)
    direction = -1  # direction to move among rails
                    # starts negative to counteract initial dir switch
    curr = 0        # current rail
    while len(plain) > 0:
        # print('curr: ' + str(curr))
        rails[curr].append(plain.pop(0)) # put one plaintext chr on curr rail
        if curr == 0 or curr == num_rails - 1:  # boundary reached
            direction *= -1     # switch direction
        curr += direction

    # @TODO: this bit could also be part of the modularization
    # that would make almost this entire function part of another function hmmmm
    cipher_list = []
    while len(rails) > 0:
        cipher_list.append(''.join(rails.pop(0)))
    cipher = ''.join(cipher_list)
    return cipher



# used by decrypt()
# calculate the number of units appearing in each rail
# return list of corresponding values
def calculate_rail_units(num_rails, units):
    # @TODO:    test me
    curr = 0
    rail_units = []
    cycle_length = (num_rails * 2) - 2
    width = int(units / cycle_length)
    remainder = units % cycle_length

    while curr < num_rails:
        if curr == 0 or curr == num_rails - 1:  # top or bottom rail
            units_per_cycle = 1
        else:
            units_per_cycle = 2

        extra = 0
        if remainder > 0:
            extra = 1
            remainder -= 1

        rail_units.append((units_per_cycle * width) + extra)
        curr += 1

    return rail_units

def decrypt(num_rails, cypher):
    # @TODO:    test me
    #           also finish me
    rail_units = calculate_rail_units(num_rails, len(cypher))
    rail_partition = []
    total = 0
    curr = 0
    while curr < num_rails:
        total += rail_units[curr]
        rail_partition.append(total)
        curr += 1

    rails = []
    part_begin = 0  # partition beginning
    part_end = 0    # partition end
    # print(str(rail_partition))      # debugging
    # curr = 0
    for curr in range(num_rails):
        # curr += 1
        part_begin = part_end
        part_end = rail_partition[curr]
        # print(str(type(part_begin)))     # debugging
        # print(str(type(part_end)))       # debugging
        rails.append(list(cypher[part_begin:part_end]))

    # @TODO: this is where things ought to be finished
    plain_list = []
    nonempty = num_rails    # rails still containing units
    direction = -1
    curr = 0                # current rail
    # print(str(rails))       # debugging
    while nonempty > 0:
        plain_list.append(rails[curr].pop(0))
        if not rails[curr]:
            nonempty -= 1   # current rail is empty
        if curr == 0 or curr == num_rails - 1:  # boundary reached
            direction *= -1     # switch direction
        curr += direction

    plain = ''.join(plain_list)
    return plain

print(encrypt(4, 'here\'s the thing'))
print(decrypt(4, encrypt(4, 'here\'s the thing')))

# Simple python script for modifying Egyptian Mobile Numbers from 10 to 11
# digits
# Just export your Google contacts, pass the contacts name as a parameter to
# the script, then delete the contacts from your Google contacts, and import
# the new contacts file
#
#
# @author: mohammadkotb
#

import sys
from os.path import exists

def error(message):
    print '[ERROR]: ' + message
    exit(1)

def modify(number):
    # modify function
    number = number.replace(' ', '')
    prefix = ''
    if number.startswith('+2'):
        prefix = '+2'
        number = number[2:]
    elif number.startswith('002'):
        prefix = '002'
        number = number[3:]
    if len(number) > 10 and number[0:3] != '015':
        return number
    if number[0:3] == '012':
        number = '0122' + number[3:]
    elif number[0:3] == '017':
        number = '0127' + number[3:]
    elif number[0:3] == '018':
        number = '0128' + number[3:]
    elif number[0:4] == '0150':
        number = '0120' + number[4:]
    elif number[0:3] == '011':
        number = '0111' + number[3:]
    elif number[0:3] == '014':
        number = '0114' + number[3:]
    elif number[0:4] == '0152':
        number = '0112' + number[4:]
    elif number[0:3] == '010':
        number = '0100' + number[3:]
    elif number[0:3] == '016':
        number = '0106' + number[3:]
    elif number[0:3] == '019':
        number = '0109' + number[3:]
    elif number[0:4] == '0151':
        number = '0101' + number[4:]
    return prefix + number

def generate_new_contacts(contacts, modified):
    if not modified:
        return
    first = False
    for line in contacts.readlines():
        contact = line.replace('\x00', '')
        index = contact.find(',Mobile,')

        if first or index == -1:
            if first:
                contact = contact[2:] # handling weird characters
            modified.write(contact)
            first = False
            continue
        else:
            tmp = contact[:index] + ',Mobile,' # contact before Mobile Number
            tmp2 = contact[index+8:] # second half of the contact
            end_number = tmp2.index(',')
            number = tmp2[:end_number] # mobile number
            tmp2 = tmp2[end_number:]

            number = modify(number)
            new_contact = tmp + number + tmp2 # construct new contact
            modified.write(new_contact)

    try:
        modified.close()
    except IOError:
        error('Error occurred while closing the new contacts file')
    print 'Contacts are generated successfully'

def input_file(fin):
    try:
        return open(fin, 'r')
    except IOError:
        error('File "' + fin + '" not found')

def output_file(fout):
    if exists(fout):
        done = False
        overwrite = True
        while not done:
            decision = raw_input('File "' + fout + '" already exists, ' + \
              ' do you want to overwrite it? (y/n): ')
            if decision.lower().find('y') == 0:
                break
            elif decision.lower().find('n') == 0:
                overwrite = False
                break
        if not overwrite:
            return
    return open(fout, 'w')

if __name__ == '__main__':
    fin = 'google.csv'
    fout = 'new_contacts.csv'
    if len(sys.argv) > 3:
        error('Too many arguments passed to the script!')

    if len(sys.argv) >= 2:
        fin = sys.argv[1]
    if len(sys.argv) >= 3:
        fout = sys.argv[2]
    if fin == fout:
        error('Input must be different than output file')

    generate_new_contacts(input_file(fin), output_file(fout))


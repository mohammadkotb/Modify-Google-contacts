
def modify(number):
    # modify function
    number = number.replace(' ', '')
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
    return number

def generate_new_contacts(fin, fout):
    contacts = open(fin, 'r')
    modified = open(fout, 'w')
    
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
            tmp = contact[:index] + ',Mobile,'
            tmp2 = contact[index+8:]
            end_number = tmp2.index(',')
            number = tmp2[:end_number]
            tmp2 = tmp2[end_number:]

            number = modify(number)
            new_contact = tmp + number + tmp2
            modified.write(new_contact)
        
if __name__ == '__main__':
    generate_new_contacts('google.csv', 'new_contacts.csv')


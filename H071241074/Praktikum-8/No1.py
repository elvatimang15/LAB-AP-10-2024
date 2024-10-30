import re

def validasi_string(string):
    if len(string) != 45:
        return False
 
    if not re.match(r'^[a-zA-Z0-9]{40}$', string[:40]):
        return False

    for char in string[:40]:
        if char.isdigit() and int(char) % 2 != 0:
            return False

    if not re.match(r'^[13579\s]{5}$', string[40:]):
        return False

    return True

input_string = input("Masukkan string: ")

if validasi_string(input_string):
    print("True")
else:
    print("False")



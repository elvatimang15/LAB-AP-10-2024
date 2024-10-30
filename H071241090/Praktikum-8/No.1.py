import re

def validasi_input (string) :
    if len(string) != 45 :
        return False

    bagian_pertama = string[:40]
    if not re.fullmatch(r"[a-zA-Z02468]{40}", bagian_pertama):
        return False
    
    bagian_terakhir = string[40:]
    if not re.fullmatch(r"[13579\s]{5}", bagian_terakhir):
        return False

    return True

string = input("Masukkan string: ")

if validasi_input(string) :
    print ("True")
else :
    print ("False")


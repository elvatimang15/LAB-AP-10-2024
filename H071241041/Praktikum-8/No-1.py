import re

def validasi_string(s):
    if len(s) != 45:
        return False
    
    bagian_pertama = r'[a-zA-Z02468]{40}' #{40} itu untuk 40 karakter pertama, huruf atau digit yg genap
    bagian_kedua = r'[13579\s]{5}' #{5} untuk 5 karakter terakhir, digit ganjil dan whitespace(seperti spasi yg tetap dihitung sbgai karakter)
    
    pola = f'^{bagian_pertama}{bagian_kedua}$' #menggabungkan pola
  
    return bool(re.match(pola, s)) #mengecek apakah string sesuai pola
    # bool berfungsi mengonversi hasil dari re.match menjadi nilai boolean

input_string = input("Masukkan string: ")
if validasi_string(input_string):
    print("True")
else:
    print("False")

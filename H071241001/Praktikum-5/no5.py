alphabet_hurufkecil = 'abcdefghijklmnopqrstuvwxyz'
alphabet_hurufbesar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


string = input("Masukkan string: ")
pergeseran = int(input("Masukkan jumlah pergeseran: "))

result = ""

# Iterasi setiap karakter dalam string
for x in string:
    if x in alphabet_hurufkecil:
        # Proses huruf kecil
        index = alphabet_hurufkecil.index(x)  # Dapatkan posisi huruf di abjad
        new_index = (index + pergeseran) % 26  # Geser posisi dan gunakan modulo untuk perputaran
        result += alphabet_hurufkecil[new_index]  # Tambahkan huruf hasil pergeseran ke hasil
    elif x in alphabet_hurufbesar:
        # Proses huruf besar
        index = alphabet_hurufbesar.index(x)  # Dapatkan posisi huruf di abjad
        new_index = (index + pergeseran) % 26  # Geser posisi dan gunakan modulo
        result += alphabet_hurufbesar[new_index]  # Tambahkan huruf hasil pergeseran ke hasil
    else:
        # Karakter lain (angka, simbol) tetap sama
        result += x

# Output hasil enkripsi
print("Cipher:", result)
        
 
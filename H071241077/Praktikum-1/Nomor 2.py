# soal 2
karakter = input("masukkan karakter : ")
kalimat = input("masukkan kalimat : ")

cek_karakter = (karakter in kalimat) and f'karakter ditemukan dalam kalimat "{kalimat}"' or f'{karakter} tidak ditemukan dalam "{kalimat}"'

print(cek_karakter)
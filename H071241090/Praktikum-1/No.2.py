karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan Kalimat : ")

cek_karakter = (karakter in kalimat) and f"{karakter} terdapat dalam kalimat \"{kalimat}\"" or f"{karakter} tidak terdapat dalam kalimat \"{kalimat}\""

print(cek_karakter)
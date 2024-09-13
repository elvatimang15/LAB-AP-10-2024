# 2
karakter = input("Masukkan karakter: ")
kalimat = input("Masukkan kalimat: ")

cek_karakter = (karakter in kalimat) and f"{karakter} terdapat dalam \"{kalimat}\"" or f"{karakter} tidak terdapat dalam \"{kalimat}\""

print(cek_karakter)
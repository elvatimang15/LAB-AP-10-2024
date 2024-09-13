karakter = input("Masukkan sebuah karakter: ")
kalimat = input("Masukkan sebuah kalimat: ")

pesan = (f"Karakter {karakter} merupakan bagian dari Kalimat {kalimat}", f"Karakter {karakter} tidak ditemukan dalam Kalimat {kalimat}")[karakter not in kalimat]

print(pesan)
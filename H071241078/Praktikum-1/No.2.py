karakter = input("Masukkan karakter: ")
kalimat = input("Masukkan kalimat: ")

hasil_list = ["Karakter tidak ditemukan dalam Kalimat", "Karakter merupakan bagian dari Kalimat"]
hasil_index = (karakter in kalimat)
hasil = hasil_list[hasil_index]

print(hasil)
Masukkan_Karakter = input('Masukkan Karakter: ')
Masukkan_Kalimat = input('Masukkan Kalimat: ')

Pesan = 'Karakter merupakan bagian dari Kalimat' * (Masukkan_Karakter in Masukkan_Kalimat) + \
        'Karakter tidak ditemukan dalam Kalimat' * (Masukkan_Karakter not in Masukkan_Kalimat)
print(Pesan)
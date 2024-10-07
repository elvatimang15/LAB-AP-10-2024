def kata_terpanjang(teks):  
    daftar_kata = teks.split()  
    kata_panjang = max(daftar_kata, key=len)  
    return kata_panjang  

input_string = input("Masukkan string: ")
print(kata_terpanjang(input_string))
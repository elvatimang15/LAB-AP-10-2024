# Soal 2 
kata = input("Masukkan kata: ")
kata_kata = kata.split()
huruf_awal = [kata[0].upper() for kata in kata_kata]
akronim = ''.join(huruf_awal)
print(akronim)

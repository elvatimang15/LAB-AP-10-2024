karakter = input("Masukkan karakter: ")
kalimat = input("Masukkan kalimat: ")
print(f"karakter {'ditemukan di dalam' * (karakter in kalimat) + 'tidak ditemukan di dalam' *(karakter not in kalimat)} kalimat")

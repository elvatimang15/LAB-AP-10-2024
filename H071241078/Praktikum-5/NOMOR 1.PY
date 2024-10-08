def palindrome(s):
    # Menghapus spasi dan mengubah ke huruf kecil
    s = s.replace(" ", "").lower()
    
    # Memeriksa apakah string sama dengan kebalikannya
    if s == s[::-1]:
        
        print("Palindrome")
    else:
        print("Bukan Palindrome")

# Mengambil input dari pengguna
input_string = input("Masukkan string: ")
palindrome(input_string)

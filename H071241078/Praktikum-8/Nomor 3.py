import re

def is_valid_username(username):
    # Pola regex untuk username: huruf atau angka, panjang antara 5-20 karakter
    pattern = r"^[A-Za-z0-9]{5,20}$"
    return re.search(pattern, username)

def is_valid_email(email):
    # Pola regex untuk email: format 'teks@teks.com' atau 'teks@teks.co.id'
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|co\.id)$"
    return re.search(pattern, email)

def is_valid_password(password):
    # Pola regex untuk password: minimal satu huruf besar, satu huruf kecil, satu angka, panjang minimal 8 karakter
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
    return re.search(pattern, password)

# -------- Program utama --------
username = input("Masukkan username: ")
if is_valid_username(username):
    email = input("Masukkan email: ")
    if is_valid_email(email):
        password = input("Masukkan password: ")
        if is_valid_password(password):
            print(f"\nRegistrasi berhasil! Selamat datang, {username}!")
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")

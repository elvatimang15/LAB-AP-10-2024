import re

def is_valid_username(username):
    # Username minimal 5 karakter, maksimal 20 karakter, terdiri dari huruf kecil, huruf besar, atau angka
    pattern = r"^[A-Za-z0-9]{5,20}$"
    return re.search(pattern, username)

def is_valid_email(email):
    # Email format username@domain.com atau username@domain.co.id, dengan huruf kecil dan angka sebelum tanda @
    pattern = r"^[a-z0-9]+@[a-z]+\.(com|co\.id)$"
    return re.search(pattern, email)

def is_valid_password(password):
    # Password minimal 8 karakter, mengandung minimal 1 huruf besar, 1 huruf kecil, dan 1 angka, tanpa karakter khusus
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
    return re.search(pattern, password)

# --------
username = input("Masukkan username: ")

if is_valid_username(username):
    email = input("Masukkan email: ")

    if is_valid_email(email):
        password = input("Masukkan password: ")

        if is_valid_password(password):
            print(f"\nRegistrasi berhasil! Selamat Datang {username}!")
        else:
            print("\nPassword yang kamu input berisiko dihack. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")

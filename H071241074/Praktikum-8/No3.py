import re

def validasi_username(username):
    if not (5 <= len(username) <= 20):
        return "Username harus antara 5 hingga 20 karakter.", False
    if not re.search(r'[a-zA-Z0-9]', username):
        return "Username harus terdiri dari huruf atau angka.", False
    return "Username valid.", True

def validasi_email(email):
    pola = re.compile(r'^[a-z]+[a-z0-9]*@[a-z]+\.[a-z]{2,}(?:\.[a-z]{2,})?$')
    if not pola.match(email):
        return "Email yang kamu input tidak valid. Registrasi gagal!", False
    return "Email valid.", True

def validasi_password(password):
    if len(password) < 8:
        return "Password harus minimal 8 karakter.", False
    if not re.search(r'[A-Z]', password):
        return "Password harus mengandung setidaknya satu huruf kapital.", False
    if not re.search(r'[a-z]', password):
        return "Password harus mengandung setidaknya satu huruf kecil.", False
    if not re.search(r'\d', password):
        return "Password harus mengandung setidaknya satu angka.", False
    if re.search(r'[^a-zA-Z0-9]', password):
        return "Password hanya boleh mengandung huruf dan angka.", False
    return "Password valid.", True

username = input("Masukkan Username: ")
email = input("Masukkan Email: ")
password = input("Masukkan Password: ")

username_msg, username_valid = validasi_username(username)
email_msg, email_valid = validasi_email(email)
password_msg, password_valid = validasi_password(password)

if username_valid and email_valid and password_valid:
    print(f"Registrasi berhasil! Selamat datang, {username}!")
else:
    if not username_valid:
        print(username_msg)
    if not email_valid:
        print(email_msg)
    if not password_valid:
        print(password_msg)

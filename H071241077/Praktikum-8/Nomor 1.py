import re

# Pattern untuk memvalidasi input sesuai dengan spesifikasi
string_pattern = r'^[A-Za-z24680]{40}[13579\s]{5}$'

# Meminta input dari pengguna
string = input('Input string: ')

# Memeriksa apakah input memiliki panjang 45 karakter dan cocok dengan pola
if len(string) == 45 and re.match(string_pattern, string):
    print('True')
else:
    print('False')


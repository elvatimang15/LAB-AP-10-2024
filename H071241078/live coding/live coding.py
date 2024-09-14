import math

# Mendapatkan input dari pengguna
x = float(input("Masukkan panjang sisi X: "))
y = float(input("Masukkan panjang sisi Y: "))

# Menghitung panjang sisi Z menggunakan teorema Pythagoras
z = math.sqrt(x**2 + y**2)

# Menghitung luas segitiga
luas = (x * y) / 2

# Menghitung keliling segitiga
keliling = x + y + z

# Menampilkan hasil
print("Luas Permukaan: {:.2f}".format(luas))
print("Keliling: {:.2f}".format(keliling))
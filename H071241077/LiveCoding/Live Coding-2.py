import math

sisi_X = float(input("Masukkan panjang sisi X : "))
sisi_Y = float(input("Masukkan panjang sisi Y : "))
sisi_Z = math.sqrt(sisi_X**2 + sisi_Y**2)

# Hitung setengah keliling
# S = (sisi_X + sisi_Y + sisi_Z)/2

# Hitung luas
luas = (1/2 * sisi_X * sisi_Y)

# Hitung keliling
keliling = sisi_X + sisi_Y + sisi_Z

print(f"luas permukaan : {luas:.2f}")
print(f"keliling : {keliling:.2f}")
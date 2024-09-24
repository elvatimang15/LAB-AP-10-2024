# import math

# sisi1 = float(input("Panjang sisi X: "))
# sisi2 = float(input("Panjang sisi Y: "))

# # Mencari sisi3
# sisi3 = math.sqrt (sisi1**1 + sisi2**2)

# # Luas segitiga
# Luas = 0.5 * sisi1 * sisi2

# # Keliling segitiga
# Keliling = sisi1 + sisi2 + sisi3 

# # output
# print(f"Luas Permukaan: {Luas:.2f}")
# print(f"Keliling: {Keliling:.2f}")

sisi1 = float(input("Panjang sisi X: "))
sisi2 = float(input("Panjang sisi Y: "))

# Mencari sisi3
sisi3 = (sisi1**2 + sisi2**2)**0.5

# Luas segitiga
Luas = 0.5 * sisi1 * sisi2

# Keliling segitiga
Keliling = sisi1 + sisi2 + sisi3 

# output
print(f"Luas Permukaan: {Luas:.2f}")
print(f"Keliling: {Keliling:.2f}")
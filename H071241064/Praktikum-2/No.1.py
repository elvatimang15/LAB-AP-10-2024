# 1

# Meminta input dari pengguna
a = float(input("Masukkan panjang sisi pertama: "))
b = float(input("Masukkan panjang sisi kedua: "))
c = float(input("Masukkan panjang sisi ketiga: "))
              
# Cek bentuk segitiga
if a == b == c:
  print("Segitiga Sama Sisi")
elif a == b or a == c or b == c:
  print("Segitiga Sama Kaki")
elif a + b > c and a + c > b and b + c > a:
  print("Segitiga Sembarang")
else:
  print("Tidak dapat membentuk segitiga yang valid")
a = float(input("Masukkan panjang sisi pertama: "))
b = float(input("Masukkan panjang sisi kedua: "))
c = float(input("Masukkan panjang sisi ketiga: "))

if a + b > c and c - b < a and c - a < b:
        if a == b == c:
            print ("Segitiga Sama Sisi")
        elif a == b or b == c or a == c:
            print ("Segitiga Sama Kaki")
        else:
            print ("Segitiga Sembarang")
if not (a + b > c and c - b < a and c - a < b):
            print ("Tidak dapat membentuk segitiga yang valid")
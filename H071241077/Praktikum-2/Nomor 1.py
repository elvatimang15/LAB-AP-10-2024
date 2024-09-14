# Soal 1
sisi_1 = float(input("masukkan panjang sisi pertama : "))
sisi_2 = float(input("masukkan panjang sisi kedua : "))
sisi_3 = float(input("masukkan panjang sisi ketiga : "))

if sisi_1 == sisi_2 == sisi_3:
    print("segitiga sama sisi")
elif sisi_1 == sisi_2 or sisi_2 == sisi_3 or sisi_1 == sisi_3:
    print("segitiga sama kaki")
elif sisi_1 + sisi_2 > sisi_3 and sisi_1 + sisi_3 > sisi_2 and sisi_2 + sisi_3 > sisi_1:
    print("segitiga sembarang")
else:
    print("tidak dapat membentuk segitiga yang valid")
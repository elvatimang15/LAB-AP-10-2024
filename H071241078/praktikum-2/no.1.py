a = float(input("Masukkan Panjang sisi pertama: "))
b = float(input("Masukkan Panjang sisi kedua: "))
c = float(input("Masukkan Panjang sisi ketiga: "))

# Check if the inputs form a valid triangle
if a + b > c and a + c > b and b + c > a:
    # Check the type of triangle
    if a == b == c:
        print("Segitiga Sama Sisi")
    elif a == b or a == c or b == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")
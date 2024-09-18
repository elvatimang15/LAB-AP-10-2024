a = int(input("Masukkan panjang sisi a: "))
b = int(input("Masukkan panjang sisi b: "))
c = int(input("Masukkan panjang sisi c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Segitiga sama sisi")
    elif a == b or b == c or a == c:
        print("Segitiga sama kaki")
    else:
        print("Segitiga sembarang")
else:
    print("Ini bukan segitiga yang valid") 
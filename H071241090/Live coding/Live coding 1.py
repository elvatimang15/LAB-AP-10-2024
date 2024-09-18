import math
print ("Menghitung luas permukaan dan keliling segitiga")
x = int(input("Panjang sisi x : "))
y = int(input("Panjang sisi y : "))

z = math.sqrt (x**2 + y**2)
luas = 0.5 * x * y
keliling= x + y + z

print (f"Luas permukaan : {luas}")
print (f"Keliling : {keliling}")


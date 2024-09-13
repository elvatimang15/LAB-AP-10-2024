# 4
celcius = float(input("Masukkan suhu dalam celcius: "))

# konversi suhu celcius ke suhu lain
kelvin = celcius + 273.15
reamur = celcius * 4 / 5
fahrenheit = celcius * 9 / 5 + 32
print(f"Hasil konversi dari suhu 50 derajat celcius ke kelvin: {kelvin:.2f}K")
print(f"Hasil konversi dari suhu 50 derajat celcius ke reamur: {reamur:.2f}°Re")
print(f"Hasil konversi dari suhu 50 derajat celcius ke fahrenheit: {fahrenheit:.2f}°F")
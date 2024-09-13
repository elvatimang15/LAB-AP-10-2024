Celcius = float(input("Masukkan Suhu dalan Celcius: "))
# celcius -> Kelvin
CK = Celcius + 273.15
# celcius -> Reamur
CR = Celcius * 4 / 5
# celcius -> Fahrenheit
CF = (Celcius * 9/5) + 32

print (f"Hasil konversi dari suhu {Celcius} derajat Celcius ke Kelvin adalah: {CK}K")
print (f"Hasil konversi dari suhu {Celcius} derajat Celcius ke Reamus adalah: {CR}R")
print (f"Hasil konversi dari suhu {Celcius} derajat Celcius ke Fahrenheit adalah: {CF}F")
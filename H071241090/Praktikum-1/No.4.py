#Konversi Suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit
celcius =float(input("Masukkan Suhu dalam Celcius : "))

kelvin = celcius + 273.15
reamur = celcius * (4/5)
fahrenheit = celcius * (9/5) + 32

print ("Hasil konversi dari suhu celcius ke kelvin adalah : ", kelvin,"K")
print ("Hasil konversi dari suhu celcius ke reamur adalah : ", reamur,"R")
print ("Hasil konversi dari suhu celcius ke fahrenheit adalah : ", fahrenheit,"F")
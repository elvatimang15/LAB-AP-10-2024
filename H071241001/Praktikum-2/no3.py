nilaiakhir= int(input("Masukkan nilai akhir: "))
kehadiran= int(input("Masukkan persentase kehadiran: "))

if kehadiran >= 75:
    if nilaiakhir >= 85:
        print("Lulus dengan predikat A")
    elif nilaiakhir >= 70:
        print("Lulus dengan predikat B")
    elif nilaiakhir >= 60:
        print("Lulus dengan predikat C")
    elif nilaiakhir <  60:
        tugasplus = int(input("Masukkan nilai tambahan: "))
        if tugasplus >= 70:
            print("Lulus dengan predikat C")
        else:
            print("tidak lulus")
else:
    print("tidak lulus")
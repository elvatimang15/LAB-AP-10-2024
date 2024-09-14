Nilai_akhir = float(input("Masukkan nilai akhir : "))
Persentase_kehadiran = int(input("Masukkan persentase kehadiran : "))

if Persentase_kehadiran >= 75:
    if Nilai_akhir >= 85:
        print("Lulus dengan Predikat A")
    elif Nilai_akhir >= 70:
        print("Lulus dengan Predikat B")
    elif Nilai_akhir >= 60:
        print("Lulus dengan Predikat C")
    

    if Nilai_akhir < 60 and Persentase_kehadiran >= 75:
        tugas_tambahan = float(input("Masukkan nilai tugas tambahan : "))
        if tugas_tambahan > 70:
            print("Lulus dengan Predikat C")
    else:
        print("Tidak lulus")

else: 
   print("Tidak Lulus")
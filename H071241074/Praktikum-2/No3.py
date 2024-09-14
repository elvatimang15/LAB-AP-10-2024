nilai_akhir = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))
tugas_tambahan = input("Apakah semua tugas tambahan selesai dengan nilai di atas 70? (ya/tidak): ")

if kehadiran < 75:
    print("Tidak Lulus")
else:
    if nilai_akhir >= 85 and nilai_akhir <= 100:
        print("Lulus dengan Predikat A")
    elif nilai_akhir >= 70 and nilai_akhir < 85:
        print("Lulus dengan Predikat B")
    elif nilai_akhir >= 60 and nilai_akhir < 70:
        print("Lulus dengan Predikat C")
    elif nilai_akhir < 60:
        if tugas_tambahan == "ya":
            print("Lulus dengan Predikat C")
        else:
            print("Tidak Lulus")
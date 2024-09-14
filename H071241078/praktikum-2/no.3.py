nilai = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))


if kehadiran >= 75:
    if nilai >= 85:
        print("Lulus dengan Predikat A")
    elif nilai >= 70: 
      print("Lulus dengan Predikat B")
    elif nilai >= 60: 
      print("Lulus dengan Predikat C")
    else:
        nilai_tugas = int(input("masukkan nilai tambahan: "))
        if nilai_tugas >= 70:
           print("Lulus dengan Predikat C")
        else:
           print("Tidak Lulus")
else:
    print("Tidak Lulus")


    
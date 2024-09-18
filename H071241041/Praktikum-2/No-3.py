nilai_akhir = int(input("Masukkan nilai akhir mahasiswa: "))
kehadiran = int(input("Masukkan persentase kehadiran mahasiswa: "))
tugas_tambahan = int(input("Masukkan nilai tambahan: "))

if kehadiran >= 75:
    if nilai_akhir >= 85:
        print("Lulus dengan Predikat A")
    elif 70 <= nilai_akhir < 85:
        print("Lulus dengan Predikat B")
    elif 60 <= nilai_akhir < 70:
        print("Lulus dengan Predikat C")
    else:
        if tugas_tambahan >= 70:
            print("Lulus dengan Predikat C karena tugas tambahan diselesaikan dengan baik")
        else:
            print("Mahasiswa Tidak Lulus karena nilai di bawah 60 dan tugas tambahan tidak diselesaikan")
else:
    print("mahasiswa tidak lulus")

nilai = int(input("Masukkan nilai : "))
hadir = int(input("Masukkan persentase kehadiran : "))

if hadir >= 75:
    if 85 <= nilai <= 100:
        print("Lulus dengan Predikat A")
    elif 70 <= nilai <= 84:
        print("Lulus dengan Predikat B")
    elif 60 <= nilai < 70:
        print("Lulus dengan Predikat C")
    elif nilai < 60:
        tugas = int(input("Masukkan nilai tambahan: "))
        if tugas >= 70 :
            print("Lulus dengan Predikat C")
        else:
            print("Tidak Lulus")
else:
    print ("Tidak Lulus")
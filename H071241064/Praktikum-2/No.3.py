# 3

# Input nilai akhir dan kehadiran
nilai_akhir = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan presentase kehadiran: "))

# Kriteria Kelulusan
if kehadiran >= 75:
    if nilai_akhir >= 85:
        predikat = 'Predikat A'
    elif nilai_akhir >= 70:
        predikat = 'Predikat B'
    elif nilai_akhir >= 60: 
        predikat = 'Predikat C'
    else: 
        nilai_tugas = int(input("Masukkan nilai tugas tambahan: "))
        if nilai_tugas > 70:
            predikat = 'Predikat C'
        else:
            predikat = 'Tidak Lulus'
else:
    predikat = 'Tidak Lulus'

print(predikat)
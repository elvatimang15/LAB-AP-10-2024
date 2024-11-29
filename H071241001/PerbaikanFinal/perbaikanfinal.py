# Buatlah program yang dapat mendata informasi mahasiswa dengan ketentuan sebagai berikut:

# Input data mahasiswa dilakukan dalam format:

# Nama
# NIM (Nomor Induk Mahasiswa)
# Nilai (skor antara 0-100)

# Validasi input data:
# Nama mahasiswa akan otomatis diubah menjadi format kapitalisasi (contoh: andi menjadi Andi).
# NIM harus memenuhi format: huruf diikuti oleh 9 digit angka (contoh: A123456789).
# Nilai harus berupa angka dalam rentang 0 hingga 100.

# Klasifikasi nilai mahasiswa berdasarkan:
# Sangat Baik jika skor ≥ 85.
# Baik jika skor antara 70 dan < 85.
# Kurang jika skor < 70.

# Program harus membagi data mahasiswa menjadi dua kategori:
# Data valid.
# Data tidak valid (contoh: format salah, NIM tidak sesuai, atau skor tidak valid).

# Output program:
# Tampilkan daftar mahasiswa yang valid, termasuk nama, NIM, nilai, dan kategori.
# Tampilkan daftar mahasiswa dengan data tidak valid.
# Data akan terus dimasukkan hingga pengguna mengetikkan perintah selesai.


import re

def validasiNIM(nim):
    pattern = r'^[A-Za-z]\d{9}$'  
    return bool(re.match(pattern, nim))

def validasiskor(skor):
    return 0 <= skor <= 100

def kategoriskor(skor):
    if skor >= 85:
        return "Sangat Baik"
    elif 70 <= skor < 85:
        return "Baik"
    else:
        return "Kurang"

def prosespendataan(data):
    validasimahasiswa = []
    invalidata = []

    for mahasiswa in data:
        try:
            nama, nim, skor = mahasiswa
            skor = int(skor) 

            if validasiNIM(nim) and validasiskor(skor):
                nama = nama.title() 
                kategori = kategoriskor(skor)  
                validasimahasiswa.append({"nama": nama, "nim": nim, "score": skor, "kategori": kategori})
            else:
                invalidata.append(mahasiswa)
        except ValueError:
            print(f"Kesalahan: Data mahasiswa tidak valid: {mahasiswa}")
            invalidata.append(mahasiswa)

    return validasimahasiswa, invalidata


def print_results(validasimahasiswa, invalidata):
    if validasimahasiswa:
        print("\nData mahasiswa valid:")
        for i, mahasiswa in enumerate(validasimahasiswa, start=1):
            print(f"{i}. Nama: {mahasiswa['nama']}")
            print(f"   NIM: {mahasiswa['nim']}")
            print(f"   Nilai: {mahasiswa['score']}")
            print(f"   Kategori: {mahasiswa['kategori']}")
    else:
        print("Tidak ada data mahasiswa valid.")

    if invalidata:
        print("\nData tidak valid ditemukan:")
        for mahasiswa in invalidata:
            print(f"- {', '.join(mahasiswa)}")

data_mahasiswa = []
print("Masukkan data mahasiswa dalam format: Nama, NIM, Nilai")
print("Ketik 'selesai' untuk berhenti.")
while True:
    user_input = input("Data: ").strip()
    if user_input.lower() == 'selesai':
        break
    try:
        nama, nim, skor = user_input.split(",")  
        data_mahasiswa.append((nama.strip(), nim.strip(), skor.strip()))
    except ValueError:
        print("Format data salah! Pastikan format: Nama, NIM, Nilai")


validasimahasiswa, invalidata = prosespendataan(data_mahasiswa)

print_results(validasimahasiswa, invalidata)

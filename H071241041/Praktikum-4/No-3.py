# def hitung_langkah(n):
#     if not isinstance(n, int) or n <= 0:
#         return "Input tidak Valid"
    
#     step_count = 0
    
#     # Lakukan perulangan hingga n menjadi 1
#     while n != 1:
#         print(n)  # Cetak nilai n di setiap langkah
#         if n % 2 == 0:
#             n //= 2  # Jika genap, bagi 2
#         else:
#             n = n * 3 + 1  # Jika ganjil, kalikan 3 lalu tambah 1
#         step_count += 1  # Tambahkan jumlah langkah
    
#     print(n)  # Cetak 1 sebagai langkah terakhir
#     return f"Jumlah langkah: {step_count}"

# try:
#     n = int(input("Masukkan bilangan bulat positif: "))
#     print(hitung_langkah(n))
# except ValueError:
#     print("Input tidak Valid")
    
def validasi_input(n):
    if isinstance(n, int) and n > 0:
        return True
    return False

def proses_bilangan(n):
    # Fungsi untuk menghitung langkah-langkah hingga mencapai angka 1
    langkah = 0
    while n != 1:
        print(float(n))  # Menampilkan nilai dalam format float
        if n % 2 == 0:
            n = n / 2  # Jika genap, bagi 2 (menggunakan pembagian float)
        else:
            n = 3 * n + 1  # Jika ganjil, kalikan 3 dan tambahkan 1
        langkah += 1  # Tambah langkah setiap kali iterasi
    print(float(n))  # Terakhir tampilkan 1.0
    return langkah

def main():
    try:
        # Meminta input dari pengguna
        angka = int(input("Masukan angka: "))
        
        # Validasi apakah input valid
        if not validasi_input(angka):
            print("Input tidak Valid")
        else:
            # Proses bilangan dan hitung jumlah langkah
            jumlah_langkah = proses_bilangan(angka)
            print(f"Jumlah langkah: {jumlah_langkah}")
    except ValueError:
        # Jika input bukan angka, tampilkan pesan kesalahan
        print("Input tidak Valid")

# Menjalankan program
main()

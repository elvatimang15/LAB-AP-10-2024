import time
import os

daftar_film = []
daftar_tiket = []

if not os.path.exists('tiket'):
    os.makedirs('tiket')

def gacha_tiket():
    return f"TICK{time.strftime('%d%m%Y%H%M%S')}"

def simpan_tiket(informasi_tiket):
    file_name = f"tiket/{informasi_tiket['id_tiket']}.txt"
    with open(file_name, "w") as file:
        tiket_string = (
            "+" + "-" * 44 + "+\n"
            "|" + " " * 15 + "TIKET BIOSKOP" + " " * 16 + "|\n"
            "+" + "-" * 44 + "+\n"
            f"| ID Tiket : {informasi_tiket['id_tiket']}" + " " * 14 + "|\n"
            f"| Film     : {informasi_tiket['film']}" + " " * 30 + "|\n"
            f"| Tanggal  : {informasi_tiket['waktu']}" + " " * 13 + "|\n"
            "+" + "-" * 44 + "+\n"
            "|" + " " * 7 + "Terima kasih telah membeli" + " " * 11 + "|\n"
            "|" + " " * 13 + "tiket Anda!" + " " * 20 + "|\n"
            "+" + "-" * 44 + "+\n"
        )
        file.write(tiket_string)


def tampilkan_tiket(tiket):
    print("+" + "-" * 44 + "+")
    print("|" + " " * 15 + "TIKET BIOSKOP" + " " * 16 + "|")
    print("+" + "-" * 44 + "+")
    print(f"| ID Tiket : {tiket['id_tiket']}" + " " * 14 + "|")
    print(f"| Film     : {tiket['film']}" + " " * 30 + "|")
    print(f"| Tanggal  : {tiket['waktu']}" + " " * 13 + "|")
    print("+" + "-" * 44 + "+")
    print("|" + " " * 7 + "Terima kasih telah membeli" + " " * 11 + "|")
    print("|" + " " * 13 + "tiket Anda!" + " " * 20 + "|")
    print("+" + "-" * 44 + "+")

def tampilkan_daftar_film():
    if not daftar_film:
        print("Belum ada film yang tersedia.")
    else:
        print("Daftar film:")
        for indeks, film in enumerate(daftar_film):
            print(f"{indeks + 1}. {film}")

def tambah_film():
    while True:
        print("\n--- Tambah Film ---")
        nama_film = input("Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
        if nama_film:
            daftar_film.append(nama_film)
            print(f"Film '{nama_film}' telah ditambahkan.")
        else:
            break

def hapus_film():
    while True:
        print("\n--- Hapus Film ---")
        tampilkan_daftar_film()
        try:
            nomor_film = int(input("Masukkan nomor film yang ingin dihapus (atau tekan Enter untuk kembali): "))
            if 1 <= nomor_film <= len(daftar_film):
                film_dihapus = daftar_film.pop(nomor_film - 1)
                print(f"Film '{film_dihapus}' telah dihapus.")
            else:
                print("Nomor film tidak valid.")
        except ValueError:
            break

def tampilkan_daftar_tiket():
    if not daftar_tiket:
        print("Belum ada tiket yang terjual.")
    else:
        for indeks, tiket in enumerate(daftar_tiket):
            print(f"{indeks + 1}. {tiket['id_tiket']}")

def hapus_tiket():
    while True:
        print("\n--- Hapus Tiket ---")
        tampilkan_daftar_tiket()
        try:
            nomor_tiket = int(input("Masukkan nomor tiket yang ingin dihapus (atau tekan Enter untuk kembali): "))
            if 1 <= nomor_tiket <= len(daftar_tiket):
                tiket_dihapus = daftar_tiket.pop(nomor_tiket - 1)
                file_name = f"tiket/{tiket_dihapus['id_tiket']}.txt"
                if os.path.exists(file_name):
                    os.remove(file_name)
                print(f"Tiket '{tiket_dihapus['id_tiket']}' berhasil dihapus.")
            else:
                print("Nomor tiket tidak valid.")
        except ValueError:
            break

def beli_tiket():
    tampilkan_daftar_film()
    if daftar_film:
        try:
            nomor_film = int(input("Masukkan nomor film yang ingin dibeli tiketnya: "))
            if 1 <= nomor_film <= len(daftar_film):
                id_tiket = gacha_tiket()
                nama_film = daftar_film[nomor_film - 1]
                waktu_pembelian = time.strftime("%d-%m-%Y %H:%M:%S")
                informasi_tiket = {
                    "id_tiket": id_tiket,
                    "film": nama_film,
                    "waktu": waktu_pembelian
                }
                daftar_tiket.append(informasi_tiket)
                simpan_tiket(informasi_tiket)

                file_name = f"tiket/{id_tiket}.txt"

                print(f"Tiket berhasil dibeli. ID tiket Anda: {id_tiket}")
                print(f"File tiket telah dibuat: {file_name}")
                tampilkan_tiket(informasi_tiket)
            else:
                print("Nomor film tidak valid.")
        except ValueError:
            print("Input tidak valid.")

def menu_admin():
    while True:
        print("\n---- Menu Admin ----")
        print("1. Tambah film")
        print("2. Hapus film")
        print("3. Daftar Tiket")
        print("4. Kembali")
        pilihan = input("Pilih opsi (1/2/3/4): ")
        try:
            if pilihan == "1":
                tambah_film()
            elif pilihan == "2":
                hapus_film()
            elif pilihan == "3":
                while True:
                    print("\n--- Daftar Tiket ---")
                    print("1. Lihat Daftar Tiket")
                    print("2. Lihat Detail Tiket")
                    print("3. Hapus Tiket")
                    print("4. Kembali")
                    pilihan = input("Pilih opsi (1/2/3/4): ")
                    if pilihan == "1":
                        tampilkan_daftar_tiket()
                    elif pilihan == "2":
                        try:
                            nomor_tiket = int(input("Masukkan nomor tiket untuk dilihat detailnya: "))
                            if 1 <= nomor_tiket <= len(daftar_tiket):
                                tampilkan_tiket(daftar_tiket[nomor_tiket - 1])
                            else:
                                print("Nomor tiket tidak valid.")
                        except ValueError:
                            print("Input tidak valid.")
                    elif pilihan == "3":
                        hapus_tiket()
                    elif pilihan == "4":
                        break
                    else:
                        print("Pilihan tidak valid, coba lagi.")
            elif pilihan == "4":
                break
            else:
                print("Pilihan tidak valid, coba lagi.")
        except ValueError:
            print("Input tidak valid.")

def menu_pengunjung():
    while True:
        print("\n--- Menu Pengunjung ---")
        print("1. Tampilkan Daftar Film")
        print("2. Beli Tiket")
        print("3. Kembali")
        pilihan = input("Pilih opsi (1/2/3): ")
        try:
            if pilihan == "1":
                tampilkan_daftar_film()
            elif pilihan == "2":
                beli_tiket()
            elif pilihan == "3":
                break
            else:
                print("Pilihan tidak valid, coba lagi.")
        except ValueError:
            print("Input tidak valid.")

def pilih_peran():
    while True:
        print("\n--- Sistem Pemesanan Tiket Bioskop ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        peran = input("Pilih peran (1/2/3): ")
        try:
            if peran == "1":
                menu_admin()
            elif peran == "2":
                menu_pengunjung()
            elif peran == "3":
                print("Keluar dari sistem.")
                break
            else:
                print("Pilihan tidak valid, coba lagi.")
        except ValueError:
            print("Input tidak valid.")

pilih_peran()

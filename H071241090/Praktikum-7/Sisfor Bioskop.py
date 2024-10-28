import os
from datetime import datetime

def sistem_informasi_bioskop() :
    folder = '/Users/admin/Documents/coding/PRAKTIKUM/Tugas 7/films'

    def tambah_film(nama_file):
        folder = '/Users/admin/Documents/coding/PRAKTIKUM/Tugas 7/films'  
        path_file = os.path.join(folder, nama_file)

        with open(path_file, 'w') as file:
            print(f"Film '{nama_file}' berhasil dibuat.")

    def hapus_film(nama_file):
        folder = '/Users/admin/Documents/coding/PRAKTIKUM/Tugas 7/films'  
        path_file = os.path.join(folder, nama_file)
        
        try:
            os.remove(path_file)
            print(f"Film '{nama_file}' berhasil dihapus.")
        except FileNotFoundError:
            print ("Film tidak ditemukan")

    def daftar_film():
        folder = '/Users/admin/Documents/coding/PRAKTIKUM/Tugas 7/films'  
        files = os.listdir(folder) 
        if files:
            print("Daftar film:")
            for index, file in enumerate(files, start=1):
                print(f"{index}. {file}")
            print('0. Kembali') 
        else :
            print ("Tidak terdapat film tersedia.")
        return files if files else []  

    def daftar_tiket():
        folder = '/Users/admin/Documents/coding/PRAKTIKUM/Tugas 7/tickets'  
        files = os.listdir(folder) 
        if files:
            print("Daftar tiket:")
            for index, file in enumerate(files, start=1):
                print(f"{index}. {file}")
        else :
            print ("Tidak terdapat tiket tersedia.")
        return files if files else []

    def id_tiket():
        current_time = datetime.now()
        ticket_id = current_time.strftime("TICK%d%m%Y%H%M%S")
        readable_time = current_time.strftime("%d %B %Y jam %H:%M:%S")
        return ticket_id, readable_time

    def beli_tiket():
        daftar_film_list = daftar_film()

        if not daftar_film_list:
            return 
    
        while True:
            opsi_film = int(input("Pilih nomor film yang ingin ditonton (0 untuk kembali): "))
            if opsi_film == 0:
                print("Kembali ke menu pengunjung.")
                return
            elif 1 <= opsi_film <= len(daftar_film_list):
                nama_film = daftar_film_list[opsi_film - 1]
                break
            else:
                print("Nomor film tidak valid. Silakan coba lagi.")

        ticket_id, readable_time = id_tiket()
        folder = '/Users/admin/Documents/coding/PRAKTIKUM/Tugas 7/tickets'
        
        tiket_file = f"{ticket_id}_{nama_film}.txt"
        path_file = os.path.join(folder, tiket_file)

        with open(path_file, 'w') as file:
            file.write("+---------------------------------------------------------------+\n")
            file.write("|                       DAFTAR FILM BIOSKOP                     |\n")
            file.write("+---------------------------------------------------------------+\n")
            file.write(f"|   ID Ticket : {ticket_id:<45}|\n")
            file.write(f"|   Film      : {nama_film:<45}|\n")
            file.write(f"|   Tanggal   : {readable_time:<45}|\n")
            file.write("+---------------------------------------------------------------+\n")
            file.write("|                     Terima Kasih Telah Membeli                |\n")
            file.write("|                            Tiket Anda!                        |\n")
            file.write("+---------------------------------------------------------------+\n")

        print()
        print(f"Tiket anda berhasil dibeli. ID Tiket Anda: {ticket_id}")
        print(f"File tiket telah dibuat: {path_file}")
        print()

    def detail_tiket() :
        daftar_tiket_list = daftar_tiket()
        while True:
            opsi_tiket = int(input("Pilih nomor tiket yang ingin diliat (0 untuk kembali): "))
            if opsi_tiket == 0:
                print("Kembali ke menu pengunjung.")
                return
            elif 1 <= opsi_tiket <= len(daftar_tiket_list):
                nama_tiket = daftar_tiket_list[opsi_tiket - 1]
                break
            else:
                print("Nomor film tidak valid. Silakan coba lagi.")

        folder = '/Users/admin/Documents/coding/PRAKTIKUM/Tugas 7/tickets'  
        path_file = os.path.join(folder, nama_tiket)

        try:
            with open(path_file, "r") as tiket:
                print(tiket.read()) 
        except FileNotFoundError:
            print("File tidak ditemukan.")

    def hapus_tiket():
        daftar_tiket_list = daftar_tiket()
        while True:
            opsi_tiket = int(input("Pilih nomor tiket yang ingin dihapus (0 untuk kembali): "))
            if opsi_tiket == 0:
                print("Kembali ke menu Admin.")
                return
            elif 1 <= opsi_tiket <= len(daftar_tiket_list):
                angka_tiket = daftar_tiket_list[opsi_tiket - 1]
                break
            else:
                print("Nomor tiket tidak valid. Silakan coba lagi.")

        folder = '/Users/admin/Documents/coding/PRAKTIKUM/Tugas 7/tickets'  
        path_file = os.path.join(folder, angka_tiket)
            
        try:
            os.remove(path_file)
            print(f"Tiket '{angka_tiket}' berhasil dihapus.")
        except FileNotFoundError:
            print ("TIket tidak ditemukan")

    def pengguna_admin() :
     while True :
        print (" --- Menu Admin ---")
        print (" 1. Tambah File \n 2. Hapus File \n 3. Daftar Tiket \n 4. Kembali ")
        opsi = int(input("Pilih Opsi (1/2/3/4) : "))

        if opsi == 1 :
            while True :
                print ()
                film = input("--- Tambah File ---- \n Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali) : ")
                if film == "" :
                    print ("")
                    print ("Kembali ke Menu Admin")
                    break
                else :
                    tambah_film(film)
        elif opsi == 2 :
            while True :
                print ()
                print("--- Hapus File ----")
                daftar_film()

                film = input("Masukkan nama file yang ingin dihapus (atau 0 untuk kembali) : ")
                if film == "0" :
                    print ()
                    print ("Kembali ke Menu Admin")
                    break
                else :
                    hapus_film(film)
        elif opsi == 3 :
            while True :
                print ()
                print ("--- Daftar Tiket --- \n 1. Lihat Daftar Tiket \n 2. Lihat Detail Tiket \n 3. Hapus Tiket \n 4. Kembali")
                opsi = int(input("Pilih opsi (1/2/3/4) : "))
                if opsi == 1 :
                    print()
                    daftar_tiket()
                    print ()
                elif opsi == 2 :
                    print()
                    detail_tiket()
                    print ()
                elif opsi == 3 :
                    print ()
                    print("--- Hapus File ----")
                    hapus_tiket()
                    print ()
                elif opsi == 4 :  
                    print ()
                    break  
        elif opsi == 4 :  
            print ()
            break       
        else :
            print ("Opsi tidak Valid.")

    def pengguna_pengunjung () :
        while True :
            print (" --- Menu Pengunjung ---")
            print (" 1. Lihat Daftar Film \n 2. Beli Tiket \n 3. Kembali ")
            opsi = int(input("Pilih Opsi (1/2/3) : "))
            
            if opsi == 1 :
                print ()
                daftar_film()
                print ()
            elif opsi == 2 :
                print ()
                beli_tiket()
                print ()
            elif opsi == 3 :
                print ()
                break      
                          
    while True :
        print ()
        print ("--- Sistem Pemesanan Tiket Bioskop ---")
        print (' 1. Admin \n 2. Pengunjung \n 3. Keluar ')
        menu = int(input("Pilih peran (1/2/3) : "))

        if menu == 1 :
            print ()
            pengguna_admin()  
        elif menu == 2 :
            print ()   
            pengguna_pengunjung()
        elif menu == 3:
            print("Terima kasih telah menggunakan sistem pemesanan tiket.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

sistem_informasi_bioskop()


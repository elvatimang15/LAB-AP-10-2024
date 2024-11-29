"""
Buatlah aplikasi manajemen kontak dengan fungsi-fungsi berikut:

Validasi Data Kontak:
Buat fungsi validasi_data(nama, nomor_telepon, email) untuk memvalidasi data kontak:

- Nama: huruf dan spasi, minimal 3 karakter.
- Nomor telepon: dimulai dengan +62 diikuti 11 digit.
- Email: sesuai format email yang valid.

dengan fungsi yang mencakup
1) Menambah Kontak:
Fungsi tambah_kontak(data_kontak) untuk menambah kontak baru, dengan memeriksa validitas dan duplikasi berdasarkan nama dan email.

2) Mencari Kontak Berdasarkan Nama dan Email:
Fungsi cari_kontak_nama(nama, data_kontak) dan cari_kontak_email(email, data_kontak) untuk mencari kontak berdasarkan nama dan email (case-insensitive).

3) Menghapus Kontak Berdasarkan Nama dan Email:
Fungsi hapus_kontak_nama(nama, data_kontak) dan hapus_kontak_email(email, data_kontak) untuk menghapus kontak berdasarkan nama atau email.

4) Menampilkan Daftar Kontak:
Fungsi untuk menampilkan semua kontak, terurut berdasarkan nama.

5) Menampilkan Kontak dengan Email Valid:
Fungsi untuk menampilkan kontak yang memiliki email valid.

dan akan menampilkan menu aksi sebagai berikut:

Menu Aksi:
Buat menu interaktif dengan pilihan:

1. Tambah kontak
2. Tampilkan jumlah kontak
3. Tampilkan kontak (urut nama)
4. Cari kontak berdasarkan nama/email
5. Hapus kontak berdasarkan nama/email
6. Keluar

"""

import re

def validasi_data(nama, nomor_telepon, email):
    if not re.match("^[A-Za-z ]{3,}$", nama):
        print("Nama kontak tidak valid. Harus terdiri dari huruf dan spasi dan minimal 3 karakter.")
        return False

    if not re.match("^\+62[0-9]{11}$", nomor_telepon):  
        print("Nomor telepon tidak valid.")
        return False
    
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        print("Email tidak valid.")
        return False
    
    return True

def get_nama(kontak):
    return kontak['nama']

def cari_kontak_nama(nama, data_kontak):
    hasil = [kontak for kontak in data_kontak if nama.lower() in kontak['nama'].lower()]
    return hasil

def cari_kontak_email(email, data_kontak):
    hasil = [kontak for kontak in data_kontak if email.lower() in kontak['email'].lower()]
    return hasil

def hapus_kontak_nama(nama, data_kontak):
    for i, kontak in enumerate(data_kontak):
        if nama.lower() == kontak['nama'].lower():
            del data_kontak[i]
            return True
    return False

def hapus_kontak_email(email, data_kontak):
    for i, kontak in enumerate(data_kontak):
        if email.lower() == kontak['email'].lower():
            del data_kontak[i]
            return True
    return False

def tambah_kontak(data_kontak):
    nama = input("Masukkan nama kontak: ")
    nomor_telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan alamat email: ")
    
    for kontak in data_kontak:
        if kontak['nama'].lower() == nama.lower() and kontak['email'].lower() == email.lower():
            print("Kontak dengan nama dan email tersebut sudah ada.")
            return  

    if validasi_data(nama, nomor_telepon, email):
        data_kontak.append({"nama": nama, "nomor_telepon": nomor_telepon, "email": email})
        print("Kontak berhasil ditambahkan!")
    else:
        print("Data kontak tidak valid, coba lagi.")

data_kontak = []

while True:
    print("\nPilih aksi:")
    print("1. Tambah kontak baru") 
    print("2. Tampilkan jumlah kontak valid")
    print("3. Tampilkan daftar kontak (urut berdasarkan nama)")
    print("4. Tampilkan kontak dengan email valid")
    print("5. Cari kontak berdasarkan nama")
    print("6. Cari kontak berdasarkan email")
    print("7. Hapus kontak berdasarkan nama")
    print("8. Hapus kontak berdasarkan email")
    print("9. Keluar") 
    
    pilihan = input("Masukkan pilihan (1-9): ")

    if pilihan == '1':
        tambah_kontak(data_kontak) 
    elif pilihan == '2':
        print(f"Jumlah kontak valid: {len(data_kontak)}")
    elif pilihan == '3':
        data_kontak_urut = sorted(data_kontak, key=get_nama)  
        print("\nDaftar kontak (urut berdasarkan nama):")
        for kontak in data_kontak_urut:
            print(f"{kontak['nama']} - {kontak['nomor_telepon']} - {kontak['email']}")
    elif pilihan == '4':
        print("\nKontak dengan email valid:")
        for kontak in data_kontak:
            print(f"{kontak['email']}")
    elif pilihan == '5':
        nama_pencarian = input("Masukkan nama untuk pencarian: ")
        hasil = cari_kontak_nama(nama_pencarian, data_kontak)
        if hasil:
            for kontak in hasil:
                print(f"Ditemukan: {kontak['nama']} - {kontak['nomor_telepon']} - {kontak['email']}")
        else:
            print("Kontak tidak ditemukan.")
    elif pilihan == '6':
        email_pencarian = input("Masukkan email untuk pencarian: ")
        hasil = cari_kontak_email(email_pencarian, data_kontak)
        if hasil:
            for kontak in hasil:
                print(f"Ditemukan: {kontak['nama']} - {kontak['nomor_telepon']} - {kontak['email']}")
        else:
            print("Kontak tidak ditemukan.")
    elif pilihan == '7':
        nama_hapus = input("Masukkan nama untuk dihapus: ")
        if hapus_kontak_nama(nama_hapus, data_kontak):
            print(f"Kontak {nama_hapus} telah dihapus.")
        else:
            print("Kontak tidak ditemukan.")
    elif pilihan == '8':
        email_hapus = input("Masukkan email untuk dihapus: ")
        if hapus_kontak_email(email_hapus, data_kontak):
            print(f"Kontak dengan email {email_hapus} telah dihapus.")
        else:
            print("Kontak tidak ditemukan.")
    elif pilihan == '9':
        print("Terima kasih telah menggunakan aplikasi kontak. Keluar...")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")

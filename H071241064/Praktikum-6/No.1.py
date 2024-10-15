inventory = {}

def tambah_barang():
    # Menambah barang baru ke dalam inventory.
    kode = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
        harga = float(input("Masukkan harga per unit: "))
    except ValueError:
        print("Input jumlah atau harga tidak valid. Silakan coba lagi.\n")
        return

    if kode in inventory:
        print("Barang sudah ada. Gunakan fungsi update untuk memperbarui.")
    else:
        inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print("Barang berhasil ditambahkan.\n")

def tampilkan_barang():
    if not inventory:   
        print("Inventori kosong.")
    else:
        for kode, data in inventory.items():
            print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']}")
    print()

def hapus_barang():
    # Menghapus barang dari inventory.
    kode = input("Masukkan kode barang yang akan dihapus: ")

    if kode in inventory:
        del inventory[kode]
        print("Barang berhasil dihapus.\n")
    else:
        print("Barang tidak ditemukan.\n")

def cari_barang():
    # Mencari barang berdasarkan kode atau nama.
    pencarian = input("Cari berdasarkan (1) Kode atau (2) Nama: ")
    hasil_cari = []

    if pencarian == '1':
        kode = input("Masukkan kode barang: ")
        if kode in inventory:
            hasil_cari.append((kode, inventory[kode]))
    elif pencarian == '2':
        nama = input("Masukkan nama barang: ")
        hasil_cari = [(kode, data) for kode, data in inventory.items() if data['nama'].lower() == nama.lower()]

    if hasil_cari:
        for kode, data in hasil_cari:
            print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}\n")
    else:
        print("Barang tidak ditemukan.\n")

def update_barang():
    kode = input("Masukkan kode barang yang ingin diupdate: ")

    if kode in inventory:
        try:
            nama = input("Masukkan nama baru: ")
            jumlah = int(input("Masukkan jumlah baru: "))
            harga = float(input("Masukkan harga per unit baru: "))
        except ValueError:
            print("Input jumlah atau harga tidak valid. Silakan coba lagi.\n")
            return
        
        inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print("Data barang berhasil diperbarui.\n")
    else:
        print("Barang tidak ditemukan.\n")

def menu():
    """Menampilkan menu interaktif."""
    while True:
        print("Menu Inventory:")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Update Data Barang")
        print("6. Keluar")
        
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program inventori.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Menjalankan program
if __name__ == "__main__": 
    menu()
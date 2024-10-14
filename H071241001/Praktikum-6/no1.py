# Inventory Barang Sederhana
inventory = {}

def tampilkan_menu():
    print("\n=== Menu Inventori Barang ===")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Barang")
    print("4. Cari Barang")
    print("5. Update Barang")
    print("6. Keluar")

def tambah_barang():
    kode_barang = input("Masukkan Kode Barang: ")
    nama_barang = input("Masukkan Nama Barang: ")
    jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    harga_barang = float(input("Masukkan Harga per Unit: "))
    inventory[kode_barang] = {
        'nama': nama_barang,
        'jumlah': jumlah_barang,
        'harga': harga_barang
    }
    print("Barang berhasil ditambahkan.")

def hapus_barang():
    kode_barang = input("Masukkan Kode Barang yang ingin dihapus: ")
    if kode_barang in inventory:
        del inventory[kode_barang]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def tampilkan_daftar_barang():
    if inventory:                 
        print("\nDaftar Barang:")
        for kode, data in inventory.items():
            print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']:.2f}")
    else:
        print("Inventory kosong.")

def cari_barang():
    pilihan = input("Cari berdasarkan (1) Kode atau (2) Nama: ")
    if pilihan == '1':
        kode_barang = input("Masukkan Kode Barang: ")
        if kode_barang in inventory:
            data = inventory[kode_barang]
            print(f"Kode: {kode_barang}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']:.2f}")
        else:
            print("Barang tidak ditemukan.")
    elif pilihan == '2':
        nama_barang = input("Masukkan Nama Barang: ")
        for kode, data in inventory.items():
            if data['nama'].lower() == nama_barang.lower():
                print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per unit: {data['harga']:.2f}")
                return
        print("Barang tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")

def update_barang():
    kode_barang = input("Masukkan Kode Barang yang ingin diupdate: ")
    if kode_barang in inventory:
        nama_barang = input("Masukkan Nama Barang baru: ")
        jumlah_barang = int(input("Masukkan Jumlah Barang baru: "))
        harga_barang = float(input("Masukkan Harga per Unit baru: "))
        inventory[kode_barang] = {
            'nama': nama_barang,
            'jumlah': jumlah_barang,
            'harga': harga_barang
        }
        print("Data barang berhasil diupdate.")
    else:
        print("Barang tidak ditemukan.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-6): ")
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_daftar_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
inventory = {}
kode_barang_list = []  # List untuk menyimpan kode barang

def add_item():
    kode_barang = input("Masukkan Kode Barang: ")
    nama_barang = input("Masukkan Nama Barang: ")
    jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    harga_barang = float(input("Masukkan Harga per Unit: "))
    
    inventory[kode_barang] = {
        'nama': nama_barang,
        'jumlah': jumlah_barang,
        'harga': harga_barang
    }
    kode_barang_list.append(kode_barang)  # Tambahkan kode barang ke list
    print("Barang berhasil ditambahkan.")

def delete_item():
    kode_barang = input("Masukkan Kode Barang yang akan dihapus: ")
    if kode_barang in inventory:
        del inventory[kode_barang]
        kode_barang_list.remove(kode_barang)  # Hapus dari list
        print("Barang berhasil dihapus.")
    else:
        print("Kode barang tidak ditemukan.")

def display_items():
    if not inventory:
        print("Tidak ada barang dalam inventory.")
    else:
        print("\nDaftar Barang:")
        for kode, data in inventory.items():
            print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per Unit: {data['harga']:.2f}")

def search_item():
    print("Cari berdasarkan (1) Kode atau (2) Nama:")
    pilihan = input("Pilih (1/2): ")
    
    if pilihan == '1':
        kode_barang = input("Masukkan Kode Barang yang dicari: ")
        if kode_barang in inventory:
            data = inventory[kode_barang]
            print(f"Barang Ditemukan - Kode: {kode_barang}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per Unit: {data['harga']:.2f}")
        else:
            print("Kode barang tidak ditemukan.")
    elif pilihan == '2':
        nama_barang = input("Masukkan Nama Barang yang dicari: ")
        found = False
        for kode, data in inventory.items():
            if data['nama'].lower() == nama_barang.lower():
                print(f"Barang Ditemukan - Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga per Unit: {data['harga']:.2f}")
                found = True
                break
        if not found:
            print("Nama barang tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")

def update_item():
    kode_barang = input("Masukkan Kode Barang yang akan diupdate: ")
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
        print("Kode barang tidak ditemukan.")


def main():
    while True:
        print("\n=== Menu Inventory Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Update Data Barang")
        print("6. Keluar")
        print("==============================")
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            add_item()
        elif pilihan == '2':
            delete_item()
        elif pilihan == '3':
            display_items()
        elif pilihan == '4':
            search_item()
        elif pilihan == '5':
            update_item()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program inventori.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


main()

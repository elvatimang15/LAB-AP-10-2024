inventory = {}

def tambah_barang():
    kode = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    harga = float(input("Masukkan harga barang: "))
    
    if kode in inventory:
        print("Barang dengan kode tersebut sudah ada.")
    else:
        inventory.update({kode: {'nama': nama, 'jumlah': jumlah, 'harga': harga}})
        print("Barang berhasil ditambahkan.")

def hapus_barang():
    kode = input("Masukkan kode barang yang akan dihapus: ")
    if inventory.pop(kode, None) is not None:
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def tampilkan_barang():
    if inventory:
        print("Daftar Barang:")
        for kode, data in inventory.items():
            print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("Inventory kosong.")

def cari_barang():
    print("Pilih metode pencarian:")
    print("1. Cari berdasarkan kode barang")
    print("2. Cari berdasarkan nama barang")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        kode = input("Masukkan kode barang yang akan dicari: ")
        data = inventory.get(kode)
        if data:
            print(f"Barang ditemukan:\nKode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
        else:
            print("Barang tidak ditemukan berdasarkan kode.")
    
    elif pilihan == '2':
        nama = input("Masukkan nama barang yang akan dicari: ")
        ditemukan = False
        for kode, data in inventory.items():
            if data['nama'].lower() == nama.lower():  
                print(f"Barang ditemukan:\nKode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
                ditemukan = True
                break
        if not ditemukan:
            print("Barang tidak ditemukan berdasarkan nama.")
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def update_barang():
    kode = input("Masukkan kode barang yang akan diupdate: ")
    data = inventory.get(kode)
    if data:
        print("Data lama:", data)
        nama_baru = input("Masukkan nama barang baru (biarkan kosong jika tidak diubah): ")
        jumlah_baru = input("Masukkan jumlah barang baru (biarkan kosong jika tidak diubah): ")
        harga_baru = input("Masukkan harga barang baru (biarkan kosong jika tidak diubah): ")
        
        if nama_baru:
            data['nama'] = nama_baru
        if jumlah_baru:
            data['jumlah'] = int(jumlah_baru)
        if harga_baru:
            data['harga'] = float(harga_baru)
            
        print("Barang berhasil diupdate.")
    else:
        print("Barang tidak ditemukan.")

def main_menu():
    while True:
        print("\n=== Program Inventory Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar")
        
        pilihan = input("Pilih menu: ")
        
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
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

main_menu()

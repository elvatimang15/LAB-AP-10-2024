def inventori_barang() :
    inventori = []

    def tambah_barang(kode, nama, jumlah, harga) :
            barang = {
        'kode': kode,
        'nama': nama,
        'jumlah': jumlah,
        'harga': harga
    }
            inventori.append(barang)

    def hapus_barang(kode) :
          for item in inventori:
                if item['kode'] == kode:
                    inventori.remove(item)
                    print(f"Barang dengan '{kode}' telah dihapus.")
                    return
                else :
                    print(f"Barang dengan kode '{kode}' tidak ditemukan.")
                    break

    def tampilkan_barang():
        if not inventori:
            print("Inventori kosong.")
        else:
            print("\n=== Daftar Barang ===")
            for barang in inventori:
                print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")

    def cari_barang(parameter, is_kode=True) :
        for item in inventori:
            if (is_kode and item['kode'] == parameter) or (not is_kode and item['nama'].lower() == parameter.lower()):
                print(f"Kode : {item['kode']}, Nama: {item['nama']}, Jumlah : {item['jumlah']}, Harga per unit : {item['harga']}")

    def update_barang(kode):
        for item in inventori:
            if item['kode'] == kode :
               jumlah_baru = int(input("Masukkan jumlah baru: "))
               harga_baru = float(input("Masukkan harga baru: "))

               item['jumlah'] = jumlah_baru
               item['harga'] = harga_baru

               print ("Data barang berhasil diperbarui")
               break

    while True :
        print ("=== Menu Inventori Barang === \n 1. Tambah barang \n 2. Hapus barang \n 3. Tampilkan barang \n 4. Cari barang \n 5. Update barang \n 6. Keluar")
        menu = int(input("Pilih Opsi (1-6) : "))

        if menu == 1 :
            kode = input("Masukkan Kode Barang: ")
            nama = input("Masukkan Nama Barang: ")
            jumlah = int(input("Masukkan Jumlah Barang: "))
            harga = float(input("Masukkan Harga per Unit: "))
            tambah_barang(kode, nama, jumlah, harga)
            print (f"Kode : {kode}, Nama: {nama}, Jumlah : {jumlah}, Harga per unit : {harga}")
            print ("")

        elif menu == 2 :
            kode = input("Masukkan kode barang yang akan dihapus: ")
            hapus_barang(kode)
            print ("")

        elif menu == 3 :
            tampilkan_barang()
            print ("")

        elif menu == 4 :
            cari = int(input("Cari berdasarkan (1) Kode atau (2) Nama : "))
            if cari == 1 :
                kode = input("Masukkan kode barang : ")
                cari_barang(kode, is_kode=True)
            elif cari == 2 :
                nama = input("Masukkan nama barang : ")
                cari_barang(nama, is_kode=False)
            print ("")

        elif menu == 5 :
            kode = input("Masukkan kode barang yang akan diperbarui: ")
            update_barang(kode)
            print ("")

        elif menu == 6 :
            print ("== Terima kasih telah menggunakan program inventori ==")
            print ("")
            break   
               
        else :
            print ("Opsi tidak valid. Pilih opsi 1-6.")
            print ("")
            
inventori_barang()
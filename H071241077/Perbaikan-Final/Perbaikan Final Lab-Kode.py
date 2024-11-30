import re

def tambah_buku(perpustakaan, judul, kategori):
    format_judul = judul.lower()
    if format_judul not in (key.lower() for key in perpustakaan):
        perpustakaan[judul] = kategori
        print(f"\nBuku '{judul}' berhasil ditambahkan ke kategori '{kategori}'.")
    else:
        print(f"\nBuku '{judul}' sudah ada dalam perpustakaan.")

def cari_buku(perpustakaan, pola):
    # Mencari buku berdasarkan pola regex secara case-insensitive
    hasil = [judul for judul in perpustakaan if re.search(pola, judul, re.IGNORECASE)]
    if hasil:
        print("\nHasil pencarian buku:")
        for judul in hasil:
            print(f"- {judul} (Kategori: {perpustakaan[judul]})")
    else:
        print(f"\nTidak ditemukan buku dengan pola '{pola}'.")

def tampilkan_buku(perpustakaan):
    # Menampilkan semua buku dalam perpustakaan
    if perpustakaan:
        print("\nDaftar Buku dalam Perpustakaan:")
        for idx, (judul, kategori) in enumerate(perpustakaan.items(), start=1):
            print(f"{idx}. {judul} - {kategori}")
    else:
        print("\nPerpustakaan masih kosong.")

def hapus_buku(perpustakaan, judul):
    # Menghapus buku berdasarkan judul secara case-insensitive
    format_judul = judul.lower()
    for key in list(perpustakaan):
        if key.lower() == format_judul:
            del perpustakaan[key]
            print(f"\nBuku '{judul}' berhasil dihapus dari perpustakaan.")
            return
    print(f"\nBuku '{judul}' tidak ditemukan di perpustakaan.")

perpustakaan = {}

while True:
    print("\n========== MENU PERPUSTAKAAN ==========")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Tampilkan Semua Buku")
    print("4. Hapus Buku")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul_buku = input("Masukkan judul buku: ").strip()
        kategori_buku = input("Masukkan kategori buku: ").strip()
        tambah_buku(perpustakaan, judul_buku, kategori_buku)
    elif pilihan == "2":
        pola = input("Masukkan pola pencarian: ")
        cari_buku(perpustakaan, pola)
    elif pilihan == "3":
        tampilkan_buku(perpustakaan)
    elif pilihan == "4":
        judul_hapus = input("Masukkan judul buku yang ingin dihapus: ").strip()
        hapus_buku(perpustakaan, judul_hapus)
    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan sistem perpustakaan!")
        break
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")

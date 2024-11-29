import re  # Mengimpor modul regex untuk pencarian pola pada nama buku

# Function untuk menambahkan buku ke dalam perpustakaan
def tambah_buku(perpustakaan, judul, kategori):
    """Menambahkan buku ke dalam koleksi perpustakaan."""
    if judul not in perpustakaan:  # Conditional statement untuk memeriksa apakah buku sudah ada
        perpustakaan[judul] = kategori  # Menambahkan buku sebagai key, dan kategori sebagai value
        print(f"\nBuku '{judul}' berhasil ditambahkan ke kategori '{kategori}'.")
    else:
        print(f"\nBuku '{judul}' sudah ada dalam perpustakaan.")

# Function untuk mencari buku berdasarkan pola Regex
def cari_buku(perpustakaan, pola):
    """Mencari buku berdasarkan pola regex."""
    hasil = [judul for judul in perpustakaan if re.search(pola, judul, re.IGNORECASE)]  # List comprehension dengan Regex
    if hasil:
        print("\nHasil pencarian buku:")
        for judul in hasil:
            print(f"- {judul.capitalize()} (Kategori: {perpustakaan[judul]})")
    else:
        print(f"\nTidak ditemukan buku dengan pola '{pola}'.")

# Function untuk menampilkan semua buku dalam perpustakaan
def tampilkan_buku(perpustakaan):
    """Menampilkan semua buku dalam perpustakaan."""
    if perpustakaan:  # Conditional statement untuk memeriksa apakah perpustakaan kosong
        print("\nDaftar Buku dalam Perpustakaan:")
        for idx, (judul, kategori) in enumerate(perpustakaan.items(), start=1):  # Looping untuk mencetak buku
            print(f"{idx}. {judul.capitalize()} - {kategori.capitalize()}")  # String manipulation
    else:
        print("\nPerpustakaan masih kosong.")

# Function untuk menghapus buku dari perpustakaan
def hapus_buku(perpustakaan, judul):
    """Menghapus buku berdasarkan judul."""
    if judul in perpustakaan:  # Conditional statement untuk memastikan buku ada
        del perpustakaan[judul]  # Menghapus buku dari koleksi
        print(f"\nBuku '{judul}' berhasil dihapus dari perpustakaan.")
    else:
        print(f"\nBuku '{judul}' tidak ditemukan di perpustakaan.")

# Data type collection: Menggunakan dictionary untuk menyimpan buku dan kategorinya
perpustakaan = {}

# Menu interaktif menggunakan loop
while True:
    print("\n========== MENU PERPUSTAKAAN ==========")
    print("1. Tambah Buku")
    print("2. Cari Buku (Regex)")
    print("3. Tampilkan Semua Buku")
    print("4. Hapus Buku")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul_buku = input("Masukkan judul buku: ").strip()  # String manipulation: Menghapus spasi berlebih
        kategori_buku = input("Masukkan kategori buku: ").strip()
        tambah_buku(perpustakaan, judul_buku, kategori_buku)
    elif pilihan == "2":
        pola = input("Masukkan pola pencarian (Regex): ")
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
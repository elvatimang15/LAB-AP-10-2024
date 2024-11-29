import re

def validasi_produk(produk):
    pattern = r'^[a-zA-Z\s]+;\d+(\.\d+)?;[a-zA-Z\s]+$'  
    return re.match(pattern, produk)

def klasifikasi_produk(list_produk):
    murah = []
    sedang = []
    mahal = []
    tidak_valid = []
    kategori_tertentu = []

    for produk in list_produk:
        produk = produk.strip()  
        if validasi_produk(produk):
            nama, harga, kategori = [item.strip() for item in produk.split(';')]  
            harga = float(harga)  

            if harga < 50:
                murah.append((nama, harga, kategori))
            elif 50 <= harga <= 100:
                sedang.append((nama, harga, kategori))
            else:
                mahal.append((nama, harga, kategori))

            if kategori.lower() == "elektronik":
                kategori_tertentu.append((nama, harga, kategori))
        else:
            tidak_valid.append(produk)
    
    return murah, sedang, mahal, tidak_valid, kategori_tertentu

def main():
    daftar_produk = input("Masukkan daftar produk (Nama;Harga;Kategori), dipisahkan dengan koma: ")
    list_produk = daftar_produk.split(",")
    
    murah, sedang, mahal, tidak_valid, kategori_tertentu = klasifikasi_produk(list_produk)

    print("\nHasil Klasifikasi Produk:")

    print("\nProduk Murah (Harga < 50):")
    for nama, harga, kategori in murah:
        print(f"- {nama} (${harga:.2f}) [{kategori}]")

    print("\nProduk Sedang (Harga 50-100):")
    for nama, harga, kategori in sedang:
        print(f"- {nama} (${harga:.2f}) [{kategori}]")

    print("\nProduk Mahal (Harga > 100):")
    for nama, harga, kategori in mahal:
        print(f"- {nama} (${harga:.2f}) [{kategori}]")

    print("\nProduk Tidak Valid (Format Salah):")
    print(", ".join(tidak_valid) if tidak_valid else "Tidak ada.")

    print("\nProduk Kategori 'Elektronik':")
    for nama, harga, kategori in kategori_tertentu:
        print(f"- {nama} (${harga:.2f}) [{kategori}]")

main()
def main():
    jarak_total = 0
    langkah_bahaya = False

    while True:
        try:
            langkah = input("Masukkan langkah (meter) atau 0 untuk selesai: ")
            if langkah == "0":
                break
            
            langkah = int(langkah)

            if langkah < 0:
                print("Input tidak valid. Masukkan bilangan bulat positif.")
                continue
            elif langkah > 20:
                langkah_bahaya = True
            
            jarak_total += langkah

        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
            continue

    # Menampilkan total jarak yang telah ditempuh
    print(f"Total jarak: {jarak_total} meter")

    # Menentukan keputusan akhir
    if langkah_bahaya:
        print("Ada bahaya: Ya")
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif jarak_total == 50:
        print("Ada bahaya: Tidak")
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Ada bahaya: Tidak")
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")
    
    

# Memanggil fungsi utama
main()
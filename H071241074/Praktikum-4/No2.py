def langkah_valid(langkah):
    try:
        langkah = int(langkah)
        return langkah >= 0, langkah  
    except ValueError:
        return False, 0  

def cek_bahaya(langkah):
    return langkah > 20

def main():
    total_jarak = 0
    ada_bahaya = False

    while True:
        langkah = input("Masukkan langkah (meter) atau 0 untuk selesai: ")
        valid, langkah = langkah_valid(langkah)

        if not valid:
            print("Input tidak valid. Masukkan angka bulat.")
            continue

        if langkah == 0:
            break

        if cek_bahaya(langkah):
            ada_bahaya = True

        total_jarak += langkah  

        if total_jarak >= 50:
            break
    print(f"Total jarak: {total_jarak} meter")
    
    if ada_bahaya:
        print("Ada bahaya: Ya")
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif not ada_bahaya and total_jarak == 50:
        print("Ada bahaya: Tidak")
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    elif not ada_bahaya and total_jarak != 50:
        print("Ada bahaya: Tidak")
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")

main()
